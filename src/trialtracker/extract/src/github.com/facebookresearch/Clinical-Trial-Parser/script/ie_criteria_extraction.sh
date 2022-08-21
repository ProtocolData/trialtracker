#!/usr/bin/env bash
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
#
# Parse clinical-trial eligibility criteria with IE.
#
# ./script/ie_parse.sh


# on setting gopath https://stackoverflow.com/questions/24306183/can-someone-explain-why-gopath-is-convenient-and-how-it-should-be-used-in-genera#:~:text=GOROOT%20points%20to%20your%20Go,different%20subfolder%20(by%20design).
# for conda https://github.com/conda-forge/go-feedstock/issues/2

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# export GOPATH = $HOME/non_fh_code/trialtracker/extract

# export GOPATH = $( dirname $(dirname $(dirname $(dirname $(dirname $DIR)))))



set -eu

NER_MODEL="bin/ner.c2"

CLINICAL_TRIAL_FILE="data/input/clinical_trials.csv"
EXTRACTED_FILE="data/output/ie_extracted_clinical_trials.tsv"
NER_FILE="data/output/ie_ner_clinical_trials.tsv"
PARSED_FILE="data/output/ie_parsed_clinical_trials.tsv"

EXTRACT_CMD="src/cmd/extract/main.go"
NER_CMD="src/ie/ner.py"
NEL_CMD="src/cmd/nel/main.go"
NEL_CONFIG="src/resources/config/nel.conf"

rm -f "$PARSED_FILE"

echo "Extract inclusion and exclusion criteria..."
if ! go run "$EXTRACT_CMD" -i "$CLINICAL_TRIAL_FILE" -o "$EXTRACTED_FILE" -logtostderr
then
  echo "Criteria extraction failed."
  exit 1
fi