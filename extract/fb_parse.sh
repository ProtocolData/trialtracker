#!/usr/bin/env bash

# Activate Go env
# Note: run this file through 'source fb_parse.sh'


# TODO: update this to work more generically
base="/Users/forrest.xiao/non_fh_code/trialtracker/extract/src/github.com/facebookresearch/Clinical-Trial-Parser/"

# set -eu

NER_MODEL="${base}"bin/ner.c2

CLINICAL_TRIAL_FILE="${base}"data/input/clinical_trials.csv
EXTRACTED_FILE="${base}"data/output/ie_extracted_clinical_trials.tsv
NER_FILE="${base}"data/output/ie_ner_clinical_trials.tsv
PARSED_FILE="${base}"data/output/ie_parsed_clinical_trials.tsv

EXTRACT_CMD="${base}"src/cmd/extract/main.go
NER_CMD="${base}"src/ie/ner.py
NEL_CMD="${base}"src/cmd/nel/main.go
NEL_CONFIG="${base}"src/resources/config/nel.conf


# /Users/forrest.xiao/non_fh_code/trialtracker/extract/src/github.com/facebookresearch/Clinical-Trial-Parser/data/output/ie_extracted_clinical_trials.tsv
# echo $EXTRACT_CMD

# Criteria extraction

conda activate trialtrackerenv_golang
echo "Extract inclusion and exclusion criteria..."
if ! go run "$EXTRACT_CMD" -i "$CLINICAL_TRIAL_FILE" -o "$EXTRACTED_FILE" -logtostderr
then
  echo "Criteria extraction failed."
  exit 1
fi


# Named entity recogntion
conda activate trialtrackerenv_py36

export PYTHONPATH="${base}"/src
if ! python "$NER_CMD" -m "$NER_MODEL" -i "$EXTRACTED_FILE" -o "$NER_FILE"
then
  echo "NER failed."
  exit 1
fi

# Named entity linking
conda activate trialtrackerenv_golang
echo "Run NEL to map NER terms to MESH concepts..."
if ! go run "$NEL_CMD" -conf "$NEL_CONFIG" -i "$NER_FILE" -o "$PARSED_FILE" -logtostderr
then
  rm -f "$PARSED_FILE"
  echo "NEL failed."
  exit 1
fi

rm "$EXTRACTED_FILE"
rm "$NER_FILE"



