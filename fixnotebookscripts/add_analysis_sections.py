import nbformat

def update_notebook():
    # Read the existing notebook
    with open('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_fin.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Add Pricing Strategy Section
    pricing_markdown = nbformat.v4.new_markdown_cell('''### 4. Pricing Strategy Optimization
Analyze price elasticity and identify optimal price points for different product categories.''')
    
    pricing_code = nbformat.v4.new_code_cell('''# Analyze price elasticity and optimize pricing strategy
try:
    # Calculate price elasticity by product category
    product_price_analysis = df_clean.groupby('Description').agg({
        'UnitPrice': ['mean', 'std', 'min', 'max'],
        'Quantity': 'sum',
        'TotalAmount': 'sum'
    }).round(2)
    
    # Flatten column names
    product_price_analysis.columns = ['avg_price', 'price_std', 'min_price', 'max_price', 'total_quantity', 'total_revenue']
    
    # Calculate price ranges and revenue per unit
    product_price_analysis['price_range'] = product_price_analysis['max_price'] - product_price_analysis['min_price']
    product_price_analysis['revenue_per_unit'] = product_price_analysis['total_revenue'] / product_price_analysis['total_quantity']
    
    # Sort by revenue to find most profitable products
    top_profitable = product_price_analysis.sort_values('total_revenue', ascending=False).head(10)
    
    print("Top 10 Products by Revenue with Price Analysis:")
    display(top_profitable)
    
    # Visualize price vs quantity relationship for top products
    plt.figure(figsize=(12, 6))
    plt.scatter(product_price_analysis['avg_price'], product_price_analysis['total_quantity'], alpha=0.5)
    plt.xlabel('Average Price')
    plt.ylabel('Total Quantity Sold')
    plt.title('Price vs. Demand Relationship')
    
    # Add trend line
    z = np.polyfit(product_price_analysis['avg_price'], product_price_analysis['total_quantity'], 1)
    p = np.poly1d(z)
    plt.plot(product_price_analysis['avg_price'], p(product_price_analysis['avg_price']), "r--", alpha=0.8)
    
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Error in pricing analysis: {e}")''')

    # Add Seasonal Marketing Section
    seasonal_markdown = nbformat.v4.new_markdown_cell('''### 5. Seasonal Marketing Planning
Analyze seasonal trends and develop targeted marketing strategies.''')
    
    seasonal_code = nbformat.v4.new_code_cell('''# Analyze seasonal trends for marketing planning
try:
    # Add month and season columns if not already present
    if 'Month' not in df_clean.columns:
        df_clean['Month'] = df_clean['InvoiceDate'].dt.month
        df_clean['Season'] = df_clean['InvoiceDate'].dt.month.map(
            {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 
             5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
             9: 'Fall', 10: 'Fall', 11: 'Fall', 12: 'Winter'})
    
    # Analyze seasonal revenue patterns
    seasonal_revenue = df_clean.groupby(['Season', 'Month']).agg({
        'TotalAmount': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique',
        'CustomerID': 'nunique'
    }).round(2)
    
    seasonal_revenue.columns = ['Total Revenue', 'Items Sold', 'Number of Transactions', 'Unique Customers']
    
    print("Seasonal Business Performance:")
    display(seasonal_revenue)
    
    # Visualize seasonal patterns
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(data=df_clean, x='Season', y='TotalAmount')
    plt.title('Revenue Distribution by Season')
    plt.xticks(rotation=45)
    
    plt.subplot(1, 2, 2)
    seasonal_customer_count = df_clean.groupby('Season')['CustomerID'].nunique()
    sns.barplot(x=seasonal_customer_count.index, y=seasonal_customer_count.values)
    plt.title('Unique Customers by Season')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Error in seasonal analysis: {e}")''')

    # Add Customer Retention Section
    retention_markdown = nbformat.v4.new_markdown_cell('''### 6. Customer Retention Programs
Analyze customer loyalty patterns and develop retention strategies.''')
    
    retention_code = nbformat.v4.new_code_cell('''# Analyze customer retention patterns
try:
    # Calculate customer purchase frequency and recency
    customer_purchase_dates = df_clean.groupby('CustomerID').agg({
        'InvoiceDate': ['min', 'max', 'count'],
        'TotalAmount': 'sum'
    })
    
    customer_purchase_dates.columns = ['first_purchase', 'last_purchase', 'purchase_count', 'total_spent']
    
    # Calculate days between purchases
    customer_purchase_dates['customer_lifetime'] = (
        customer_purchase_dates['last_purchase'] - customer_purchase_dates['first_purchase']).dt.days
    
    customer_purchase_dates['avg_purchase_frequency'] = customer_purchase_dates['customer_lifetime'] / customer_purchase_dates['purchase_count']
    
    # Segment customers based on purchase frequency and spending
    customer_segments = customer_purchase_dates.copy()
    customer_segments['frequency_segment'] = pd.qcut(customer_segments['purchase_count'], q=3, labels=['Low', 'Medium', 'High'])
    customer_segments['spending_segment'] = pd.qcut(customer_segments['total_spent'], q=3, labels=['Low', 'Medium', 'High'])
    
    # Display customer segments
    segment_analysis = customer_segments.groupby(['frequency_segment', 'spending_segment']).agg({
        'CustomerID': 'count',
        'total_spent': 'mean',
        'purchase_count': 'mean',
        'avg_purchase_frequency': 'mean'
    }).round(2)
    
    print("Customer Segment Analysis:")
    display(segment_analysis)
    
    # Visualize customer segments
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(data=customer_segments, x='frequency_segment', y='total_spent')
    plt.title('Spending by Frequency Segment')
    plt.xticks(rotation=45)
    
    plt.subplot(1, 2, 2)
    segment_sizes = customer_segments.groupby('frequency_segment').size()
    plt.pie(segment_sizes, labels=segment_sizes.index, autopct='%1.1f%%')
    plt.title('Customer Segment Distribution')
    
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Error in retention analysis: {e}")''')

    # Add Personalized Marketing Section
    marketing_markdown = nbformat.v4.new_markdown_cell('''### 7. Personalized Marketing Campaigns
Develop targeted marketing strategies based on customer segments and preferences.''')
    
    marketing_code = nbformat.v4.new_code_cell('''# Analyze customer preferences for personalized marketing
try:
    # Create customer product preferences matrix
    customer_preferences = df_clean.groupby(['CustomerID', 'Description'])['Quantity'].sum().unstack(fill_value=0)
    
    # Perform customer segmentation using K-means
    scaler = StandardScaler()
    customer_preferences_scaled = scaler.fit_transform(customer_preferences)
    
    # Find optimal number of clusters
    inertias = []
    K = range(1, 6)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(customer_preferences_scaled)
        inertias.append(kmeans.inertia_)
    
    # Apply K-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    customer_segments = kmeans.fit_predict(customer_preferences_scaled)
    
    # Analyze segment characteristics
    customer_preferences['Segment'] = customer_segments
    segment_profiles = customer_preferences.groupby('Segment').agg(['mean', 'count'])
    
    # Get top products for each segment
    top_products_per_segment = {}
    for segment in range(3):
        segment_avg = customer_preferences[customer_preferences['Segment'] == segment].mean()
        top_products = segment_avg.nlargest(5)
        top_products_per_segment[f'Segment {segment}'] = top_products
    
    print("Top Products by Customer Segment:")
    for segment, products in top_products_per_segment.items():
        print(f"\\n{segment}:")
        display(products)
    
    # Visualize segment characteristics
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(K, inertias, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Inertia')
    plt.title('Elbow Method For Optimal k')
    
    plt.subplot(1, 2, 2)
    segment_sizes = pd.Series(customer_segments).value_counts()
    plt.pie(segment_sizes, labels=[f'Segment {i}' for i in range(len(segment_sizes))], autopct='%1.1f%%')
    plt.title('Customer Segment Distribution')
    
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Error in marketing analysis: {e}")''')

    # Add all new cells to the notebook
    nb['cells'].extend([
        pricing_markdown, pricing_code,
        seasonal_markdown, seasonal_code,
        retention_markdown, retention_code,
        marketing_markdown, marketing_code
    ])
    
    # Save the updated notebook
    with open('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_fin.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    update_notebook()
