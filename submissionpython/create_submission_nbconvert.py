import nbformat
import os
from nbconvert import PDFExporter
from nbconvert.preprocessors import ExecutePreprocessor
import markdown
from datetime import datetime

def create_submission():
    """Create submission files using nbconvert"""
    
    # First convert README to notebook
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Create a notebook for README
    nb = nbformat.v4.new_notebook()
    
    # Add title cell
    title_cell = nbformat.v4.new_markdown_cell("""# Customer Behavior Analysis Project
    
**Course**: IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers  
**Student Name**: Lalit Nayyar  
**Email ID**: lalitnayyar@gmail.com  
**Assignment**: Data-Driven Decision Making Analysis  
**Date**: May 4, 2025
    """)
    
    # Add README content cell
    readme_cell = nbformat.v4.new_markdown_cell(readme_content)
    
    nb.cells.extend([title_cell, readme_cell])
    
    # Save README notebook
    with open('00_README.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    # List of notebooks in order
    notebooks = [
        '00_README.ipynb',
        'LalitNayyarIIMKMod4_analysis_fin.ipynb',
        'LalitNayyarIIMKMod4_descriptive_analysis_fin.ipynb',
        'LalitNayyarIIMKMod4_diagnostic_analysis_fin.ipynb',
        'LalitNayyarIIMKMod4_predictive_analysis_fin.ipynb'
    ]
    
    # Convert each notebook to HTML
    for notebook in notebooks:
        if os.path.exists(notebook):
            os.system(f'jupyter nbconvert --to html {notebook}')
    
    # Create index.html that combines all HTML files
    html_content = ['<!DOCTYPE html><html><head><title>IIMK Module 4 Submission</title>',
                   '<style>body{font-family:Arial,sans-serif;margin:40px;}</style></head><body>']
    
    for notebook in notebooks:
        html_file = notebook.replace('.ipynb', '.html')
        if os.path.exists(html_file):
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract body content
                start = content.find('<body')
                end = content.find('</body>')
                if start > -1 and end > -1:
                    body_content = content[start:end+7]
                    html_content.append(f'<div class="notebook">{body_content}</div>')
                    html_content.append('<div style="page-break-after: always;"></div>')
    
    html_content.append('</body></html>')
    
    # Save combined HTML
    with open('LalitNayyar_IIMK_Module4_Submission.html', 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_content))
    
    # Convert combined HTML to PDF using nbconvert
    os.system('jupyter nbconvert --to pdf LalitNayyar_IIMK_Module4_Submission.html')
    
    print("Submission files created successfully!")
    print("1. Individual HTML files for each notebook")
    print("2. Combined submission in LalitNayyar_IIMK_Module4_Submission.pdf")

if __name__ == '__main__':
    create_submission()
