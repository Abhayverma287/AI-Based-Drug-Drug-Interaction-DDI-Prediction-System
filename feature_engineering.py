from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

def smiles_to_fp(smiles):
    
    mol = Chem.MolFromSmiles(smiles)
    
    if mol is None:
        return np.zeros(2048)
    
    fp = AllChem.GetMorganFingerprintAsBitVect(mol,2,nBits=2048)
    
    return np.array(fp)