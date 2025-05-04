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
    
    # Find and replace the imports cell
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code' and 'import pandas as pd' in cell['source']:
            nb['cells'][i] = imports_cell
            break
    
    # Save the updated notebook
    with open('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_final.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    update_notebook()
