# snomed-ontology-parser
The goal of this repository is to find medical text concepts from a document and map them to a specific level of hierachy in the snomed ontology.

# Packages
Please follow intallation instructions in the following link:

[scispacy](https://github.com/allenai/scispacy) = 0.5.1  
[medspacy](https://github.com/medspacy/medspacy) = 0.2.0.0  
[pymedtermino2](https://owlready2.readthedocs.io/en/latest/pymedtermino2.html) => Owlready2 = 0.37  

## Download UMLS and Snomed CT Files from the [UMLS website](https://www.nlm.nih.gov/research/umls/).
You need to apply for permission to download the files.
Follows this https://owlready2.readthedocs.io/en/latest/pymedtermino2.html.

## Run Notebook
Please run `concept_distribution.ipynb` to find relations between parent concepts and child concepts.
Note that sometimes the processed `pym.sqlite` file will be locked. Current work around is to copy the file and replace the original file and run the notebook again as shown in `remove_sql_lock.sh`. 


To find concept id from the interactive interface. 
See https://bioportal.bioontology.org/ontologies/SNOMED_CF/?p=classes&conceptid=root. Note that this interface uses old version of the snomed ontology.

## Example
With the following text sentence: `Alterations in the hypocretin receptor 2 and preprohypocretin genes produce narcolepsy in some animals.` , this repo can find medical concepts from the sentence and map them to the snomed ontology.

![image](https://i.imgur.com/Cr9aYBH.png)
