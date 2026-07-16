# Project: Exploratory Breast Cancer Diagnostic Data Analysis in Python 
# Author: Akash Bhardwaj 
# Purpose: Perform basic data-quality checks on the processed dataset 
 
from pathlib import Path 
import pandas as pd 
 
# Define project-relative paths 
input_file = Path("data_processed") / "breast_cancer_dataframe.csv" 
output_file = Path("outputs") / "tables" / "python_data_quality_summary.csv" 
 
# Check that the input file exists 
if not input_file.exists(): 
   raise FileNotFoundError( 
       f"Input file not found: {input_file}" 
   ) 
 
# Load processed data 
df = pd.read_csv(input_file) 
 
# Calculate quality-control measures 
qc_summary = pd.DataFrame({ 
   "metric": [ 
       "number_of_rows", 
       "number_of_columns", 
       "total_missing_values", 
       "duplicate_rows", 
       "benign_samples", 
       "malignant_samples" 
   ], 
   "value": [ 
       df.shape[0], 
       df.shape[1],
       int(df.isna().sum().sum()), 
       int(df.duplicated().sum()), 
       int((df["diagnosis_label"] == "Benign").sum()), 
       int((df["diagnosis_label"] == "Malignant").sum()) 
   ] 
}) 
 
# Create output folder if required 
output_file.parent.mkdir(parents=True, exist_ok=True) 
 
# Save QC summary 
qc_summary.to_csv(output_file, index=False) 
 
# Print results 
print("Python Data Quality Summary") 
print("===========================") 
print(qc_summary.to_string(index=False)) 
print() 
print(f"QC summary saved to: {output_file}") 
