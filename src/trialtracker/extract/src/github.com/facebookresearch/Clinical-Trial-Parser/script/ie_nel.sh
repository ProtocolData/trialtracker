#!/usr/bin/env bash
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
#
# Parse clinical-trial eligibility criteria with IE.
#
# ./script/ie_parse.sh

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


echo "Run NEL to map NER terms to MESH concepts..."
if ! go run "$NEL_CMD" -conf "$NEL_CONFIG" -i "$NER_FILE" -o "$PARSED_FILE" -logtostderr
then
  rm -f "$PARSED_FILE"
  echo "NEL failed."
  exit 1
fi

rm "$EXTRACTED_FILE"
rm "$NER_FILE"