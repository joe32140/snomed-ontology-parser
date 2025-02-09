import spacy
from medspacy.context import ConTextComponent
from medspacy.visualization import visualize_ent
from scispacy.linking import EntityLinker

class ConceptExtractor:
    def __init__(self):
        """Initialize spaCy pipeline with required components."""
        self.nlp = spacy.load("en_core_sci_sm")
        self.nlp.add_pipe("scispacy_linker", 
                         config={"resolve_abbreviations": True, 
                                "linker_name": "umls"})
        self.nlp.add_pipe("medspacy_context")
        
    def get_snomed_concepts(self, text, visualization=False, remove_negated_entity=True):
        """Extract SNOMED concepts from text.
        
        Args:
            text (str): Input text to extract concepts from
            visualization (bool): Whether to visualize entities
            remove_negated_entity (bool): Whether to remove negated entities
            
        Returns:
            Concepts: Collection of SNOMED concepts
        """
        doc = self.nlp(text)
        if visualization:
            visualize_ent(doc)
            
        umls_concepts = Concepts()
        
        for entity in doc.ents:
            if remove_negated_entity and entity._.is_negated:
                continue
                
            for umls_ent in entity._.kb_ents:
                if CUI[umls_ent[0]] and CUI[umls_ent[0]].name:
                    umls_concepts.add(CUI[umls_ent[0]])
                    break
                    
        snomed_concepts = umls_concepts >> SNOMEDCT_US
        return snomed_concepts 