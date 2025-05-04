import nbformat

def update_notebook():
    # Read the existing notebook
    with open('LalitNayyarIIMKMod4_descriptive_analysis_1.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Update the imports and style settings
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            if 'plt.style.use' in cell['source']:
                # Replace the problematic style settings with correct ones
                cell['source'] = '''# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set visualization style
plt.style.use('default')  # Use default matplotlib style
sns.set_theme(style="whitegrid")  # Set seaborn style
sns.set_palette('husl')  # Set color palette

# Increase font size for better readability
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

# Display settings for pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)'''
                break
    
    # Save the updated notebook
    with open('LalitNayyarIIMKMod4_descriptive_analysis_1.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    update_notebook()
