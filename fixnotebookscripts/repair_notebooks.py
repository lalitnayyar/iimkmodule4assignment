import json
import nbformat
from pathlib import Path
import sys

def repair_notebook(notebook_path):
    """Repair corrupted Jupyter notebooks."""
    try:
        # First try to read the notebook normally
        with open(notebook_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Try to parse as JSON first
        try:
            notebook_dict = json.loads(content)
        except json.JSONDecodeError:
            print(f"JSON decode error in {notebook_path}. Attempting to fix...")
            # Remove any invalid characters and try again
            content = ''.join(char for char in content if ord(char) >= 32 or char in '\n\r\t')
            notebook_dict = json.loads(content)
        
        # Convert to notebook format
        notebook = nbformat.from_dict(notebook_dict)
        
        # Ensure notebook format version is correct
        if notebook.nbformat < 4:
            print(f"Converting notebook format from version {notebook.nbformat} to 4")
            notebook = nbformat.convert(notebook, 4)
        
        # Fix metadata
        if 'kernelspec' not in notebook.metadata:
            notebook.metadata['kernelspec'] = {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            }
        
        # Fix cells
        valid_cells = []
        for cell in notebook.cells:
            try:
                # Ensure cell has required fields
                if 'cell_type' not in cell:
                    continue
                
                # Fix missing metadata
                if 'metadata' not in cell:
                    cell['metadata'] = {}
                
                # Fix missing source
                if 'source' not in cell:
                    cell['source'] = ''
                
                # Fix missing outputs for code cells
                if cell['cell_type'] == 'code' and 'outputs' not in cell:
                    cell['outputs'] = []
                
                # Fix execution count
                if cell['cell_type'] == 'code' and 'execution_count' not in cell:
                    cell['execution_count'] = None
                
                valid_cells.append(cell)
            except Exception as e:
                print(f"Skipping invalid cell: {str(e)}")
        
        notebook.cells = valid_cells
        
        # Add essential imports if needed
        essential_imports = [
            "import pandas as pd",
            "import numpy as np",
            "import matplotlib.pyplot as plt",
            "import seaborn as sns",
            "from sklearn.model_selection import train_test_split",
            "from sklearn.preprocessing import StandardScaler",
            "from sklearn.ensemble import RandomForestRegressor",
            "import warnings",
            "warnings.filterwarnings('ignore')",
            "%matplotlib inline"
        ]
        
        if len(notebook.cells) == 0 or notebook.cells[0].cell_type != 'code':
            notebook.cells.insert(0, nbformat.v4.new_code_cell('\n'.join(essential_imports)))
        
        # Create backup of original file
        backup_path = notebook_path.parent / f"{notebook_path.stem}_backup{notebook_path.suffix}"
        import shutil
        shutil.copy2(notebook_path, backup_path)
        
        # Save repaired notebook
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(notebook, f)
        
        print(f"Successfully repaired {notebook_path}")
        print(f"Backup saved as {backup_path}")
        return True
        
    except Exception as e:
        print(f"Error repairing {notebook_path}: {str(e)}")
        return False

def main():
    """Repair all notebooks in the project."""
    notebook_paths = [
        "LalitNayyarIIMKMod4_analysis.ipynb",
        "LalitNayyarIIMKMod4_descriptive_analysis.ipynb",
        "LalitNayyarIIMKMod4_behavior_diagnostic_analysis_final.ipynb",
        "LalitNayyarIIMKMod4_predictive_analysis.ipynb"
    ]
    
    success_count = 0
    for nb_path in notebook_paths:
        path = Path(nb_path)
        if path.exists():
            if repair_notebook(path):
                success_count += 1
        else:
            print(f"Notebook not found: {nb_path}")
    
    print(f"\nRepair complete. Successfully repaired {success_count} out of {len(notebook_paths)} notebooks.")

if __name__ == "__main__":
    main()
