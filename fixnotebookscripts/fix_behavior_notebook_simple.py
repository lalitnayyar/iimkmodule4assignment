import nbformat

def update_notebook():
    # Read the existing notebook
    with open('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_final.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Update the imports cell
    imports_cell = nbformat.v4.new_code_cell('''# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from datetime import datetime
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Set visualization style
plt.style.use('default')
sns.set_theme(style="whitegrid")
sns.set_palette('husl')

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline''')

    # Update the data loading cell
    data_cell = nbformat.v4.new_code_cell('''# Load and prepare the data
df = pd.read_excel('Online Retail.xlsx')
print("Original data shape:", df.shape)

def clean_data(df):
    """Clean the retail dataset"""
    df_clean = df.copy()
    df_clean = df_clean.dropna()
    df_clean = df_clean[~df_clean['InvoiceNo'].astype(str).str.contains('C')]
    df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)]
    df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])
    df_clean['TotalAmount'] = df_clean['Quantity'] * df_clean['UnitPrice']
    return df_clean.reset_index(drop=True)

df_clean = clean_data(df)
print("\\nCleaned data shape:", df_clean.shape)
print("\\nSample of cleaned data:")
display(df_clean.head())''')

    # Find and replace cells
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            if 'import pandas as pd' in cell['source']:
                nb['cells'][i] = imports_cell
            elif 'df = pd.read_excel' in cell['source']:
                nb['cells'][i] = data_cell

    # Save the updated notebook
    with open('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_final.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    update_notebook()
