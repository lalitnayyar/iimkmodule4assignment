# Customer Behavior Analysis Project

**Course**: IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers  
**Student Name**: Lalit Nayyar  
**Email ID**: lalitnayyar@gmail.com  
**Assignment Name**: Week 4: Required Assignment 4.1

## Project Overview
This project analyzes customer behavior data from an online retail platform using various analytical approaches. The analysis is structured in three comprehensive notebooks, each focusing on different aspects of customer behavior analysis.

## Notebooks Description

### 1. `LalitNayyarIIMKMod4_analysis.ipynb`
**Initial Data Analysis and Preparation**
- **Features**:
  - Data loading and inspection
  - Missing value analysis and handling
  - Data cleaning and preprocessing
  - Feature engineering (TotalAmount calculation)
  - Basic statistical analysis
- **Key Functions**:
  - `clean_data()`: Comprehensive data cleaning function
  - Data type conversion and validation
  - Outlier detection and handling
- **Usage Guide**:
  1. Run all imports in the first cell
  2. Execute data loading and inspection cells
  3. Review data quality metrics
  4. Run cleaning functions
  5. Verify cleaned dataset statistics

### 2. `LalitNayyarIIMKMod4_descriptive_analysis.ipynb`
**Descriptive Analytics and Pattern Recognition**
- **Features**:
  - Purchase frequency analysis
  - Product popularity metrics
  - Temporal purchase patterns
  - Customer spending analysis
  - Advanced visualizations
- **Key Analyses**:
  - Customer purchase frequency distribution
  - Top products by quantity and revenue
  - Monthly and daily sales trends
  - Customer spending patterns
- **Visualizations**:
  - Distribution plots
  - Time series analysis charts
  - Product performance bar charts
  - Customer segmentation plots
- **Usage Guide**:
  1. Ensure cleaned data is available
  2. Run frequency analysis section
  3. Execute product analysis cells
  4. Generate temporal pattern visualizations
  5. Review customer spending insights

### 3. `LalitNayyarIIMKMod4_predictive_analysis.ipynb`
**Predictive Modeling and Future Behavior Forecasting**
- **Features**:
  - Purchase frequency prediction
  - Customer Lifetime Value (CLV) modeling
  - Feature importance analysis
  - Model performance evaluation
- **Models Implemented**:
  - Random Forest Regressor for purchase prediction
  - CLV prediction model
  - Feature importance ranking
- **Key Functions**:
  - `create_customer_features()`: RFM feature engineering
  - `prepare_clv_features()`: CLV feature preparation
  - Model training and evaluation functions
- **Usage Guide**:
  1. Run feature engineering cells
  2. Execute model training sections
  3. Review model performance metrics
  4. Analyze feature importance results
  5. Generate predictions and insights

## Technical Requirements
- Python 3.8+
- Required packages:
  ```
  pandas>=1.3.0
  numpy>=1.20.0
  matplotlib>=3.4.0
  seaborn>=0.11.0
  scikit-learn>=1.0.0
  openpyxl>=3.0.7
  jupyter>=1.0.0
  ```

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/lalitnayyar/iimkmodule4assignment.git
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Place 'Online Retail.xlsx' dataset in the project directory
4. Run notebooks in sequence:
   - Start with analysis notebook
   - Proceed to descriptive analysis
   - Finally, run predictive analysis

## Data Requirements
- Input file: 'Online Retail.xlsx'
- Required columns:
  - InvoiceNo
  - StockCode
  - Description
  - Quantity
  - InvoiceDate
  - UnitPrice
  - CustomerID
  - Country

## Key Insights and Outputs
1. **Customer Behavior Patterns**:
   - Purchase frequency distributions
   - Customer value segmentation
   - Temporal buying patterns

2. **Product Performance**:
   - Top-selling products
   - Revenue contributors
   - Seasonal trends

3. **Predictive Insights**:
   - Future purchase likelihood
   - Customer lifetime value predictions
   - High-potential customer identification

## Troubleshooting
- Ensure all dependencies are correctly installed
- Verify dataset format matches requirements
- Check for sufficient memory for large dataset operations
- Run notebooks in specified sequence to maintain data flow

## Contributing
For any improvements or issues, please create a pull request or raise an issue in the repository.

## License
This project is part of academic coursework for IIMK's Professional Certificate program.
