import nbformat

def update_notebook():
    # Read the existing notebook
    with open('LalitNayyarIIMKMod4_descriptive_analysis_1.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Add data cleaning function
    cleaning_cell = nbformat.v4.new_code_cell('''def clean_data(df):
    """
    Clean the retail dataset by:
    1. Removing missing values
    2. Removing cancelled orders (those with 'C' in InvoiceNo)
    3. Ensuring positive quantities and prices
    4. Converting InvoiceDate to datetime
    """
    if df is None:
        return None
    
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
    
    # Reset index
    df_clean = df_clean.reset_index(drop=True)
    
    print("Data cleaning summary:")
    print(f"Original records: {len(df)}")
    print(f"Clean records: {len(df_clean)}")
    print(f"Removed records: {len(df) - len(df_clean)}")
    
    return df_clean''')
    
    # Insert the cleaning function cell after imports but before data loading
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code' and 'import' in cell['source']:
            nb['cells'].insert(i + 1, cleaning_cell)
            break
    
    # Save the updated notebook
    with open('LalitNayyarIIMKMod4_descriptive_analysis_1.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    update_notebook()
