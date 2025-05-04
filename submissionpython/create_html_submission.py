import nbformat
import markdown
from datetime import datetime
import os

def create_html_submission():
    """Create a nicely formatted HTML submission"""
    
    # Start HTML content
    html_content = ['''<!DOCTYPE html>
<html>
<head>
    <title>IIMK Module 4 Submission - Lalit Nayyar</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 40px;
            line-height: 1.6;
            color: #333;
        }
        .header { 
            text-align: center; 
            margin-bottom: 40px;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 5px;
        }
        h1 { color: #2c3e50; }
        h2 { 
            color: #34495e;
            margin-top: 30px;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }
        h3 { color: #7f8c8d; }
        pre { 
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        img { 
            max-width: 100%;
            height: auto;
            margin: 20px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .page-break { 
            page-break-after: always;
            height: 0;
            margin: 0;
            border: 0;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f8f9fa;
        }
        .notebook-section {
            margin-bottom: 40px;
            border: 1px solid #eee;
            padding: 20px;
            border-radius: 5px;
        }
        @media print {
            .page-break {
                page-break-after: always;
            }
            body {
                margin: 20mm;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Customer Behavior Analysis Project</h1>
        <h2>Data-Driven Decision Making Analysis</h2>
        <p><strong>Course:</strong> IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers</p>
        <p><strong>Student Name:</strong> Lalit Nayyar</p>
        <p><strong>Email ID:</strong> lalitnayyar@gmail.com</p>
        <p><strong>Date:</strong> May 4, 2025</p>
    </div>
    <div class="page-break"></div>
    ''']
    
    # Add README content
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
        html_content.append('<div class="notebook-section">')
        html_content.append('<h2>Project Documentation</h2>')
        html_content.append(markdown.markdown(readme_content))
        html_content.append('</div>')
        html_content.append('<div class="page-break"></div>')
    
    # Process each notebook
    notebooks = [
        'LalitNayyarIIMKMod4_analysis_fin.ipynb',
        'LalitNayyarIIMKMod4_descriptive_analysis_fin.ipynb',
        'LalitNayyarIIMKMod4_diagnostic_analysis_fin.ipynb',
        'LalitNayyarIIMKMod4_predictive_analysis_fin.ipynb'
    ]
    
    for notebook_file in notebooks:
        try:
            with open(notebook_file, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
                
                html_content.append(f'<div class="notebook-section">')
                html_content.append(f'<h2>{notebook_file}</h2>')
                
                for cell in nb.cells:
                    if cell.cell_type == 'markdown':
                        html_content.append(markdown.markdown(cell.source))
                    elif cell.cell_type == 'code':
                        html_content.append('<pre><code>')
                        html_content.append(cell.source)
                        html_content.append('</code></pre>')
                        
                        if hasattr(cell, 'outputs'):
                            for output in cell.outputs:
                                if 'text' in output:
                                    html_content.append(f'<pre>{output.text}</pre>')
                                elif 'data' in output:
                                    if 'image/png' in output.data:
                                        img_data = output.data['image/png']
                                        html_content.append(f'<img src="data:image/png;base64,{img_data}">')
                                    elif 'text/html' in output.data:
                                        html_content.append(output.data['text/html'])
                
                html_content.append('</div>')
                html_content.append('<div class="page-break"></div>')
                
        except Exception as e:
            print(f"Error processing {notebook_file}: {e}")
    
    # Close HTML
    html_content.append('</body></html>')
    
    # Save the HTML file
    with open('LalitNayyar_IIMK_Module4_Submission.html', 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_content))
    
    print("Submission HTML created successfully!")
    print("\nTo create the final PDF:")
    print("1. Open LalitNayyar_IIMK_Module4_Submission.html in Chrome")
    print("2. Press Ctrl+P or Command+P")
    print("3. Set Destination to 'Save as PDF'")
    print("4. Set Layout to 'Portrait'")
    print("5. Enable 'Background graphics'")
    print("6. Click 'Save' and name it 'LalitNayyar_IIMK_Module4_Submission.pdf'")

if __name__ == '__main__':
    create_html_submission()
