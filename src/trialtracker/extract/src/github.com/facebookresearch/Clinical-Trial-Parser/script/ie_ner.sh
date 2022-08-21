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


echo "Run NER on extracted criteria..."
export PYTHONPATH="$(pwd)/src"
if ! python "$NER_CMD" -m "$NER_MODEL" -i "$EXTRACTED_FILE" -o "$NER_FILE"
then
  echo "NER failed."
  exit 1
fi

# Errors
# [W init.h:137] Caffe2 GlobalInit should be run before any other API calls.
# https://stackoverflow.com/questions/64973075/issue-when-converting-onnx-model-to-caffe2