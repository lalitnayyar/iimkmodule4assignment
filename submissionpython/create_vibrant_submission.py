import nbformat
from nbconvert import HTMLExporter
import markdown
import os
from datetime import datetime

def create_vibrant_submission():
    """Create a professional submission with vibrant colors and enhanced visuals"""
    
    # HTML template with vibrant styling
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>IIMK Module 4 Submission - Lalit Nayyar</title>
        <style>
            :root {
                --primary-color: #2962ff;
                --secondary-color: #0039cb;
                --accent-color: #768fff;
                --success-color: #00c853;
                --warning-color: #ffd600;
                --error-color: #d50000;
                --text-primary: #212121;
                --text-secondary: #757575;
                --background-light: #f5f5f5;
            }
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                line-height: 1.6;
                color: var(--text-primary);
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background: #ffffff;
            }
            .header {
                text-align: center;
                margin-bottom: 40px;
                padding: 40px;
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                color: white;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }
            .header h1 { 
                font-size: 2.8em; 
                margin-bottom: 20px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }
            .header h2 { 
                font-size: 2em;
                color: var(--accent-color);
                border: none;
            }
            .section {
                margin-bottom: 40px;
                padding: 30px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                border: 1px solid #e0e0e0;
            }
            h1 { color: var(--primary-color); font-size: 2.5em; margin-bottom: 20px; }
            h2 { 
                color: var(--secondary-color); 
                font-size: 2em; 
                border-bottom: 3px solid var(--accent-color);
                padding-bottom: 10px;
                margin-top: 30px;
            }
            h3 { color: var(--text-secondary); font-size: 1.5em; }
            code { 
                background: var(--background-light); 
                padding: 3px 6px; 
                border-radius: 4px;
                color: var(--primary-color);
            }
            pre { 
                background: var(--background-light); 
                padding: 20px; 
                border-radius: 8px; 
                overflow-x: auto;
                border-left: 4px solid var(--primary-color);
            }
            img { 
                max-width: 100%; 
                height: auto; 
                margin: 20px auto;
                border-radius: 8px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.1);
                display: block;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                box-shadow: 0 1px 4px rgba(0,0,0,0.05);
            }
            th, td {
                padding: 15px;
                border: 1px solid #e0e0e0;
                text-align: left;
            }
            th { 
                background: var(--primary-color);
                color: white;
            }
            tr:nth-child(even) {
                background: var(--background-light);
            }
            .page-break { page-break-after: always; }
            .notebook-title {
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                color: white;
                padding: 20px;
                margin: 30px 0;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            .output_png img {
                display: block;
                margin: 30px auto;
                max-width: 900px;
                border: 1px solid #e0e0e0;
            }
            .dataframe {
                font-size: 0.9em;
                margin: 20px 0;
                width: 100%;
            }
            .dataframe th {
                background: var(--primary-color);
                color: white;
                font-weight: 600;
            }
            .dataframe tr:hover {
                background: #f0f0f0;
            }
            .cell {
                margin: 20px 0;
                padding: 15px;
                border-radius: 8px;
            }
            .text_cell {
                background: white;
            }
            .code_cell {
                background: var(--background-light);
            }
            @media print {
                body { margin: 25mm; }
                .page-break { page-break-after: always; }
                pre { white-space: pre-wrap; }
                .header {
                    -webkit-print-color-adjust: exact;
                    print-color-adjust: exact;
                }
                img {
                    max-width: 800px;
                    page-break-inside: avoid;
                }
                table {
                    page-break-inside: avoid;
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
    
    # HTML exporter setup with custom template
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
                
                # Update visualization style for notebook cells
                for cell in nb.cells:
                    if cell.cell_type == 'code' and 'matplotlib' in str(cell.source):
                        cell.source = cell.source.replace("plt.style.use('default')", """
plt.style.use('default')
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#2962ff', '#00c853', '#ffd600', '#d50000', '#6200ea', '#00bfa5'])
plt.rcParams['figure.figsize'] = [12, 6]
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
""")
                
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
    
    print(f"\nVibrant submission HTML created: {output_html}")
    print("\nTo create the final PDF:")
    print("1. Open the HTML file in Chrome")
    print("2. Press Ctrl+P (or Command+P)")
    print("3. Set Destination to 'Save as PDF'")
    print("4. Enable 'Background graphics'")
    print("5. Set margins to 'Default'")
    print("6. Save as 'LalitNayyar_IIMK_Module4_Submission.pdf'")

if __name__ == '__main__':
    create_vibrant_submission()
