import aact_querier as aq
import requests
from bs4 import BeautifulSoup
import json
import os
from collections import OrderedDict
import re



def append_record(a_dict):
  try:
    with open('extracted_data/trial_docs.json') as f:
      data = json.load(f)
    data.update(a_dict)
    
    with open('extracted_data/trial_docs.json', 'w') as f:
      json.dump(data, f)
  except:
    with open('extracted_data/trial_docs.json', 'w') as f:
      json.dump(a_dict, f)


def get_last_nct():
  try:
    with open('extracted_data/trial_docs.json') as f:
      data = json.load(f, object_pairs_hook=OrderedDict)
    return next(reversed(data))

  except:
    return None


def scrape_docs(nct_list):
  url_base= 'https://clinicaltrials.gov/ct2/show/'
  nct=''

  # Create object page
  doc_dict={}
  start=False

  # for nct in nct_list[:10]:
  for nct in nct_list:

    url=url_base+nct

    if (get_last_nct()==nct) or (get_last_nct() is None):
      print("Started! NCT", nct)
      start=True

    if start:

      try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml') #Fails on this STEP!

        docs = soup.find_all("a", {"class": "tr-study-link"})
        doc_dict={}

        nct_dict={}
        
        for d in docs:
          if bool(re.search('.*/prot.*pdf$', d['href'], re.IGNORECASE)):
            nct_dict['PROT']='https://clinicaltrials.gov'+d['href']

          if bool(re.search('.*/sap.*pdf$', d['href'], re.IGNORECASE)):
            nct_dict['SAP']='https://clinicaltrials.gov'+d['href']

          if bool(re.search('.*/icf.*pdf$', d['href'], re.IGNORECASE)):
            nct_dict['ICF']='https://clinicaltrials.gov'+d['href']
            
        doc_dict[nct]=nct_dict
        append_record(doc_dict)
      except:
        print("error: ",url)


if __name__ == "__main__":
	print(f"Running {__file__} file directly...")
	query=aq.get_default_query()
	df=aq.query_aact(query)
	nct_list=df.nct_id.tolist()
	scrape_docs(nct_list)
