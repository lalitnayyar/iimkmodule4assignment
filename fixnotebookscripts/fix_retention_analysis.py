import nbformat

def update_notebook():
    # Read the existing notebook
    with open('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_fin.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Update the customer retention analysis cell
    retention_cell = nbformat.v4.new_code_cell('''# Analyze customer retention patterns
try:
    print("Starting customer retention analysis...")
    
    # Ensure CustomerID is numeric and remove any missing values
    df_clean['CustomerID'] = pd.to_numeric(df_clean['CustomerID'], errors='coerce')
    df_customers = df_clean.dropna(subset=['CustomerID'])
    
    print(f"Analyzing {df_customers['CustomerID'].nunique()} unique customers")
    
    # Calculate customer metrics
    customer_metrics = df_customers.groupby('CustomerID').agg({
        'InvoiceDate': ['min', 'max', 'count'],
        'TotalAmount': ['sum', 'mean'],
        'Quantity': 'sum',
        'Description': 'nunique'
    })
    
    # Flatten column names
    customer_metrics.columns = [
        'first_purchase', 'last_purchase', 'purchase_count',
        'total_spent', 'avg_order_value', 'total_items',
        'unique_products'
    ]
    
    # Calculate customer lifetime and frequency
    customer_metrics['customer_lifetime_days'] = (
        customer_metrics['last_purchase'] - customer_metrics['first_purchase']
    ).dt.days
    
    # Avoid division by zero
    customer_metrics['avg_days_between_purchases'] = np.where(
        customer_metrics['purchase_count'] > 1,
        customer_metrics['customer_lifetime_days'] / (customer_metrics['purchase_count'] - 1),
        0
    )
    
    # Create customer segments
    customer_metrics['recency_days'] = (
        df_customers['InvoiceDate'].max() - customer_metrics['last_purchase']
    ).dt.days
    
    # Create segments using quartiles
    for metric in ['total_spent', 'purchase_count', 'recency_days']:
        customer_metrics[f'{metric}_segment'] = pd.qcut(
            customer_metrics[metric],
            q=4,
            labels=['Low', 'Medium-Low', 'Medium-High', 'High']
        )
    
    print("\\nCustomer Metrics Summary:")
    display(customer_metrics.describe().round(2))
    
    # Analyze customer segments
    print("\\nCustomer Segments by Spending:")
    display(customer_metrics.groupby('total_spent_segment').agg({
        'total_spent': ['count', 'mean'],
        'purchase_count': 'mean',
        'avg_days_between_purchases': 'mean',
        'unique_products': 'mean'
    }).round(2))
    
    # Visualize customer segments
    plt.figure(figsize=(15, 5))
    
    # Plot 1: Spending Distribution
    plt.subplot(1, 3, 1)
    sns.boxplot(data=customer_metrics, y='total_spent')
    plt.title('Customer Spending Distribution')
    plt.ylabel('Total Spent')
    
    # Plot 2: Purchase Frequency
    plt.subplot(1, 3, 2)
    sns.histplot(data=customer_metrics, x='purchase_count', bins=30)
    plt.title('Purchase Frequency Distribution')
    plt.xlabel('Number of Purchases')
    
    # Plot 3: Customer Segments
    plt.subplot(1, 3, 3)
    segment_sizes = customer_metrics['total_spent_segment'].value_counts()
    plt.pie(segment_sizes, labels=segment_sizes.index, autopct='%1.1f%%')
    plt.title('Customer Segments by Spending')
    
    plt.tight_layout()
    plt.show()
    
    # Calculate retention metrics
    print("\\nCustomer Retention Analysis:")
    total_customers = customer_metrics.shape[0]
    repeat_customers = (customer_metrics['purchase_count'] > 1).sum()
    retention_rate = (repeat_customers / total_customers) * 100
    
    print(f"Total Customers: {total_customers}")
    print(f"Repeat Customers: {repeat_customers}")
    print(f"Retention Rate: {retention_rate:.2f}%")
    
except Exception as e:
    print(f"Error in retention analysis: {e}")
    print("Debug info:")
    print(f"DataFrame columns: {df_clean.columns.tolist()}")
    print(f"CustomerID dtype: {df_clean['CustomerID'].dtype}")
    print("Sample of CustomerID values:", df_clean['CustomerID'].head())''')

    # Find and replace the retention analysis cell
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code' and 'customer_purchase_dates = df_clean.groupby' in cell['source']:
            nb['cells'][i] = retention_cell
            break
    
    # If not found, append it
    if 'customer_purchase_dates = df_clean.groupby' not in [cell['source'] for cell in nb['cells'] if cell['cell_type'] == 'code']:
        retention_markdown = nbformat.v4.new_markdown_cell('''### 6. Customer Retention Programs
Analyze customer loyalty patterns and develop retention strategies.''')
        nb['cells'].extend([retention_markdown, retention_cell])

    # Save the updated notebook
    with open('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_fin.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    update_notebook()
