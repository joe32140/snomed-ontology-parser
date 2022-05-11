# snomed-ontology-parser
The goal of this repository is to map medical text contents to a specific level of hierachy in the snomed ontology.

# Packages
spacy
scispacy
medspacy
pymedtermino2

## Download UMLS and Snomed CT Files from the [UMLS website](https://www.nlm.nih.gov/research/umls/).
You can download ontology files at https://bioportal.bioontology.org/ontologies/SNOMEDCT.
For example, we use Clinical Findings in this repository. 
Please find the download link of CSV formant in https://bioportal.bioontology.org/ontologies/SNOMED_CF.

## Run Notebook
Please run `concept_distribution.ipynb` to find relations between parent concepts and child concepts.
To find concept id from the interactive interface. See https://bioportal.bioontology.org/ontologies/SNOMED_CF/?p=classes&conceptid=root. Note that this interface uses old version of the snomed ontology.
