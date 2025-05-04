import nbformat

def update_notebook():
    # Read the existing notebook
    with open('LalitNayyarIIMKMod4_predictive_analysis_1.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Add Purchase Frequency Prediction section with fixed feature creation
    nb['cells'].append(nbformat.v4.new_markdown_cell('''## Purchase Frequency Prediction Analysis
    
This section focuses on predicting customer purchase frequency using machine learning techniques.'''))

    nb['cells'].append(nbformat.v4.new_code_cell('''# Calculate total amount for each transaction
df['total_amount'] = df['Quantity'] * df['UnitPrice']

# Create customer features
customer_features = df.groupby('CustomerID').agg({
    'InvoiceNo': 'count',
    'Quantity': 'sum',
    'InvoiceDate': ['min', 'max'],
    'StockCode': 'nunique',
    'UnitPrice': 'mean',
    'total_amount': 'sum'
}).reset_index()

# Flatten column names
customer_features.columns = ['CustomerID', 'total_transactions', 'total_items', 
                           'first_purchase_date', 'last_purchase_date',
                           'unique_items_bought', 'average_unit_price',
                           'total_spent']

# Calculate additional features
customer_features['average_order_value'] = customer_features['total_spent'] / customer_features['total_transactions']
customer_features['average_items_per_transaction'] = customer_features['total_items'] / customer_features['total_transactions']

# Calculate purchase frequency
customer_features['purchase_frequency'] = customer_features['total_transactions'] / \
    ((customer_features['last_purchase_date'] - customer_features['first_purchase_date']).dt.days + 1)

# Display the first few rows of customer features
print("Sample of Customer Features:")
display(customer_features.head())
print("\nFeature Statistics:")
display(customer_features.describe())'''))

    nb['cells'].append(nbformat.v4.new_code_cell('''# Prepare features for purchase frequency prediction
def prepare_frequency_features(customer_features):
    features = customer_features.copy()
    
    # Select features for prediction
    X = features[['total_spent', 'average_order_value', 'total_transactions', 
                 'unique_items_bought', 'average_items_per_transaction']]
    y = features['purchase_frequency']
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate purchase frequency model
def train_frequency_model(X_train, X_test, y_train, y_test):
    # Initialize and train model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = rf_model.predict(X_test)
    
    # Calculate metrics
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    # Get feature importance
    feature_importance = pd.DataFrame({
        'feature': X_train.columns,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    return r2, rmse, feature_importance, rf_model

# Prepare the data and train the model
X_train, X_test, y_train, y_test = prepare_frequency_features(customer_features)
r2_freq, rmse_freq, feature_imp_freq, freq_model = train_frequency_model(X_train, X_test, y_train, y_test)

print("Purchase Frequency Prediction Results:")
print(f"R-squared Score: {r2_freq:.4f}")
print(f"Root Mean Square Error: {rmse_freq:.4f}")
print("\nFeature Importance:")
print(feature_imp_freq)

# Visualize feature importance
plt.figure(figsize=(10, 6))
sns.barplot(x='importance', y='feature', data=feature_imp_freq)
plt.title('Feature Importance for Purchase Frequency Prediction')
plt.tight_layout()
plt.show()'''))

    # Add Customer Lifetime Value Prediction section
    nb['cells'].append(nbformat.v4.new_markdown_cell('''## Customer Lifetime Value Prediction

This section focuses on predicting customer lifetime value to identify high-potential customers.'''))

    nb['cells'].append(nbformat.v4.new_code_cell('''# Prepare features for CLV prediction
def prepare_clv_features(customer_features):
    features = customer_features.copy()
    
    # Select features for prediction
    X = features[['average_order_value', 'total_transactions', 'purchase_frequency',
                 'unique_items_bought', 'average_items_per_transaction']]
    y = features['total_spent']  # Using total_spent as CLV
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate CLV model
def train_clv_model(X_train, X_test, y_train, y_test):
    # Initialize and train model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = rf_model.predict(X_test)
    
    # Calculate metrics
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    # Get feature importance
    feature_importance = pd.DataFrame({
        'feature': X_train.columns,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    return r2, rmse, feature_importance, rf_model

# Prepare the data and train the model
X_train, X_test, y_train, y_test = prepare_clv_features(customer_features)
r2_clv, rmse_clv, feature_imp_clv, clv_model = train_clv_model(X_train, X_test, y_train, y_test)

print("Customer Lifetime Value Prediction Results:")
print(f"R-squared Score: {r2_clv:.4f}")
print(f"Root Mean Square Error: {rmse_clv:.4f}")
print("\nFeature Importance:")
print(feature_imp_clv)

# Visualize feature importance
plt.figure(figsize=(10, 6))
sns.barplot(x='importance', y='feature', data=feature_imp_clv)
plt.title('Feature Importance for CLV Prediction')
plt.tight_layout()
plt.show()'''))

    # Add Business Applications section
    nb['cells'].append(nbformat.v4.new_markdown_cell('''## Business Applications

### 1. Inventory Management
- Purchase frequency predictions can be used for stock planning
- Optimize inventory levels based on predicted demand
- Reduce stockouts and overstock situations

### 2. Marketing Optimization
- Target high-potential customers identified through CLV prediction
- Adjust marketing spend based on predicted customer value
- Create personalized marketing campaigns based on purchase patterns

### 3. Customer Retention
- Identify at-risk customers through purchase frequency analysis
- Implement targeted retention strategies
- Focus on converting low-frequency buyers to high-frequency customers

### 4. Resource Allocation
- Optimize resource allocation based on customer value predictions
- Focus customer service efforts on high-value segments
- Align business strategies with customer potential'''))

    # Add Customer Segmentation based on Predictions
    nb['cells'].append(nbformat.v4.new_markdown_cell('''## Customer Segmentation Based on Predictions'''))

    nb['cells'].append(nbformat.v4.new_code_cell('''# Create customer segments based on predictions
def create_customer_segments(customer_features, freq_model, clv_model):
    # Get predictions
    freq_pred = freq_model.predict(customer_features[['total_spent', 'average_order_value', 
                                                    'total_transactions', 'unique_items_bought',
                                                    'average_items_per_transaction']])
    
    clv_pred = clv_model.predict(customer_features[['average_order_value', 'total_transactions',
                                                  'purchase_frequency', 'unique_items_bought',
                                                  'average_items_per_transaction']])
    
    # Create segments
    segments = pd.DataFrame({
        'CustomerID': customer_features['CustomerID'],
        'Predicted_Frequency': freq_pred,
        'Predicted_CLV': clv_pred
    })
    
    # Segment customers based on predictions
    segments['Frequency_Segment'] = pd.qcut(segments['Predicted_Frequency'], 
                                          q=3, labels=['Low', 'Medium', 'High'])
    segments['CLV_Segment'] = pd.qcut(segments['Predicted_CLV'],
                                    q=3, labels=['Low', 'Medium', 'High'])
    
    return segments

# Create and analyze segments
customer_segments = create_customer_segments(customer_features, freq_model, clv_model)

# Display segment distribution
print("Customer Segment Distribution:")
print("\nFrequency Segments:")
print(customer_segments['Frequency_Segment'].value_counts())
print("\nCLV Segments:")
print(customer_segments['CLV_Segment'].value_counts())

# Visualize segment distribution
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

customer_segments['Frequency_Segment'].value_counts().plot(kind='pie', ax=ax1, autopct='%1.1f%%')
ax1.set_title('Distribution of Frequency Segments')

customer_segments['CLV_Segment'].value_counts().plot(kind='pie', ax=ax2, autopct='%1.1f%%')
ax2.set_title('Distribution of CLV Segments')

plt.tight_layout()
plt.show()'''))

    # Save the updated notebook
    with open('LalitNayyarIIMKMod4_predictive_analysis_1.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    update_notebook()
