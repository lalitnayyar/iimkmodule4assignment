import nbformat
from nbconvert import HTMLExporter, PDFExporter
from nbconvert.preprocessors import ExecutePreprocessor
import markdown
import os
from datetime import datetime

def create_submission():
    """Create a professional submission document combining README and notebook outputs"""
    
    # HTML template with professional styling
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>IIMK Module 4 Submission - Lalit Nayyar</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            .header {
                text-align: center;
                margin-bottom: 40px;
                padding: 30px;
                background: #f8f9fa;
                border-radius: 8px;
            }
            .section {
                margin-bottom: 40px;
                padding: 20px;
                background: white;
                border: 1px solid #eee;
                border-radius: 8px;
            }
            h1 { color: #2c3e50; font-size: 2.5em; margin-bottom: 20px; }
            h2 { color: #34495e; font-size: 2em; border-bottom: 2px solid #eee; padding-bottom: 10px; }
            h3 { color: #7f8c8d; font-size: 1.5em; }
            code { background: #f8f9fa; padding: 2px 5px; border-radius: 3px; }
            pre { background: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto; }
            img { max-width: 100%; height: auto; margin: 20px 0; border-radius: 5px; }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }
            th, td {
                padding: 12px;
                border: 1px solid #ddd;
                text-align: left;
            }
            th { background: #f8f9fa; }
            .page-break { page-break-after: always; }
            .notebook-title {
                background: #2c3e50;
                color: white;
                padding: 15px;
                margin: 30px 0;
                border-radius: 5px;
            }
            .output_png img {
                display: block;
                margin: 20px auto;
                max-width: 800px;
            }
            @media print {
                body { margin: 25mm; }
                .page-break { page-break-after: always; }
                pre { white-space: pre-wrap; }
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
            <p><strong>Date:</strong> May 5, 2025</p>
        </div>
    '''
    
    # Read README content
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            readme_content = f.read()
            html_content = html_template
            html_content += f'<div class="section"><h2>Project Documentation</h2>{markdown.markdown(readme_content)}</div>'
            html_content += '<div class="page-break"></div>'
    except Exception as e:
        print(f"Error reading README: {e}")
        return
    
    # Process notebooks
    notebooks = [
        'LalitNayyarIIMKMod4_analysis_fin.ipynb',
        'LalitNayyarIIMKMod4_descriptive_analysis_fin.ipynb',
        'LalitNayyarIIMKMod4_diagnostic_analysis_fin.ipynb',
        'LalitNayyarIIMKMod4_predictive_analysis_fin.ipynb'
    ]
    
    # HTML exporter setup
    html_exporter = HTMLExporter()
    html_exporter.exclude_input_prompt = True
    html_exporter.exclude_output_prompt = True
    
    for notebook_file in notebooks:
        try:
            if os.path.exists(notebook_file):
                print(f"Processing {notebook_file}...")
                
                # Read and execute notebook
                with open(notebook_file, 'r', encoding='utf-8') as f:
                    nb = nbformat.read(f, as_version=4)
                
                # Convert to HTML
                (body, resources) = html_exporter.from_notebook_node(nb)
                
                # Add to main HTML
                html_content += f'<div class="section"><div class="notebook-title"><h2>{notebook_file}</h2></div>'
                html_content += body
                html_content += '</div><div class="page-break"></div>'
            else:
                print(f"Warning: {notebook_file} not found")
                
        except Exception as e:
            print(f"Error processing {notebook_file}: {e}")
    
    # Close HTML
    html_content += '</body></html>'
    
    # Save HTML
    output_html = 'LalitNayyar_IIMK_Module4_Submission.html'
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\nSubmission HTML created: {output_html}")
    print("\nTo create the final PDF:")
    print("1. Open the HTML file in Chrome")
    print("2. Press Ctrl+P (or Command+P)")
    print("3. Set Destination to 'Save as PDF'")
    print("4. Enable 'Background graphics'")
    print("5. Set margins to 'Default'")
    print("6. Save as 'LalitNayyar_IIMK_Module4_Submission.pdf'")

if __name__ == '__main__':
    create_submission()
