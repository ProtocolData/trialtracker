
try:
    from extract import aact_querier as aq
except (ModuleNotFoundError, ImportError):
    import aact_querier as aq
#TODO: Can't be right, need to fix: https://stackoverflow.com/questions/44315077/import-error-running-unittest-in-python3

import requests
from bs4 import BeautifulSoup
import json
import os
from collections import OrderedDict
import re
import argparse



def append_record(a_dict, path):  
  try:
    with open(path) as f:
      data = json.load(f)
    data.update(a_dict)
    
    with open(path, 'w') as f:
      json.dump(data, f)

  except Exception as e:
    with open(path, 'w') as f:
      json.dump(a_dict, f)

      


def get_last_nct(path):
  try:
    with open(path) as f:
      data = json.load(f, object_pairs_hook=OrderedDict)
    return next(reversed(data))

  except Exception as e:
    # print(e)
    print(f"Tried initializing based on previous file, but no {path} file created yet.")
    return None


def scrape_docs(nct_list, path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "extracted_data/trial_docs.json")):
  url_base= 'https://clinicaltrials.gov/ct2/show/'
  nct=''

  scraped_doc_counter=0
  last_nct=get_last_nct(path)

  # Create object page
  doc_dict={}
  start=False

  # for nct in nct_list[:10]:
  for nct in nct_list:

    url=url_base+nct

    if (not start)&((last_nct==nct) or (last_nct is None)):
      # print("Started! ", nct)
      start=True

    if start:

      try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')

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
        append_record(doc_dict, path)
        scraped_doc_counter+=1

      except:
        print("error: ",url)

  return scraped_doc_counter


# Add argparse https://stackoverflow.com/questions/1009860/how-to-read-process-command-line-arguments
# Structure argparse https://www.reddit.com/r/learnpython/comments/3do2wr/where_to_put_argparse/
# Docs https://docs.python.org/3/library/argparse.html
# Tutorial https://docs.python.org/3/howto/argparse.html

def parse_args():
    parser=argparse.ArgumentParser(description="Scrape document links from clinicaltrials.gov")
    
    parser.add_argument("-t", "--testtrials", dest='test_trials', action="store_true", 
                    help="Use test nct trial ids to avoid long query times.  Stores test json in trial_docs_test.json")

    parser.add_argument("-f", "--funfact", dest='fun_fact', action="store_true",
                    help="Returns a fun fact.  There is only one static fun fact.")

    args=parser.parse_args()
    
    if args.test_trials:
      print("Test query used")
    
    if args.fun_fact:
      print("Contagious cancers are known to be transmitted between animals like dogs and Tasmanian Devils, and in rare cases, between mother and fetus: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3228048/")

    return args

def main():
  print(f"Running {__file__} file directly...")
  args=parse_args()
  
  nct_list=[]
  my_path = os.path.abspath(os.path.dirname(__file__))
  path = os.path.join(my_path, "extracted_data/trial_docs.json")

  if args.test_trials:
    nct_list=['NCT03386513','NCT03520959','NCT03490747']
    path = os.path.join(my_path, "extracted_data/trial_docs_test.json")

  else:
    query=aq.get_default_query()
    df=aq.query_aact(query)
    nct_list=df.nct_id.tolist()

  trials_scraped=scrape_docs(nct_list, path)
  print(f"{trials_scraped} trial docs scraped to {path}.")


if __name__ == "__main__":
  main()
