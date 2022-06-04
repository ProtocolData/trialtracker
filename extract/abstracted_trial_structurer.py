import pandas as pd
import numpy as np
import argparse


def clean_data(df):
  df.rename(columns={'ClinicalTrials.gov Identifier': 'nct','Survey Timestamp':'timestamp','Coder Name':'coder'}, inplace=True)
  

  # EntryID 159: NCT ID cleaned from https://ClinicalTrials.gov/show/NCT04577833 to NCT04577833
  df.loc[159,'nct']='NCT04577833'

  # EntryID 639: NCT ID and trial names switched
  df.loc[639,'nct']='NCT03702309'  
  df.loc[639,'Please copy/paste the name of the trial here:']='Liquid Biopsy Evaluation and Repository Development at Princess Margaret (LIBERATE)'

  # EntryID 654: NCT ID cleaned from ClinicalTrials.gov Identifier: NCT03564197 to NCT03564197
  df.loc[654,'nct']='NCT03564197'


  nct_based_removal=[166,376,482]
  # Not completed
  df.drop(nct_based_removal, axis='index', inplace=True)

  # Print summary stats
  print("Unique Trials Abstracted: ", df.nct.nunique())
  print("   Number of Singly-, Doubly-, and Triply- abstracted trials: ")
  print(df.groupby(['nct']).agg({'coder':'count'}).reset_index().coder.value_counts().rename_axis('abstractors').reset_index(name='trials'))

  #TODO: Doesn't seem that helpful to separate this as a one-use function.  Also look into best practices for passing/returning mutable objects.




def parse_args():
    parser=argparse.ArgumentParser(description="Process abstracted data from wide to long format.")
    
    parser.add_argument("-p", "--path", type=argparse.FileType('r', encoding='UTF-8'), 
                      required=True, dest="filename",
                    help="Requires path to abstracted data.  Please enter file path without enclosing in quotes.")


    args=parser.parse_args()
    
    return args

if __name__ == "__main__":
  print(f"Running {__file__} file directly...")

  args=parse_args()
  
  path = args.filename
  df = pd.read_csv(path, index_col=0)
  clean_data(df)


  # Add length field
  df['nct_len']=df.nct.str.len()

  # Get doubly abstracted data
  df_agg=df.groupby(['nct']).agg({'coder':'count'}).reset_index()
  double_abs_ncts=df_agg[df_agg.coder==2].nct.to_list()
  double_df=df[df.nct.isin(double_abs_ncts)].sort_values(by='nct')
  
  # Wide to long
  double_df_long=double_df.melt(id_vars=['timestamp','coder','nct'])


  # Get every other row
  a = np.arange(len(double_df_long))
  df1 = double_df_long[(a % 2 == 1)]

  # Get alternate rows
  df2 = double_df_long[((a+1) % 2 == 1) ]

  dff=df1.merge(df2, on=['nct','variable'])

  # Measure agreement
  dff['agreement']= dff['value_x'].fillna('-').eq(dff['value_y'].fillna('-'))
  dff.agreement=dff.agreement.astype(int)

  dff['same_coder']= dff.coder_x==dff.coder_y
  dff['same_coder']=dff['same_coder'].astype(int)

  
  # Remove double-reviewed by the same coder.  Note this could be interesting to see if they agree with themselves.
  dff_clean=dff[dff.same_coder==0]
  dff_clean.nct.nunique()

  dff_clean['var_group']=dff_clean['variable'].apply(lambda x: x.split(" (choice=")[0])

  dff_clean.to_csv("~/Downloads/doubly_abstracted_concordance_clean.csv")


  # query=get_default_query()
  # df=query_aact(query)
  # print(df.head())



