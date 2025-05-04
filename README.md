# Customer Behavior Analysis Project

**Course**: IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers  
**Student Name**: Lalit Nayyar  
**Email ID**: lalitnayyar@gmail.com  
**Assignment Name**: Week 4: Required Assignment 4.1

## Project Overview
This project analyzes customer behavior data from an online retail platform using various analytical approaches. The analysis is structured in four comprehensive notebooks, each focusing on different aspects of customer behavior analysis.

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

### 3. `LalitNayyarIIMKMod4_behavior_diagnostic_analysis_final.ipynb`
**Diagnostic Analytics for Understanding Customer Behavior**
- **Features**:
  - Root cause analysis of customer patterns
  - Price-sales relationship analysis
  - Seasonal impact investigation
  - Customer loyalty factor analysis
  - Advanced correlation studies
- **Key Analyses**:
  - Product performance drivers
  - Customer spending variations
  - Temporal pattern drivers
  - Customer loyalty factors
- **Analytical Methods**:
  - Correlation analysis
  - Statistical hypothesis testing
  - Seasonal decomposition
  - Customer segmentation analysis
- **Usage Guide**:
  1. Run correlation analyses for product performance
  2. Execute seasonal pattern investigation
  3. Analyze customer spending factors
  4. Review loyalty analysis results
  5. Generate comprehensive insights report

### 4. `LalitNayyarIIMKMod4_predictive_analysis.ipynb`
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
   cd iimkmodule4assignment
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Place 'Online Retail.xlsx' dataset in the project directory
4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## Running the Notebooks

### Step 1: Initial Data Analysis
**Notebook**: `LalitNayyarIIMKMod4_analysis.ipynb`
1. Open the notebook in Jupyter
2. Run all cells in sequence using `Shift + Enter` or using the "Run All" command
3. **Important Checkpoints**:
   - Verify data loading is successful
   - Check data cleaning results
   - Confirm feature engineering outputs
4. **Expected Outputs**:
   - Cleaned dataset saved as 'cleaned_retail_data.csv'
   - Initial statistics report
   - Data quality metrics

### Step 2: Descriptive Analysis
**Notebook**: `LalitNayyarIIMKMod4_descriptive_analysis.ipynb`
1. Ensure 'cleaned_retail_data.csv' exists from Step 1
2. Open and run all cells sequentially
3. **Important Checkpoints**:
   - Verify data loading from cleaned dataset
   - Check visualization outputs
   - Review statistical summaries
4. **Expected Outputs**:
   - Customer purchase patterns
   - Product analysis charts
   - Temporal trend visualizations

### Step 3: Diagnostic Analysis
**Notebook**: `LalitNayyarIIMKMod4_behavior_diagnostic_analysis_final.ipynb`
1. Requires completed descriptive analysis
2. Open and run cells in order
3. **Important Checkpoints**:
   - Confirm correlation analysis results
   - Verify hypothesis test outputs
   - Check seasonal decomposition plots
4. **Expected Outputs**:
   - Root cause analysis reports
   - Factor correlation matrices
   - Seasonal impact charts
   - Customer loyalty metrics

### Step 4: Predictive Analysis
**Notebook**: `LalitNayyarIIMKMod4_predictive_analysis.ipynb`
1. Requires all previous notebooks completed
2. Open and execute cells sequentially
3. **Important Checkpoints**:
   - Verify feature preparation
   - Check model training progress
   - Review performance metrics
4. **Expected Outputs**:
   - Trained prediction models
   - Performance evaluation reports
   - Feature importance rankings
   - Future predictions

## Troubleshooting Guide

### Common Issues and Solutions

1. **Data Loading Issues**
   ```python
   FileNotFoundError: Online Retail.xlsx not found
   ```
   - Solution: Ensure the dataset is in the project root directory
   - Check file name and case sensitivity

2. **Memory Issues**
   ```python
   MemoryError: Unable to allocate array
   ```
   - Solution: Restart kernel and clear output
   - Run notebooks on a machine with at least 8GB RAM

3. **Package Import Errors**
   ```python
   ModuleNotFoundError: No module named 'package_name'
   ```
   - Solution: Run `pip install -r requirements.txt`
   - Verify Python environment activation

4. **Visualization Errors**
   ```python
   RuntimeError: Invalid display value
   ```
   - Solution: Restart kernel
   - Run `%matplotlib inline` in a new cell

### Performance Optimization

1. **For Large Datasets**
   - Use data sampling for initial analysis
   - Implement chunked processing
   - Clear unused variables

2. **For Slow Visualizations**
   - Reduce plot resolution
   - Use efficient plot types
   - Limit data points in visualizations

## Quality Checks

After running each notebook, verify:
1. All cells executed successfully
2. No warning messages in outputs
3. All visualizations rendered properly
4. Expected files generated
5. Results match expected ranges

## Expected Runtime

- Analysis Notebook: ~5 minutes
- Descriptive Analysis: ~10 minutes
- Diagnostic Analysis: ~15 minutes
- Predictive Analysis: ~20 minutes

*Note: Runtimes may vary based on hardware specifications*

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

## Contributing
For any improvements or issues, please create a pull request or raise an issue in the repository.

## License
This project is part of academic coursework for IIMK's Professional Certificate program.
