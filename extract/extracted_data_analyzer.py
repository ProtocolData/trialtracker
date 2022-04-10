import json
from collections import OrderedDict



def read_doc_links():
  data=OrderedDict()

  try:
    with open('extracted_data/trial_docs.json') as f:
      data = json.load(f, object_pairs_hook=OrderedDict)

  except:
    print("Error reading json!")

  return data

def main():
  trial_docs=read_doc_links()
  print(len(trial_docs)," items read.")


if __name__ == "__main__":
  main()