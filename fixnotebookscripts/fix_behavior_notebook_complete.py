import nbformat

def update_notebook():
    # Read the existing notebook
    with open('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_fin.ipynb', 'r', encoding='utf-8') as f:
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

    # Update the data loading and cleaning cell
    data_cell = nbformat.v4.new_code_cell('''try:
    # Load the data
    print("Loading data...")
    df = pd.read_excel('Online Retail.xlsx')
    print("Original data shape:", df.shape)
    
    def clean_data(df):
        """Clean the retail dataset"""
        print("Cleaning data...")
        df_clean = df.copy()
        
        # Remove missing values
        df_clean = df_clean.dropna()
        print(f"After removing missing values: {len(df_clean)} records")
        
        # Remove cancelled orders
        df_clean = df_clean[~df_clean['InvoiceNo'].astype(str).str.contains('C')]
        print(f"After removing cancelled orders: {len(df_clean)} records")
        
        # Ensure positive quantities and prices
        df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)]
        print(f"After ensuring positive values: {len(df_clean)} records")
        
        # Convert InvoiceDate to datetime
        df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])
        
        # Calculate total amount
        df_clean['TotalAmount'] = df_clean['Quantity'] * df_clean['UnitPrice']
        
        return df_clean.reset_index(drop=True)
    
    # Clean the data
    df_clean = clean_data(df)
    
    print("\\nData cleaning complete!")
    print("Final data shape:", df_clean.shape)
    print("\\nSample of cleaned data:")
    display(df_clean.head())
    
    # Display basic statistics
    print("\\nBasic statistics of numerical columns:")
    display(df_clean.describe())
    
except FileNotFoundError:
    print("Error: 'Online Retail.xlsx' file not found. Please ensure it's in the correct directory.")
except Exception as e:
    print(f"Error during data preparation: {e}")''')

    # Update the product analysis cell
    product_cell = nbformat.v4.new_code_cell('''try:
    # Product Analysis
    print("Analyzing product sales patterns...")
    
    # Group by product
    product_analysis = df_clean.groupby('Description').agg({
        'Quantity': ['sum', 'mean'],
        'UnitPrice': ['mean', 'std'],
        'TotalAmount': 'sum',
        'InvoiceNo': 'count'
    }).round(2)
    
    # Flatten column names
    product_analysis.columns = ['total_quantity', 'avg_quantity', 'avg_price', 'price_std', 'total_revenue', 'transaction_count']
    
    # Sort by revenue
    top_products = product_analysis.sort_values('total_revenue', ascending=False).head(10)
    
    print("\\nTop 10 Products by Revenue:")
    display(top_products)
    
    # Visualize price-quantity relationship
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.scatter(product_analysis['avg_price'], product_analysis['total_quantity'], alpha=0.5)
    plt.xlabel('Average Price')
    plt.ylabel('Total Quantity Sold')
    plt.title('Price vs. Demand Relationship')
    
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df_clean, y='UnitPrice')
    plt.title('Price Distribution')
    
    plt.tight_layout()
    plt.show()
    
except Exception as e:
    print(f"Error in product analysis: {e}")''')

    # Find and replace cells
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            if 'import pandas as pd' in cell['source']:
                nb['cells'][i] = imports_cell
            elif 'df = pd.read_excel' in cell['source']:
                nb['cells'][i] = data_cell
            elif 'product_analysis = df_clean.groupby' in cell['source']:
                nb['cells'][i] = product_cell

    # Save the updated notebook
    with open('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_fin.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    update_notebook()
