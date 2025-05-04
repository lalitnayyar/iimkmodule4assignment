import nbformat

def update_notebook():
    # Read the existing notebook
    with open('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_final.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Update the data loading and cleaning cell
    data_loading_cell = nbformat.v4.new_code_cell('''# Load and prepare the data
try:
    # Load the data
    df = pd.read_excel('Online Retail.xlsx')
    print("Original data shape:", df.shape)
    
    # Define the cleaning function
    def clean_data(df):
        """
        Clean the retail dataset by:
        1. Removing missing values
        2. Removing cancelled orders (those with 'C' in InvoiceNo)
        3. Ensuring positive quantities and prices
        4. Converting InvoiceDate to datetime
        5. Adding TotalAmount column
        """
        # Create a copy of the dataframe
        df_clean = df.copy()
        
        # Remove rows with missing values
        df_clean = df_clean.dropna()
        
        # Remove cancelled orders (those with 'C' in InvoiceNo)
        df_clean = df_clean[~df_clean['InvoiceNo'].astype(str).str.contains('C')]
        
        # Ensure positive quantities and prices
        df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)]
        
        # Convert InvoiceDate to datetime if it's not already
        if not pd.api.types.is_datetime64_any_dtype(df_clean['InvoiceDate']):
            df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])
        
        # Calculate total amount
        df_clean['TotalAmount'] = df_clean['Quantity'] * df_clean['UnitPrice']
        
        # Reset index
        df_clean = df_clean.reset_index(drop=True)
        
        print("Data cleaning summary:")
        print(f"Original records: {len(df)}")
        print(f"Clean records: {len(df_clean)}")
        print(f"Removed records: {len(df) - len(df_clean)}")
        
        return df_clean
    
    # Clean the data
    df_clean = clean_data(df)
    print("\nCleaned data sample:")
    display(df_clean.head())
    
except FileNotFoundError:
    print("Error: 'Online Retail.xlsx' file not found. Please ensure it's in the correct directory.")
except Exception as e:
    print(f"Error loading data: {e}")''')

    # Update the product analysis cell
    product_analysis_cell = nbformat.v4.new_code_cell('''# Analyze price points vs. sales volume
try:
    product_analysis = df_clean.groupby('Description').agg({
        'Quantity': 'sum',
        'UnitPrice': 'mean',
        'TotalAmount': 'sum'
    }).reset_index()

    # Calculate correlation between price and quantity
    correlation = stats.pearsonr(product_analysis['UnitPrice'], product_analysis['Quantity'])

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=product_analysis, x='UnitPrice', y='Quantity')
    plt.title('Price vs. Sales Volume Relationship')
    plt.xlabel('Unit Price')
    plt.ylabel('Total Quantity Sold')
    plt.text(0.05, 0.95, f'Correlation: {correlation[0]:.2f}\\np-value: {correlation[1]:.4f}',
             transform=plt.gca().transAxes)
    plt.show()
except Exception as e:
    print(f"Error in product analysis: {e}")''')

    # Update the seasonal analysis cell
    seasonal_analysis_cell = nbformat.v4.new_code_cell('''# Analyze seasonal patterns
try:
    # Add time-based features
    df_clean['Month'] = df_clean['InvoiceDate'].dt.month
    df_clean['Season'] = df_clean['InvoiceDate'].dt.month.map(
        {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 
         5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
         9: 'Fall', 10: 'Fall', 11: 'Fall', 12: 'Winter'})

    # Analyze seasonal sales patterns
    seasonal_category_sales = df_clean.groupby(['Season', 'Description'])['Quantity'].sum().reset_index()
    top_products_per_season = seasonal_category_sales.sort_values('Quantity', ascending=False).groupby('Season').head(5)

    plt.figure(figsize=(15, 8))
    sns.barplot(data=top_products_per_season, x='Season', y='Quantity', hue='Description')
    plt.title('Top Products by Season')
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Error in seasonal analysis: {e}")''')

    # Update the customer analysis cell
    customer_analysis_cell = nbformat.v4.new_code_cell('''# Analyze customer purchasing behavior
try:
    customer_analysis = df_clean.groupby('CustomerID').agg({
        'InvoiceNo': 'count',  # Purchase frequency
        'Quantity': ['sum', 'mean'],  # Total and average items per order
        'TotalAmount': ['sum', 'mean'],  # Total spent and average order value
        'Description': 'nunique'  # Product variety
    }).round(2)

    customer_analysis.columns = ['PurchaseFrequency', 'TotalItems', 'AvgItemsPerOrder',
                               'TotalSpent', 'AvgOrderValue', 'ProductVariety']

    # Calculate correlations
    correlations = customer_analysis.corr()['TotalSpent'].sort_values(ascending=False)
    
    print("Correlations with Total Spending:")
    display(correlations)

    # Visualize relationships
    plt.figure(figsize=(12, 8))
    sns.heatmap(customer_analysis.corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix of Customer Behavior Metrics')
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Error in customer analysis: {e}")''')

    # Find and replace cells
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            if 'df = pd.read_excel' in cell['source']:
                nb['cells'][i] = data_loading_cell
            elif 'product_analysis = df_clean.groupby' in cell['source']:
                nb['cells'][i] = product_analysis_cell
            elif 'df_clean[\'Month\'] = pd.to_datetime' in cell['source']:
                nb['cells'][i] = seasonal_analysis_cell
            elif 'customer_analysis = df_clean.groupby' in cell['source']:
                nb['cells'][i] = customer_analysis_cell

    # Save the updated notebook
    with open('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_final.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    update_notebook()
