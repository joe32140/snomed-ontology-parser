# SNOMED Ontology Parser

A Python tool for extracting medical concepts from text and mapping them to the SNOMED-CT ontology hierarchy.

## Overview

This repository provides functionality to:
- Extract medical concepts from text documents
- Map extracted concepts to SNOMED-CT ontology
- Analyze concept distributions across different hierarchical levels
- Visualize concept relationships and distributions

## Prerequisites

### 1. Required Python Packages

Install the following packages with their specific versions:
- [scispacy](https://github.com/allenai/scispacy) (v0.5.1)
- [medspacy](https://github.com/medspacy/medspacy) (v0.2.0.0)
- [Owlready2](https://owlready2.readthedocs.io/en/latest/pymedtermino2.html) (v0.37) - Required for pymedtermino2

### 2. UMLS and SNOMED-CT Access

1. Apply for UMLS access at the [UMLS website](https://www.nlm.nih.gov/research/umls/)
2. Download the required UMLS and SNOMED-CT files
3. Follow the setup instructions in the [pymedtermino2 documentation](https://owlready2.readthedocs.io/en/latest/pymedtermino2.html)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/snomed-ontology-parser.git
cd snomed-ontology-parser
```

2. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate snomed-parser
```

## Usage

### Running the Analysis

1. Place your UMLS data files in the `./data` directory
2. Run the Jupyter notebook:
```bash
jupyter notebook concept_distribution.ipynb
```

Note: If you encounter a locked `pym.sqlite` file error, use the provided script:
```bash
bash remove_sql_lock.sh
```

### Finding Concept IDs

To look up specific concept IDs, you can use the [SNOMED CT Browser](https://bioportal.bioontology.org/ontologies/SNOMEDCT?p=classes)
(Note: The browser may use an older version of the SNOMED ontology)

## Example

Input text:
```
Alterations in the hypocretin receptor 2 and preprohypocretin genes produce narcolepsy in some animals.
```

Output visualization:
![Concept Mapping Example](https://i.imgur.com/Cr9aYBH.png)

## Project Structure

```
snomed-ontology-parser/
├── src/
│   ├── main.py              # Main application entry point
│   ├── concept_extractor.py # Extracts medical concepts from text
│   ├── concept_analyzer.py  # Analyzes concept distributions
│   └── data_loader.py       # Handles UMLS data loading
├── data/                    # Directory for UMLS data files
├── concept_distribution.ipynb
├── environment.yml
└── remove_sql_lock.sh
```
