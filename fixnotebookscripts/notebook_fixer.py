import json
import nbformat
from pathlib import Path

def fix_notebook(notebook_path):
    """Fix common issues in Jupyter notebooks."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Add kernel specification if missing
    if 'kernelspec' not in notebook.metadata:
        notebook.metadata['kernelspec'] = {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    
    # Add essential imports to first code cell
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
    
    # Check if first cell exists and is code
    if len(notebook.cells) > 0 and notebook.cells[0].cell_type == 'code':
        current_imports = notebook.cells[0].source.split('\n')
        # Add missing imports
        for imp in essential_imports:
            if imp not in current_imports:
                current_imports.append(imp)
        notebook.cells[0].source = '\n'.join(current_imports)
    else:
        # Create new cell with imports
        new_cell = nbformat.v4.new_code_cell('\n'.join(essential_imports))
        notebook.cells.insert(0, new_cell)
    
    # Add error handling to data loading
    for cell in notebook.cells:
        if cell.cell_type == 'code' and 'read_excel' in cell.source:
            if 'try:' not in cell.source:
                cell.source = f"""try:
    {cell.source}
except FileNotFoundError:
    print("Error: 'Online Retail.xlsx' file not found. Please ensure it's in the correct directory.")
except Exception as e:
    print(f"Error loading data: {{e}}")"""
    
    # Save the modified notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)

def main():
    """Fix all notebooks in the project."""
    notebook_paths = [
        "LalitNayyarIIMKMod4_analysis.ipynb",
        "LalitNayyarIIMKMod4_descriptive_analysis.ipynb",
        "LalitNayyarIIMKMod4_behavior_diagnostic_analysis_final.ipynb",
        "LalitNayyarIIMKMod4_predictive_analysis.ipynb"
    ]
    
    for nb_path in notebook_paths:
        try:
            print(f"Fixing {nb_path}...")
            fix_notebook(nb_path)
            print(f"Successfully fixed {nb_path}")
        except Exception as e:
            print(f"Error fixing {nb_path}: {e}")

if __name__ == "__main__":
    main()
