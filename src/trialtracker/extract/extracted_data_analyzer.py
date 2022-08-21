import json
from collections import OrderedDict
import os


#TODO: This path thing is probably not ideal
def read_doc_links(path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "extracted_data/trial_docs.json")): 
  data=OrderedDict()

  try:
    with open(path) as f:
      data = json.load(f, object_pairs_hook=OrderedDict)

  except:
    print("Error reading json!")

  return data

def main():
  trial_docs=read_doc_links(path)
  print(len(trial_docs)," items read.")


if __name__ == "__main__":
  main()