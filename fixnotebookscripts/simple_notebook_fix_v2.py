import nbformat
from pathlib import Path

def create_notebook():
    """Create a new notebook with proper structure and error handling"""
    
    # Initialize notebook
    nb = nbformat.v4.new_notebook()
    
    # Add metadata
    nb.metadata = {
        'kernelspec': {
            'display_name': 'Python 3',
            'language': 'python',
            'name': 'python3'
        }
    }
    
    # Create cells
    cells = []
    
    # Header
    cells.append(nbformat.v4.new_markdown_cell('''# Customer Behavior Predictive Analysis
## IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers
**Student Name**: Lalit Nayyar  
**Email ID**: lalitnayyar@gmail.com  
**Assignment**: Week 4: Required Assignment 4.1'''))
    
    # Imports
    cells.append(nbformat.v4.new_code_cell('''# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

# Set plot style
plt.style.use('default')  # Using default style instead of seaborn
sns.set_theme(style="whitegrid")  # Set seaborn style this way instead'''))
    
    # Data Loading
    cells.append(nbformat.v4.new_markdown_cell('## 1. Data Loading and Cleaning'))
    cells.append(nbformat.v4.new_code_cell('''# Load the original data
try:
    df = pd.read_excel('Online Retail.xlsx')
    print("Data loaded successfully!")
    print(f"Initial shape: {df.shape}")
except Exception as e:
    print(f"Error loading data: {e}")'''))
    
    # Data Cleaning
    cells.append(nbformat.v4.new_code_cell('''# Clean the data
try:
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.dropna(subset=['CustomerID'])
    
    # Convert data types
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['CustomerID'] = df['CustomerID'].astype(int)
    
    # Calculate total amount
    df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
    
    # Remove invalid transactions
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    df = df[~df['InvoiceNo'].astype(str).str.contains('C', na=False)]
    
    print("\nCleaning completed!")
    print(f"Final shape: {df.shape}")
    
    # Save cleaned data
    df.to_csv('cleaned_retail_data.csv', index=False)
    print("\nCleaned data saved to 'cleaned_retail_data.csv'")
    
except Exception as e:
    print(f"Error cleaning data: {e}")'''))
    
    # Feature Engineering
    cells.append(nbformat.v4.new_markdown_cell('## 2. Feature Engineering'))
    cells.append(nbformat.v4.new_code_cell('''# Create customer features
try:
    # Calculate customer metrics
    max_date = df['InvoiceDate'].max()
    
    customer_features = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (max_date - x.max()).days,  # Recency
        'InvoiceNo': 'count',  # Frequency
        'TotalAmount': ['sum', 'mean']  # Monetary
    })
    
    # Flatten column names
    customer_features.columns = ['Recency', 'Frequency', 'TotalRevenue', 'AvgPurchaseValue']
    
    print("Features created successfully!")
    print("\nFeature summary:")
    display(customer_features.describe())
    
except Exception as e:
    print(f"Error in feature engineering: {e}")'''))
    
    # Model Training
    cells.append(nbformat.v4.new_markdown_cell('## 3. Model Training'))
    cells.append(nbformat.v4.new_code_cell('''# Prepare data for modeling
try:
    # Prepare features and target
    X = customer_features.drop('TotalRevenue', axis=1)
    y = customer_features['TotalRevenue']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test_scaled)
    
    # Calculate performance
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print("Model Results:")
    print(f"R² Score: {r2:.4f}")
    print(f"RMSE: {rmse:.2f}")
    
except Exception as e:
    print(f"Error in model training: {e}")'''))
    
    # Visualization
    cells.append(nbformat.v4.new_markdown_cell('## 4. Results Visualization'))
    cells.append(nbformat.v4.new_code_cell('''# Plot results
try:
    # Feature importance
    importance = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=importance, x='importance', y='feature')
    plt.title('Feature Importance')
    plt.tight_layout()
    plt.show()
    
    # Actual vs Predicted
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel('Actual Revenue')
    plt.ylabel('Predicted Revenue')
    plt.title('Actual vs Predicted Revenue')
    plt.tight_layout()
    plt.show()
    
except Exception as e:
    print(f"Error in visualization: {e}")'''))
    
    # Add cells to notebook
    nb.cells = cells
    return nb

def save_notebook(notebook_path):
    """Save the notebook to the specified path"""
    try:
        # Create new notebook
        nb = create_notebook()
        
        # Create backup of existing notebook if it exists
        if Path(notebook_path).exists():
            backup_path = Path(notebook_path).parent / f"{Path(notebook_path).stem}_backup.ipynb"
            Path(notebook_path).rename(backup_path)
            print(f"Created backup at {backup_path}")
        
        # Save new notebook
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"Successfully created new notebook at {notebook_path}")
        return True
    
    except Exception as e:
        print(f"Error saving notebook: {e}")
        return False

if __name__ == "__main__":
    notebook_path = "LalitNayyarIIMKMod4_predictive_analysis_1.ipynb"
    save_notebook(notebook_path)
