import aact_querier as aq
import os

def fb_parser_query():
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
	(c.downcase_name like '%cancer%'
	or c.downcase_name like '%neoplasm%'
	or c.downcase_name like '%tumor%'
	or c.downcase_name like '%malignancy%'
	or c.downcase_name like '%oncology%'
	or c.downcase_name like '%neoplasia%'
	or c.downcase_name like '%neoplastic%'
	or c.downcase_name like '%carcinoma%'
	or c.downcase_name like '%lymphoma%'
	or c.downcase_name like '%metastatic%%'
	or c.downcase_name like '%metastasis%'
	or c.downcase_name like '%metastases%'
	or c.downcase_name like '%leukemia%'
	or c.downcase_name like '%leukaemia%'
	or c.downcase_name like '%myeloma%'
	or c.downcase_name like '%mesothelioma%'
	or c.downcase_name like '%malignan%'
	or c.downcase_name like '%hnscc%'
	or c.downcase_name like '%melanoma%'
	or c.downcase_name like '%polycythemia vera%'
	or c.downcase_name like '%blastoma%'
	or c.downcase_name like '%sarcoma%'
	or c.downcase_name like '%nsclc%'
	or (downcase_name like '%gist%' and downcase_name not like '%regist%' and downcase_name not like '%logist%')
	or c.downcase_name like '%crpc%'
	or c.downcase_name like '%myelodysplastic syndrome%'
	or c.downcase_name like '%mds%'
	or c.downcase_name like '%cytoma%'
	or c.downcase_name like '%waldenstrom macroglobulinemia%'
	or c.downcase_name like '%myelofibrosis%'
	or c.downcase_name like '%hodgkin%'
	or c.downcase_name like '%cml%'
	or c.downcase_name like '%aml%'
	or c.downcase_name like '%glioma%'
	or c.downcase_name like '%ependymoma%'
	or c.downcase_name like '%seminoma%'
	or c.downcase_name like '%chordoma%'
	or c.downcase_name like '%pseudomyxoma peritonei%'
	or c.downcase_name like '%fibroxanthoma%'
	)

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
	)

	select 
	t.nct_id AS \"#nct_id\",
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

def main():
	my_path = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(my_path, "extracted_data/ct_fb_parser_data.csv")
	print(path)
	
	try:
		df=aq.query_aact(fb_parser_query())
		df.to_csv(path)

	except:
	  print("Data download failed.  Please check credentials and query and try again.")

if __name__ == "__main__":
	main()