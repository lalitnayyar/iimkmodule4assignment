import nbformat

def update_notebook():
    # Read the existing notebook
    with open('LalitNayyarIIMKMod4_descriptive_analysis_1.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Update the data loading and cleaning section
    data_prep_cell = nbformat.v4.new_code_cell('''# Load and prepare the data
df = pd.read_excel('Online Retail.xlsx')
print("Original data shape:", df.shape)

# Clean the data
df_clean = clean_data(df)
print("\nCleaned data shape:", df_clean.shape)

# Calculate total amount for each transaction
df_clean['TotalAmount'] = df_clean['Quantity'] * df_clean['UnitPrice']
print("\nSample of cleaned data with total amount:")
display(df_clean.head())

# Basic statistics of the cleaned dataset
print("\nBasic statistics of numerical columns:")
display(df_clean.describe())''')

    # Update the product analysis section
    product_analysis_cell = nbformat.v4.new_code_cell('''# Analyze top selling products
product_sales = df_clean.groupby('Description').agg({
    'Quantity': 'sum',
    'TotalAmount': 'sum',
    'InvoiceNo': 'count'
}).rename(columns={'InvoiceNo': 'TransactionCount'})

# Sort by quantity sold
top_products_by_quantity = product_sales.sort_values('Quantity', ascending=False).head(10)

# Display top products by quantity
print("Top 10 Products by Quantity Sold:")
display(top_products_by_quantity)

# Sort by total amount
top_products_by_amount = product_sales.sort_values('TotalAmount', ascending=False).head(10)

# Display top products by revenue
print("\nTop 10 Products by Revenue:")
display(top_products_by_amount)

# Visualize top products by quantity
plt.figure(figsize=(12, 6))
sns.barplot(x='Quantity', y=top_products_by_quantity.index, data=top_products_by_quantity)
plt.title('Top 10 Products by Quantity Sold')
plt.xlabel('Total Quantity Sold')
plt.tight_layout()
plt.show()

# Visualize top products by revenue
plt.figure(figsize=(12, 6))
sns.barplot(x='TotalAmount', y=top_products_by_amount.index, data=top_products_by_amount)
plt.title('Top 10 Products by Revenue')
plt.xlabel('Total Revenue')
plt.tight_layout()
plt.show()''')

    # Find and replace the relevant cells
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            if 'df = pd.read_excel' in cell['source']:
                nb['cells'][i] = data_prep_cell
            elif 'product_sales = df_clean.groupby' in cell['source']:
                nb['cells'][i] = product_analysis_cell

    # Save the updated notebook
    with open('LalitNayyarIIMKMod4_descriptive_analysis_1.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    update_notebook()
