import pandas as pd
import os
import sys
import aact_querier as aq


def prep_incremental_extraction(filepath='extracted_data/ct_fb_parser_data.csv', nct_col='#nct_id')
	# Read a csv that contains NCT IDs.  Search 

	path = os.path.abspath(os.path.dirname('.'))

	# Read previously extracted eligibility criteria
	main_filepath='extracted_data/ie_parsed_clinical_trials.tsv'
	ie_path = os.path.join(path, main_filepath)
	ie=pd.read_csv(ie_path, sep='\t')


	# Save previously extracted eligibility criteria to new file
	ie_path_prev = os.path.join(path, "src/github.com/facebookresearch/Clinical-Trial-Parser/data/output/ie_parsed_clinical_trials_prev.tsv")
	ie.to_csv(ie_path_prev, index=False)

	# Get list of NCT IDs for previously extracted eligibility criteria
	prev_ncts=list(set(ie['#nct_id'].tolist()))

	# Read current list of NCT IDs for trials of interest
	df=pd.read_csv(filepath, index_col=0)
	cur_ncts=list(set(df[nct_col].tolist()))

	# Find only the trials that have not already had eligibility criteria extracted
	diff_ncts=list(set(cur_ncts) - set(prev_ncts))


	# Run query to pull eligiblity criteria data from clinicaltrials.gov to use for eligibility criteria extraction
	terms=aq.get_term_str()
	add_ncts=aq.query_aact(aq.get_default_query(terms, fb_parser_format=True, nct_list=diff_ncts))
	fb_parser_output=add_ncts[['#nct_id','title','has_us_facility','conditions','eligibility_criteria']]

	# Save file as input for fb clinical trial parser
	out_path = os.path.join(path, "src/github.com/facebookresearch/Clinical-Trial-Parser/data/input/clinical_trials.csv")
	fb_parser_output.to_csv(out_path, index=False, index=False)


def combine_extractions():
	# Read newly extracted eligibility criteria
	path = os.path.abspath(os.path.dirname('.'))
	ie_path = os.path.join(path, "src/github.com/facebookresearch/Clinical-Trial-Parser/data/output/ie_parsed_clinical_trials.tsv")
	ie=pd.read_csv(ie_path, sep='\t')


	# Read previously parsed data
	main_filepath='extracted_data/ie_parsed_clinical_trials.tsv'
	main_parsed_path = os.path.join(path, main_filepath)
	main=pd.read_csv(main_parsed_path, sep='\t')
	
	# Print stats
	print(f"Original extraction included {main['#nct_id'].nunique()} trials.")
	print(f"New extraction includes {ie['#nct_id'].nunique()} trials.")

	new_ncts=list(set(ie['#nct_id'].tolist()))
	main_ncts=list(set(main['#nct_id'].tolist()))

	# Find overlapping trials that have been extracted already
	diff_ncts=list(set(new_ncts) - set(main_ncts))

	print(f"There are {len(diff_ncts)} overlapping trials.")


	# Combine data and drop duplicates
	combined_df=pd.concat([main, ie]).drop_duplicates().reset_index(drop=True)
	combined_df.to_csv(main_parsed_path, sep="\t")





if __name__ == "__main__":
	print(f"Running {__file__} file directly...")

	

