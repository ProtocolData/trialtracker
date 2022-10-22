import pandas as pd
import numpy as np
import psycopg2
import getpass
import pandas.io.sql as psql
import os


def get_term_str():
	my_path = os.path.abspath(os.path.dirname(__file__))
	# path = os.path.join(my_path, "extracted_data/ct_fb_parser_data.csv")
	term_path = os.path.join(my_path, "extracted_data/cancer_terms.csv")

	# print(f"Reading cancer terms from: {term_path}")
	terms=pd.read_csv(term_path, dtype=str)

	temp_str=""
	for i, r in terms.iterrows(): 
	    if i>0:
	        temp_str+=" or "
	    if r[1]!=r[1]: #returns True if r[1] is NaN
	        temp_str+=f"c.downcase_name like '%{r[0]}%'"
	    if r[1]==r[1]: #returns True if r[1] is not NaN
	        temp_str+=f"(c.downcase_name like '%{r[0]}%'"
	        temp_str+=f" and downcase_name not like '%{r[1]}%'"
	        if r[2]==r[2]: #returns True if r[2] is not NaN
	            temp_str+=f" and downcase_name not like '%{r[2]}%'"
	        temp_str+=")"
	return temp_str


def get_default_query(term_str: str, fb_parser_format=True, nct_list=[]):
	#has some rarer terminology https://www.clinicaltrials.gov/ct2/show/NCT03050268

	nct_str="t.nct_id"
	fb_nct_str="""t.nct_id AS \"#nct_id\""""

	ncts="'"+"','". join(nct_list)+"'"

	nct_list_str=f"or s.nct_id in ({ncts})"

	query=f"""
	with cancer_trials as (select  distinct s.nct_id,s.brief_title AS title,
	s.start_date,
	s.overall_status,
	s.phase,
	s.enrollment,
	s.enrollment_type,
		
	s.study_type,
		s.number_of_arms,
		s.number_of_groups,
		s.why_stopped,
		s.has_dmc,
		s.is_fda_regulated_drug,
		s.is_fda_regulated_device,
		s.is_unapproved_device,
		s.is_ppsd,
		s.is_us_export

	from ctgov.studies s
	inner join ctgov.conditions c
	on s.nct_id=c.nct_id
	where 
	(

	({term_str})
	)

	
	{nct_list_str if len(nct_list)>0 else ""}


	)
	,



	conditions as (
	SELECT
	c.nct_id,
	STRING_AGG(c.name, '|' ORDER BY name) AS conditions
	FROM cancer_trials t
	inner join ctgov.conditions c
	on t.nct_id=c.nct_id	
	GROUP BY
	c.nct_id	
	),

	sponsors as (
	select 
	s.nct_id,
	STRING_AGG(s.name, '|' ORDER BY name) AS lead_sponsor
		
	from ctgov.sponsors s
	where s.lead_or_collaborator='lead'	
	group by s.nct_id	
	),
	
	responsible_parties as (
	select 
	r.nct_id,
	STRING_AGG(r.name, '|') AS responsible_party_name,
	STRING_AGG(r.responsible_party_type, '|') AS responsible_party_type,
	STRING_AGG(r.title, '|') AS responsible_party_title,
	STRING_AGG(r.organization, '|') AS responsible_party_organization,
	STRING_AGG(r.affiliation, '|') AS responsible_party_affiliation
		
	from ctgov.responsible_parties r
	group by r.nct_id
	),
	
	principal_investigators as (
	select 
	o.nct_id,
	STRING_AGG(o.name, '|') AS pi_name,
	STRING_AGG(o.role, '|') AS pi_role,
	STRING_AGG(o.affiliation, '|') AS pi_affiliation
		
	from ctgov.overall_officials o
	where o.role='Principal Investigator'
	group by o.nct_id
	),

	facilities as (
	select 
	f.nct_id,
	count(distinct case when f.country='United States' then id else null end) as us_facility_count,
	count(distinct id) as total_facility_count,
	count(distinct case when f.country='United States' then id else null end)*1.0/
	count(distinct id) as percent_us_facilities
		
	from ctgov.facilities f
	group by f.nct_id
	)

	select 
	
	{fb_nct_str if fb_parser_format else nct_str},
	t.title,
	CASE WHEN cv.has_us_facility THEN 'true' ELSE 'false' END AS has_us_facility,
	c.conditions,
	e.criteria AS eligibility_criteria, 
	t.start_date, s.lead_sponsor, b.description as summary, t.overall_status, t.phase, t.enrollment, t.enrollment_type, t.study_type, t.number_of_arms, t.number_of_groups, t.why_stopped, t.has_dmc, t.is_fda_regulated_drug, t.is_fda_regulated_device, t.is_unapproved_device, t.is_ppsd, t.is_us_export,
	r.responsible_party_name,
	r.responsible_party_type,
	r.responsible_party_title,
	r.responsible_party_organization,
	r.responsible_party_affiliation,
	pi.pi_name,
	pi.pi_role,
	pi.pi_affiliation,
	case 
	when lower(pi.pi_affiliation) LIKE CONCAT('%', lower(s.lead_sponsor), '%') 
	or lower(s.lead_sponsor) LIKE CONCAT('%', lower(pi.pi_affiliation), '%') 
	or lower(s.lead_sponsor) LIKE CONCAT('%', lower(pi.pi_name), '%') 
	or lower(pi.pi_name) LIKE CONCAT('%', lower(s.lead_sponsor), '%')
	or (lower(t.title) like '%investigator%' and lower(t.title) like '%initiated%')
	then TRUE else FALSE end as investigator_initiated_study,
	f.us_facility_count,
	f.total_facility_count,
	f.percent_us_facilities

	from cancer_trials t

	inner join conditions c
	on t.nct_id=c.nct_id

	left join ctgov.calculated_values cv
	on cv.nct_id=t.nct_id

	left join ctgov.eligibilities e
	on e.nct_id=t.nct_id

	left join sponsors s
	on s.nct_id=t.nct_id

	left join responsible_parties r
	on r.nct_id=t.nct_id
	
	left join principal_investigators pi
	on pi.nct_id=t.nct_id

	left join facilities f
	on f.nct_id=t.nct_id

	left join ctgov.brief_summaries b
	on b.nct_id=t.nct_id

	order by t.nct_id asc;
	"""

	return query


def get_cancer_trial_sites(term_str: str):
	query=f"""
	with cancer_trials as (select  distinct s.nct_id,s.brief_title AS title,
	s.start_date,
	s.overall_status,
	s.phase,
	s.enrollment,
	s.enrollment_type,
		
	s.study_type,
		s.number_of_arms,
		s.number_of_groups,
		s.why_stopped,
		s.has_dmc,
		s.is_fda_regulated_drug,
		s.is_fda_regulated_device,
		s.is_unapproved_device,
		s.is_ppsd,
		s.is_us_export

	from ctgov.studies s
	inner join ctgov.conditions c
	on s.nct_id=c.nct_id
	where 
	(
	{term_str}
	)
	) 

	select 
	t.nct_id,
	t.title,
	CASE WHEN cv.has_us_facility THEN 'true' ELSE 'false' END AS has_us_facility,
	t.start_date, t.overall_status, t.phase, t.enrollment, t.enrollment_type, t.study_type, t.number_of_arms, t.number_of_groups, t.why_stopped, t.has_dmc, t.is_fda_regulated_drug, t.is_fda_regulated_device, t.is_unapproved_device, t.is_ppsd, t.is_us_export,
	f.id as facility_id,
	f.name as facility_name,
	f.status as facility_status,
	f.city as facility_city,
	f.state as facility_state,
	f.zip as facility_zip,
	f.country as facility_country

	from cancer_trials t

	left join ctgov.calculated_values cv
	on cv.nct_id=t.nct_id

	left join ctgov.facilities f
	on t.nct_id=f.nct_id
	
	order by t.nct_id asc


	;
	"""

	return query



def query_aact(query):
	connection=False
	try:
	  # Connect to an existing database
	  connection = psycopg2.connect(user=getpass.getpass("What is your AACT username?  If you don't have one, please sign up for access here: https://aact.ctti-clinicaltrials.org/users/sign_up"),
	                                password=getpass.getpass('What is your AACT password?'),
	                                host="aact-db.ctti-clinicaltrials.org",
	                                port="5432",
	                                database="aact")


	  # Create a cursor to perform database operations
	  df = psql.read_sql(query, connection)
	  connection.close()
	  return df
	  # print("You are connected to - ", record, "\n")

	except:
	  print("Error while connecting to PostgreSQL.  Please see https://aact.ctti-clinicaltrials.org/connect for more details.")
	finally:
	  if (connection):
	      connection.close()
	      print("PostgreSQL connection is now closed")


def download_data(query=get_default_query(get_term_str()), filename="ct_fb_parser_data.csv"):
	file_path="extracted_data/"+filename
	my_path = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(my_path, file_path)


	try:
		df=query_aact(query)
		df.to_csv(path)

	except:
	  print("Data download failed.  Please check credentials and query and try again.")
  

if __name__ == "__main__":
	print(f"Running {__file__} file directly...")

	download_data()

