import json
import nbformat
from pathlib import Path

def create_markdown_cell(content):
    """Create a markdown cell with given content."""
    return nbformat.v4.new_markdown_cell(content)

def create_code_cell(content):
    """Create a code cell with given content."""
    return nbformat.v4.new_code_cell(content)

def fix_predictive_notebook(notebook_path):
    """Fix and enhance the predictive analysis notebook."""
    try:
        # Read the notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
        
        # Create backup
        backup_path = Path(notebook_path).parent / f"{Path(notebook_path).stem}_backup.ipynb"
        with open(backup_path, 'w', encoding='utf-8') as f:
            nbformat.write(notebook, f)
        
        # Reset notebook cells
        notebook.cells = []
        
        # Add header markdown
        header_md = """# Customer Behavior Predictive Analysis
## IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers
**Student Name**: Lalit Nayyar  
**Email ID**: lalitnayyar@gmail.com  
**Assignment**: Week 4: Required Assignment 4.1

This notebook focuses on predictive analytics for customer behavior, including:
1. Feature Engineering
2. Model Development
3. Prediction and Evaluation
"""
        notebook.cells.append(create_markdown_cell(header_md))
        
        # Add imports
        imports_code = """# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
plt.style.use('seaborn')

print("All required libraries imported successfully!")"""
        notebook.cells.append(create_code_cell(imports_code))
        
        # Add data loading section
        data_loading_md = """## 1. Data Loading and Validation
Loading the cleaned customer data from previous analysis."""
        notebook.cells.append(create_markdown_cell(data_loading_md))
        
        data_loading_code = """def validate_data(df):
    '''Validate the loaded data for required columns and data quality'''
    required_columns = ['CustomerID', 'InvoiceNo', 'InvoiceDate', 
                       'Quantity', 'UnitPrice', 'TotalAmount']
    
    # Check required columns
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    # Check data types
    if not pd.api.types.is_numeric_dtype(df['CustomerID']):
        raise ValueError("CustomerID should be numeric")
    if not pd.api.types.is_datetime64_any_dtype(df['InvoiceDate']):
        raise ValueError("InvoiceDate should be datetime")
    
    return True

# Load and validate data
try:
    df = pd.read_csv('cleaned_retail_data.csv')
    if 'InvoiceDate' in df.columns:
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    validate_data(df)
    print("Data loaded and validated successfully!")
    print(f"Dataset shape: {df.shape}")
    print("\nSample of the data:")
    display(df.head())
    
except FileNotFoundError:
    print("Error: cleaned_retail_data.csv not found!")
    print("Please run the analysis notebook first to generate the cleaned dataset.")
except Exception as e:
    print(f"Error in data loading/validation: {e}")"""
        notebook.cells.append(create_code_cell(data_loading_code))
        
        # Add feature engineering section
        feature_eng_md = """## 2. Feature Engineering
Creating customer-level features for predictive modeling."""
        notebook.cells.append(create_markdown_cell(feature_eng_md))
        
        feature_eng_code = """def create_customer_features(df):
    '''Create comprehensive customer-level features for prediction'''
    try:
        # Calculate recency
        max_date = df['InvoiceDate'].max()
        customer_features = df.groupby('CustomerID').agg({
            'InvoiceDate': lambda x: (max_date - x.max()).days,  # Recency
            'InvoiceNo': 'count',  # Frequency
            'TotalAmount': ['sum', 'mean', 'std'],  # Monetary metrics
            'Quantity': ['sum', 'mean', 'std'],  # Purchase quantity metrics
        })
        
        # Flatten column names
        customer_features.columns = [
            'Recency', 'Frequency', 
            'TotalRevenue', 'AvgPurchaseValue', 'StdPurchaseValue',
            'TotalQuantity', 'AvgQuantity', 'StdQuantity'
        ]
        
        # Add derived features
        customer_features['PurchaseVariability'] = customer_features['StdPurchaseValue'] / customer_features['AvgPurchaseValue']
        customer_features['QuantityVariability'] = customer_features['StdQuantity'] / customer_features['AvgQuantity']
        
        # Handle infinities and NaNs
        customer_features = customer_features.replace([np.inf, -np.inf], np.nan)
        customer_features = customer_features.fillna(0)
        
        print("Feature engineering completed successfully!")
        return customer_features
    
    except Exception as e:
        print(f"Error in feature engineering: {e}")
        return None

# Create features
customer_features = create_customer_features(df)
if customer_features is not None:
    print("\nFeature summary:")
    display(customer_features.describe())"""
        notebook.cells.append(create_code_cell(feature_eng_code))
        
        # Add model preparation section
        model_prep_md = """## 3. Model Preparation
Preparing features and target variable for modeling."""
        notebook.cells.append(create_markdown_cell(model_prep_md))
        
        model_prep_code = """def prepare_features_and_target(customer_features):
    '''Prepare features and target for modeling'''
    try:
        # Use TotalRevenue as target variable
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
        
        print("Data preparation completed successfully!")
        return X_train_scaled, X_test_scaled, y_train, y_test, scaler
    
    except Exception as e:
        print(f"Error in data preparation: {e}")
        return None, None, None, None, None

# Prepare data for modeling
X_train_scaled, X_test_scaled, y_train, y_test, scaler = prepare_features_and_target(customer_features)"""
        notebook.cells.append(create_code_cell(model_prep_code))
        
        # Add model training section
        model_train_md = """## 4. Model Training and Evaluation
Training Random Forest model and evaluating its performance."""
        notebook.cells.append(create_markdown_cell(model_train_md))
        
        model_train_code = """def train_and_evaluate_model(X_train_scaled, X_test_scaled, y_train, y_test):
    '''Train and evaluate the Random Forest model'''
    try:
        # Train model
        rf_model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        rf_model.fit(X_train_scaled, y_train)
        
        # Make predictions
        y_pred = rf_model.predict(X_test_scaled)
        
        # Calculate metrics
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        
        print("Model Training Results:")
        print(f"R² Score: {r2:.4f}")
        print(f"RMSE: {rmse:.2f}")
        print(f"MAE: {mae:.2f}")
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'feature': X_train.columns,
            'importance': rf_model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        # Plot feature importance
        plt.figure(figsize=(10, 6))
        sns.barplot(x='importance', y='feature', data=feature_importance)
        plt.title('Feature Importance')
        plt.xlabel('Importance')
        plt.tight_layout()
        plt.show()
        
        return rf_model, feature_importance
    
    except Exception as e:
        print(f"Error in model training: {e}")
        return None, None

# Train and evaluate model
if all(v is not None for v in [X_train_scaled, X_test_scaled, y_train, y_test]):
    rf_model, feature_importance = train_and_evaluate_model(
        X_train_scaled, X_test_scaled, y_train, y_test
    )"""
        notebook.cells.append(create_code_cell(model_train_code))
        
        # Add prediction section
        prediction_md = """## 5. Making Predictions
Using the trained model to make predictions."""
        notebook.cells.append(create_markdown_cell(prediction_md))
        
        prediction_code = """def make_predictions(model, scaler, customer_features, top_n=10):
    '''Make predictions for customer revenue'''
    try:
        if model is None or scaler is None:
            raise ValueError("Model or scaler not available")
        
        # Prepare features for prediction
        X_pred = customer_features.drop('TotalRevenue', axis=1)
        X_pred_scaled = scaler.transform(X_pred)
        
        # Make predictions
        predictions = model.predict(X_pred_scaled)
        
        # Create results DataFrame
        results = pd.DataFrame({
            'CustomerID': customer_features.index,
            'Actual_Revenue': customer_features['TotalRevenue'],
            'Predicted_Revenue': predictions
        })
        
        # Calculate prediction error
        results['Prediction_Error'] = abs(results['Actual_Revenue'] - results['Predicted_Revenue'])
        results['Error_Percentage'] = (results['Prediction_Error'] / results['Actual_Revenue']) * 100
        
        print("Top 10 Customers by Predicted Revenue:")
        display(results.nlargest(top_n, 'Predicted_Revenue'))
        
        # Plot actual vs predicted
        plt.figure(figsize=(10, 6))
        plt.scatter(results['Actual_Revenue'], results['Predicted_Revenue'], alpha=0.5)
        plt.plot([0, results['Actual_Revenue'].max()], [0, results['Actual_Revenue'].max()], 'r--')
        plt.xlabel('Actual Revenue')
        plt.ylabel('Predicted Revenue')
        plt.title('Actual vs Predicted Revenue')
        plt.tight_layout()
        plt.show()
        
        return results
    
    except Exception as e:
        print(f"Error in making predictions: {e}")
        return None

# Make predictions
if rf_model is not None and scaler is not None:
    prediction_results = make_predictions(rf_model, scaler, customer_features)"""
        notebook.cells.append(create_code_cell(prediction_code))
        
        # Save the enhanced notebook
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(notebook, f)
        
        print(f"Successfully enhanced {notebook_path}")
        print(f"Backup saved as {backup_path}")
        return True
        
    except Exception as e:
        print(f"Error enhancing notebook: {str(e)}")
        return False

if __name__ == "__main__":
    notebook_path = "LalitNayyarIIMKMod4_predictive_analysis_1.ipynb"
    fix_predictive_notebook(notebook_path)
