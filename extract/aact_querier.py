import pandas as pd
import numpy as np
import psycopg2
import getpass
import pandas.io.sql as psql


def get_default_query():
	query="""
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
	(c.downcase_name like '%cancer%'
	or c.downcase_name like '%neoplasm%'
	or c.downcase_name like '%tumor%'
	or c.downcase_name like '%malignancy%'
	or c.downcase_name like '%oncology%'
	or c.downcase_name like '%neoplasia%'
	or c.downcase_name like '%neoplastic%'
	) 
	# or
	# (s.brief_title like '%cancer%'
	# or s.brief_title like '%neoplasm%'
	# or s.brief_title like '%tumor%'
	# or s.brief_title like '%malignancy%'
	# or s.brief_title like '%oncology%'
	# or s.brief_title like '%neoplasia%'
	# or s.brief_title like '%neoplastic%')
	))
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
	)

	select 
	t.nct_id,
	t.title,
	CASE WHEN cv.has_us_facility THEN 'true' ELSE 'false' END AS has_us_facility,
	c.conditions,
	e.criteria AS eligibility_criteria, 
	t.start_date, s.lead_sponsor, b.description as summary, t.overall_status, t.phase, t.enrollment, t.enrollment_type, t.study_type, t.number_of_arms, t.number_of_groups, t.why_stopped, t.has_dmc, t.is_fda_regulated_drug, t.is_fda_regulated_device, t.is_unapproved_device, t.is_ppsd, t.is_us_export

	from cancer_trials t

	inner join conditions c
	on t.nct_id=c.nct_id

	left join ctgov.calculated_values cv
	on cv.nct_id=t.nct_id

	left join ctgov.eligibilities e
	on e.nct_id=t.nct_id

	left join sponsors s
	on s.nct_id=t.nct_id

	left join ctgov.brief_summaries b
	on b.nct_id=t.nct_id

	order by t.nct_id asc;
	"""

	return query


def query_aact(query):
	connection=False
	try:
	  # Connect to an existing database
	  connection = psycopg2.connect(user=getpass.getpass('What is your AACT username?'),
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
  

if __name__ == "__main__":
	print(f"Running {__file__} file directly...")
	query=get_default_query()
	df=query_aact(query)
	print(df.head())

