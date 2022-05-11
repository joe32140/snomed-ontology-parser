# snomed-ontology-parser
The goal of this repository is to map medical text contents to a specific level of hierachy in the snomed ontology.

# Packages
Please follow intallation instructions in the following link:

[scispacy](https://github.com/allenai/scispacy)  
[medspacy](https://github.com/medspacy/medspacy)  
[pymedtermino2](https://owlready2.readthedocs.io/en/latest/pymedtermino2.html)

## Download UMLS and Snomed CT Files from the [UMLS website](https://www.nlm.nih.gov/research/umls/).
You need to apply for permission to download the files.
Follows this https://owlready2.readthedocs.io/en/latest/pymedtermino2.html.

## Run Notebook
Please run `concept_distribution.ipynb` to find relations between parent concepts and child concepts.


To find concept id from the interactive interface. 
See https://bioportal.bioontology.org/ontologies/SNOMED_CF/?p=classes&conceptid=root. Note that this interface uses old version of the snomed ontology.
