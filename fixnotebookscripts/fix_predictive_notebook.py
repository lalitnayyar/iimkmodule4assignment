import json
import nbformat
from pathlib import Path

def fix_predictive_notebook(notebook_path):
    """Fix specific issues in the predictive analysis notebook."""
    try:
        # Read the notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
        
        # Create backup
        backup_path = Path(notebook_path).parent / f"{Path(notebook_path).stem}_backup.ipynb"
        with open(backup_path, 'w', encoding='utf-8') as f:
            nbformat.write(notebook, f)
        
        # Fix kernel spec
        notebook.metadata['kernelspec'] = {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
        
        # Essential imports for predictive analysis
        essential_imports = [
            "import pandas as pd",
            "import numpy as np",
            "import matplotlib.pyplot as plt",
            "import seaborn as sns",
            "from sklearn.model_selection import train_test_split",
            "from sklearn.preprocessing import StandardScaler",
            "from sklearn.ensemble import RandomForestRegressor",
            "from sklearn.metrics import mean_squared_error, r2_score",
            "import warnings",
            "warnings.filterwarnings('ignore')",
            "%matplotlib inline",
            "plt.style.use('seaborn')"
        ]
        
        # Add or update imports
        if len(notebook.cells) > 0 and notebook.cells[0].cell_type == 'code':
            current_imports = notebook.cells[0].source.split('\n')
            for imp in essential_imports:
                if imp not in current_imports:
                    current_imports.append(imp)
            notebook.cells[0].source = '\n'.join(current_imports)
        else:
            notebook.cells.insert(0, nbformat.v4.new_code_cell('\n'.join(essential_imports)))
        
        # Add data loading with error handling
        data_loading_cell = """# Load the cleaned data
try:
    df = pd.read_csv('cleaned_retail_data.csv')
    print("Data loaded successfully!")
    print(f"Shape of the dataset: {df.shape}")
except FileNotFoundError:
    print("Error: cleaned_retail_data.csv not found!")
    print("Please run the analysis notebook first to generate the cleaned dataset.")
except Exception as e:
    print(f"Error loading data: {e}")"""
        
        # Check if data loading cell exists, if not add it
        data_loading_exists = False
        for cell in notebook.cells:
            if 'read_csv' in cell.source:
                data_loading_exists = True
                cell.source = data_loading_cell
                break
        
        if not data_loading_exists:
            notebook.cells.insert(1, nbformat.v4.new_code_cell(data_loading_cell))
        
        # Add feature engineering functions
        feature_engineering_cell = """def create_customer_features(df):
    '''Create customer-level features for prediction'''
    customer_features = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (x.max() - x.min()).days,  # Customer tenure
        'InvoiceNo': 'count',  # Number of purchases
        'TotalAmount': ['sum', 'mean', 'std'],  # Purchase statistics
        'Quantity': ['sum', 'mean', 'std']  # Quantity statistics
    })
    
    # Flatten column names
    customer_features.columns = ['Tenure', 'PurchaseCount', 
                               'TotalRevenue', 'AvgPurchaseValue', 'StdPurchaseValue',
                               'TotalQuantity', 'AvgQuantity', 'StdQuantity']
    
    return customer_features

def prepare_features_and_target(customer_features):
    '''Prepare features and target for modeling'''
    # Use TotalRevenue as target variable
    X = customer_features.drop('TotalRevenue', axis=1)
    y = customer_features['TotalRevenue']
    
    # Handle missing values
    X = X.fillna(0)
    
    return X, y"""
        
        # Add feature engineering cell if not exists
        if not any('create_customer_features' in cell.source for cell in notebook.cells):
            notebook.cells.append(nbformat.v4.new_code_cell(feature_engineering_cell))
        
        # Save the fixed notebook
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(notebook, f)
        
        print(f"Successfully fixed {notebook_path}")
        print(f"Backup saved as {backup_path}")
        return True
        
    except Exception as e:
        print(f"Error fixing notebook: {str(e)}")
        return False

if __name__ == "__main__":
    notebook_path = "LalitNayyarIIMKMod4_predictive_analysis_1.ipynb"
    fix_predictive_notebook(notebook_path)
