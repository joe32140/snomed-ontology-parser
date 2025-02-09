from data_loader import UMLSLoader
from concept_extractor import ConceptExtractor
from concept_analyzer import get_children_concept_distribution

def main():
    # Initialize and load UMLS data
    loader = UMLSLoader(data_dir="./data")
    loader.load_or_create_database()
    PYM, SNOMEDCT_US, CUI = loader.get_ontologies()
    
    # Initialize concept extractor
    extractor = ConceptExtractor()
    
    # Example usage
    text = "Alterations in the hypocretin receptor 2 and preprohypocretin genes produce narcolepsy in some animals."
    concepts = extractor.get_snomed_concepts(text, visualization=True)
    
    # Get concept distribution
    snomed_concept_list = [[c.name, c.label.first()] for c in concepts]
    
    # Analyze root concept distribution
    root_distribution = get_children_concept_distribution(
        concepts, 
        "138875005",  # SNOMED-CT root concept
        visualization=True
    )
    
    # Analyze next level distributions
    child_distributions = {}
    for child in SNOMEDCT_US["138875005"].children:
        child_distributions[child.label.first()] = get_children_concept_distribution(
            concepts, 
            child.name
        )
        
    return {
        "concepts": snomed_concept_list,
        "root_distribution": root_distribution,
        "child_distributions": child_distributions
    }

if __name__ == "__main__":
    results = main() 