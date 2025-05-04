# Customer Behavior Analysis Project

**Course**: IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers  
**Student Name**: Lalit Nayyar  
**Email ID**: lalitnayyar@gmail.com  
**Assignment**: Data-Driven Decision Making Analysis

## Project Overview
This project demonstrates the application of data-driven decision-making concepts to analyze customer behavior in an online retail platform. The analysis progresses through multiple stages of analytics maturity, from descriptive to predictive, providing actionable insights for business decisions.

## Dataset Description
- **Source**: Online Retail Dataset
- **Type**: Structured transactional data
- **Time Period**: 2010-2011
- **Key Features**: 
  - InvoiceNo: Transaction identifier
  - StockCode: Product code
  - Description: Product name
  - Quantity: Items per transaction
  - InvoiceDate: Transaction timestamp
  - UnitPrice: Price per unit
  - CustomerID: Unique customer identifier
  - Country: Customer's country

## Analysis Structure

### 1. Data Preprocessing Notebook (`LalitNayyarIIMKMod4_analysis_fin.ipynb`)
**Learning Outcome**: Data Description, Preprocessing and Cleaning (4 points)
- **Features**:
  - Comprehensive data quality assessment
  - Missing value analysis and handling
  - Duplicate detection and removal
  - Data type validation and conversion
  - Outlier detection and treatment
- **Key Functions**:
  - `clean_data()`: Complete data cleaning pipeline
  - `validate_data_types()`: Data type verification
  - `handle_outliers()`: Outlier treatment
- **Usage Guide**:
  1. Load the raw dataset
  2. Execute data quality checks
  3. Apply cleaning functions
  4. Validate cleaned dataset
  5. Export processed data for analysis

### 2. Descriptive Analytics Notebook (`LalitNayyarIIMKMod4_descriptive_analysis_fin.ipynb`)
**Learning Outcome**: Descriptive Analytics (2 points)
- **Analysis Components**:
  - Purchase patterns analysis
  - Product popularity metrics
  - Customer segmentation
  - Sales trend analysis
- **Visualizations**:
  - Time series plots of sales trends
  - Product performance heatmaps
  - Customer segment distributions
  - Geographic sales analysis
- **Key Insights**:
  - Top-performing products
  - Peak sales periods
  - Customer buying patterns
  - Regional performance metrics

### 3. Diagnostic Analytics Notebook (`LalitNayyarIIMKMod4_diagnostic_analysis_fin.ipynb`)
**Learning Outcome**: Diagnostic Analytics (2 points)
- **Analysis Methods**:
  - Correlation analysis
  - Factor analysis
  - Root cause investigation
  - Pattern attribution
- **Key Components**:
  - Price sensitivity analysis
  - Customer churn factors
  - Seasonal impact assessment
  - Product affinity analysis
- **Business Insights**:
  - Churn drivers identification
  - Sales pattern explanations
  - Customer behavior factors
  - Performance variance analysis

### 4. Predictive Analytics Notebook (`LalitNayyarIIMKMod4_predictive_analysis_fin.ipynb`)
**Learning Outcome**: Predictive Analytics (2 points)
- **Models Implemented**:
  - Customer Lifetime Value prediction
  - Purchase frequency forecasting
  - Product demand prediction
  - Churn risk assessment
- **Technical Components**:
  - Model selection justification
  - Feature engineering process
  - Performance metrics analysis
  - Prediction reliability assessment
- **Business Applications**:
  - Revenue forecasting
  - Inventory optimization
  - Customer retention strategies
  - Targeted marketing recommendations

## Execution Instructions

### Environment Setup
```python
# Required packages
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### Running the Analysis
1. **Data Preprocessing**:
   - Open `LalitNayyar_Data_Preprocessing.ipynb`
   - Run all cells sequentially
   - Verify cleaned data output

2. **Descriptive Analysis**:
   - Open `LalitNayyar_Descriptive_Analytics.ipynb`
   - Ensure cleaned data is available
   - Execute all cells
   - Review visualization outputs

3. **Diagnostic Analysis**:
   - Open `LalitNayyar_Diagnostic_Analytics.ipynb`
   - Run correlation analyses
   - Review factor analysis results
   - Generate insight reports

4. **Predictive Analysis**:
   - Open `LalitNayyar_Predictive_Analytics.ipynb`
   - Execute model training
   - Validate predictions
   - Review business recommendations

## Submission Components
1. **Notebooks**:
   - All four analysis notebooks
   - Properly documented with markdown
   - Clear code comments
   - Complete output cells

2. **Documentation**:
   - This README.md file
   - Analysis methodology explanation
   - Results interpretation
   - Business recommendations

3. **Data Files**:
   - Original dataset
   - Cleaned dataset
   - Intermediate analysis outputs

4. **Presentation**:
   - Key findings summary
   - Visualization highlights
   - Actionable insights
   - Strategic recommendations

## Assessment Criteria Alignment
- **Data Processing (4 pts)**: Comprehensive data cleaning and preparation
- **Descriptive Analytics (2 pts)**: Thorough pattern analysis and visualization
- **Diagnostic Analytics (2 pts)**: In-depth causation analysis
- **Predictive Analytics (2 pts)**: Advanced modeling and forecasting

## Author's Note
This analysis demonstrates the practical application of data science concepts to real-world business problems, providing actionable insights for decision-making.
