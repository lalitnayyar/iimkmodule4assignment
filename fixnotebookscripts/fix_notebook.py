import nbformat

def update_notebook():
    # Read the existing notebook
    with open('LalitNayyarIIMKMod4_predictive_analysis_1.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Add Data Preparation section
    nb['cells'].append(nbformat.v4.new_markdown_cell('''## Data Preparation and Feature Engineering'''))
    
    nb['cells'].append(nbformat.v4.new_code_cell('''# Load the data
df = pd.read_csv('cleaned_retail_data.csv')

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Calculate total amount for each transaction
df['total_amount'] = df['Quantity'] * df['UnitPrice']

print("Data loaded successfully. Shape:", df.shape)
display(df.head())'''))

    # Add Feature Creation section
    nb['cells'].append(nbformat.v4.new_code_cell('''# Create customer features
def create_customer_features(df):
    # Group by CustomerID and calculate aggregates
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
    
    return customer_features

# Create customer features
customer_features = create_customer_features(df)

print("Customer features created successfully. Shape:", customer_features.shape)
display(customer_features.head())
print("\nFeature Statistics:")
display(customer_features.describe())'''))

    # Add Purchase Frequency Prediction section
    nb['cells'].append(nbformat.v4.new_markdown_cell('''## Purchase Frequency Prediction Analysis
    
This section focuses on predicting customer purchase frequency using machine learning techniques.'''))

    nb['cells'].append(nbformat.v4.new_code_cell('''# Calculate purchase frequency
customer_features['purchase_frequency'] = customer_features['total_transactions'] / \
    ((customer_features['last_purchase_date'] - customer_features['first_purchase_date']).dt.days + 1)

# Prepare features for purchase frequency prediction
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

    # Save the updated notebook
    with open('LalitNayyarIIMKMod4_predictive_analysis_1.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    update_notebook()
