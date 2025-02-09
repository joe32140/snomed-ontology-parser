import os
from owlready2 import *
from owlready2.pymedtermino2 import *
from owlready2.pymedtermino2.umls import *
from owlready2.pymedtermino2.model import Concepts
import subprocess

class UMLSLoader:
    def __init__(self, data_dir="./data"):
        """Initialize UMLS loader with data directory path.
        
        Args:
            data_dir (str): Path to directory containing UMLS data files
        """
        self.data_dir = data_dir
        self.pym_path = f"{data_dir}/pym.sqlite3"
        self.umls_path = f"{data_dir}/umls-2022AA-full.zip"
        
    def load_or_create_database(self):
        """Load existing UMLS database or create new one if it doesn't exist."""
        if not os.path.exists(self.pym_path):
            self._create_new_database()
        else:
            self._load_existing_database()
            
    def _create_new_database(self):
        """Create new UMLS database from zip file."""
        print(f"Creating new database at {self.pym_path}")
        default_world.set_backend(filename=self.pym_path)
        import_umls(self.umls_path, terminologies=["SNOMEDCT_US", "CUI"])
        default_world.save()
        
    def _load_existing_database(self):
        """Load existing UMLS database."""
        print(f"Loading existing database from {self.pym_path}")
        try:
            umls.default_world.set_backend(filename=self.pym_path)
        except:
            print("Database locked. Attempting to release lock...")
            subprocess.run(["bash", "scripts/remove_sql_lock.sh"])
            umls.default_world.set_backend(filename=self.pym_path)

    def get_ontologies(self):
        """Get SNOMED-CT and CUI ontologies.
        
        Returns:
            tuple: (PYM ontology, SNOMED-CT ontology, CUI ontology)
        """
        PYM = get_ontology("http://PYM/").load()
        SNOMEDCT_US = PYM["SNOMEDCT_US"]
        CUI = PYM["CUI"]
        return PYM, SNOMEDCT_US, CUI 