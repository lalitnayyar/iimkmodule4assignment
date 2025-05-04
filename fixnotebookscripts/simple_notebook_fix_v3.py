import nbformat
from pathlib import Path

def create_notebook():
    """Create a new notebook with enhanced business analysis"""
    nb = nbformat.v4.new_notebook()
    nb.metadata = {'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
    cells = []
    
    # Header and imports remain the same as before, but add more libraries
    cells.append(nbformat.v4.new_markdown_cell('''# Customer Behavior Predictive Analysis
## IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers
**Student Name**: Lalit Nayyar  
**Email ID**: lalitnayyar@gmail.com  
**Assignment**: Week 4: Required Assignment 4.1'''))
    
    cells.append(nbformat.v4.new_code_cell('''# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

# Set plot style
plt.style.use('default')
sns.set_theme(style="whitegrid")'''))

    # Previous data loading and cleaning cells remain the same...
    
    # Add new business analysis sections
    cells.append(nbformat.v4.new_markdown_cell('''## 5. Business Applications

### 5.1 Inventory Management Analysis
Analyzing purchase patterns and product demand for inventory optimization.'''))
    
    cells.append(nbformat.v4.new_code_cell('''# Inventory Management Analysis
try:
    # Product demand analysis
    product_demand = df.groupby('StockCode').agg({
        'Quantity': ['sum', 'mean', 'std'],
        'InvoiceNo': 'count'
    }).round(2)
    product_demand.columns = ['TotalQuantity', 'AvgQuantity', 'StdQuantity', 'OrderCount']
    
    # Calculate reorder points (example using 2 sigma for safety stock)
    product_demand['ReorderPoint'] = (product_demand['AvgQuantity'] * 7 + 
                                    2 * product_demand['StdQuantity'])
    
    # Top products by demand
    top_products = product_demand.nlargest(10, 'TotalQuantity')
    
    # Visualize top products
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_products.reset_index(), 
                x='TotalQuantity', y='StockCode')
    plt.title('Top 10 Products by Demand')
    plt.tight_layout()
    plt.show()
    
    print("\nInventory Management Insights:")
    print("Top 5 Products Reorder Points:")
    display(product_demand.nlargest(5, 'ReorderPoint')[['AvgQuantity', 'StdQuantity', 'ReorderPoint']])
    
except Exception as e:
    print(f"Error in inventory analysis: {e}")'''))

    cells.append(nbformat.v4.new_markdown_cell('''### 5.2 Marketing Optimization
Identifying high-value customers and segments for targeted marketing.'''))
    
    cells.append(nbformat.v4.new_code_cell('''# Marketing Optimization Analysis
try:
    # RFM Segmentation
    rfm_scores = customer_features.copy()
    
    # Convert metrics to scores 1-5
    for metric in ['Recency', 'Frequency', 'TotalRevenue']:
        labels = range(5, 0, -1) if metric == 'Recency' else range(1, 6)
        rfm_scores[f'{metric}_Score'] = pd.qcut(rfm_scores[metric], q=5, labels=labels)
    
    # Calculate RFM Score
    rfm_scores['RFM_Score'] = (rfm_scores['Recency_Score'].astype(str) + 
                              rfm_scores['Frequency_Score'].astype(str) + 
                              rfm_scores['TotalRevenue_Score'].astype(str))
    
    # Customer Segmentation
    def segment_customers(row):
        r, f, m = row['Recency_Score'], row['Frequency_Score'], row['TotalRevenue_Score']
        if r >= 4 and f >= 4 and m >= 4:
            return 'Champions'
        elif r >= 3 and f >= 3 and m >= 3:
            return 'Loyal Customers'
        elif r >= 3 and f >= 1 and m >= 2:
            return 'Potential Loyalists'
        elif r <= 2 and f <= 2 and m <= 2:
            return 'Lost Customers'
        else:
            return 'Average Customers'
    
    rfm_scores['Customer_Segment'] = rfm_scores.apply(segment_customers, axis=1)
    
    # Visualize segments
    plt.figure(figsize=(10, 6))
    segment_counts = rfm_scores['Customer_Segment'].value_counts()
    sns.barplot(x=segment_counts.index, y=segment_counts.values)
    plt.title('Customer Segments Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Segment characteristics
    print("\nSegment Characteristics:")
    display(rfm_scores.groupby('Customer_Segment').agg({
        'TotalRevenue': 'mean',
        'Frequency': 'mean',
        'Recency': 'mean'
    }).round(2))
    
except Exception as e:
    print(f"Error in marketing analysis: {e}")'''))

    cells.append(nbformat.v4.new_markdown_cell('''### 5.3 Customer Retention Analysis
Identifying at-risk customers and retention opportunities.'''))
    
    cells.append(nbformat.v4.new_code_cell('''# Customer Retention Analysis
try:
    # Calculate customer risk scores
    retention_metrics = customer_features.copy()
    
    # Risk factors:
    # 1. High recency (hasn't purchased recently)
    # 2. Low frequency (few purchases)
    # 3. Declining purchase value
    
    # Calculate risk score (0-100, higher = more at risk)
    max_recency = retention_metrics['Recency'].max()
    retention_metrics['RecencyRisk'] = (retention_metrics['Recency'] / max_recency) * 100
    
    max_freq = retention_metrics['Frequency'].max()
    retention_metrics['FrequencyRisk'] = ((max_freq - retention_metrics['Frequency']) / max_freq) * 100
    
    retention_metrics['ChurnRisk'] = (retention_metrics['RecencyRisk'] * 0.5 + 
                                    retention_metrics['FrequencyRisk'] * 0.5)
    
    # Categorize risk levels
    retention_metrics['RiskLevel'] = pd.qcut(retention_metrics['ChurnRisk'], 
                                           q=3, 
                                           labels=['Low', 'Medium', 'High'])
    
    # Visualize risk distribution
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=retention_metrics, x='RiskLevel', y='TotalRevenue')
    plt.title('Customer Value by Risk Level')
    plt.tight_layout()
    plt.show()
    
    # High-risk valuable customers
    high_risk_valuable = retention_metrics[
        (retention_metrics['RiskLevel'] == 'High') & 
        (retention_metrics['TotalRevenue'] > retention_metrics['TotalRevenue'].median())
    ]
    
    print("\nHigh-Risk Valuable Customers Summary:")
    print(f"Number of high-risk valuable customers: {len(high_risk_valuable)}")
    print("\nAverage metrics for high-risk valuable customers:")
    display(high_risk_valuable[['Recency', 'Frequency', 'TotalRevenue', 'ChurnRisk']].mean().round(2))
    
except Exception as e:
    print(f"Error in retention analysis: {e}")'''))

    cells.append(nbformat.v4.new_markdown_cell('''### 5.4 Resource Allocation Analysis
Optimizing resource allocation based on customer value and needs.'''))
    
    cells.append(nbformat.v4.new_code_cell('''# Resource Allocation Analysis
try:
    # Customer value analysis
    value_analysis = customer_features.copy()
    
    # Calculate customer lifetime value (simple version)
    value_analysis['CLV'] = value_analysis['TotalRevenue'] * (value_analysis['Frequency'] / value_analysis['Recency'])
    
    # Customer segments based on value
    value_analysis['ValueSegment'] = pd.qcut(value_analysis['CLV'], 
                                           q=4, 
                                           labels=['Bronze', 'Silver', 'Gold', 'Platinum'])
    
    # Analyze segment characteristics
    segment_analysis = value_analysis.groupby('ValueSegment').agg({
        'CLV': 'mean',
        'TotalRevenue': 'sum',
        'Frequency': 'mean',
        'CustomerID': 'count'
    }).round(2)
    
    segment_analysis['Revenue_Proportion'] = (segment_analysis['TotalRevenue'] / 
                                            segment_analysis['TotalRevenue'].sum() * 100)
    
    # Visualize value distribution
    plt.figure(figsize=(12, 6))
    
    # Create subplot for customer distribution
    plt.subplot(1, 2, 1)
    customer_dist = value_analysis['ValueSegment'].value_counts()
    plt.pie(customer_dist, labels=customer_dist.index, autopct='%1.1f%%')
    plt.title('Customer Distribution by Segment')
    
    # Create subplot for revenue distribution
    plt.subplot(1, 2, 2)
    revenue_dist = segment_analysis['Revenue_Proportion']
    plt.pie(revenue_dist, labels=revenue_dist.index, autopct='%1.1f%%')
    plt.title('Revenue Distribution by Segment')
    
    plt.tight_layout()
    plt.show()
    
    print("\nSegment Analysis:")
    display(segment_analysis)
    
    # Resource allocation recommendations
    print("\nResource Allocation Recommendations:")
    for segment in ['Platinum', 'Gold', 'Silver', 'Bronze']:
        segment_data = segment_analysis.loc[segment]
        print(f"\n{segment} Segment:")
        print(f"- Customers: {segment_data['CustomerID']:.0f}")
        print(f"- Average CLV: ${segment_data['CLV']:,.2f}")
        print(f"- Revenue Contribution: {segment_data['Revenue_Proportion']:.1f}%")
    
except Exception as e:
    print(f"Error in resource allocation analysis: {e}")'''))

    cells.append(nbformat.v4.new_markdown_cell('''### 5.5 Business Recommendations

Based on the analysis above, here are key recommendations for each business area:

1. **Inventory Management**:
   - Implement automated reorder points for top products
   - Adjust safety stock levels based on demand variability
   - Focus on optimizing stock levels for high-demand items

2. **Marketing Optimization**:
   - Develop targeted campaigns for each customer segment
   - Allocate marketing budget based on segment value
   - Create personalized offers for high-value customers

3. **Customer Retention**:
   - Implement early intervention for high-risk valuable customers
   - Develop retention programs based on risk levels
   - Create win-back campaigns for lost customers

4. **Resource Allocation**:
   - Prioritize resources for Platinum and Gold segments
   - Develop upgrade paths for Silver customers
   - Optimize service levels based on customer value'''))

    nb.cells = cells
    return nb

def save_notebook(notebook_path):
    """Save the notebook to the specified path"""
    try:
        nb = create_notebook()
        
        if Path(notebook_path).exists():
            backup_path = Path(notebook_path).parent / f"{Path(notebook_path).stem}_backup.ipynb"
            Path(notebook_path).rename(backup_path)
            print(f"Created backup at {backup_path}")
        
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
