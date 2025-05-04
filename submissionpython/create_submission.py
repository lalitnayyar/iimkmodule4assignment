import nbformat
import markdown
from weasyprint import HTML, CSS
from datetime import datetime
import os

def create_submission_pdf():
    """Create a comprehensive PDF submission document."""
    
    # Create HTML content
    html_content = []
    
    # Add header
    html_content.append("""
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #2c3e50; text-align: center; }
            h2 { color: #34495e; margin-top: 30px; }
            h3 { color: #7f8c8d; }
            pre { background-color: #f8f9fa; padding: 10px; border-radius: 5px; }
            img { max-width: 100%; height: auto; margin: 20px 0; }
            .header { text-align: center; margin-bottom: 40px; }
            .page-break { page-break-after: always; }
            .code-output { background-color: #f8f9fa; padding: 15px; margin: 10px 0; }
        </style>
    </head>
    <body>
    """)
    
    # Add title page
    html_content.append("""
    <div class="header">
        <h1>Customer Behavior Analysis Project</h1>
        <h2>Data-Driven Decision Making Analysis</h2>
        <p><strong>Course:</strong> IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers</p>
        <p><strong>Student Name:</strong> Lalit Nayyar</p>
        <p><strong>Email ID:</strong> lalitnayyar@gmail.com</p>
        <p><strong>Date:</strong> May 4, 2025</p>
    </div>
    <div class="page-break"></div>
    """)
    
    # Add README content
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
        html_content.append(markdown.markdown(readme_content))
    
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
                
                html_content.append(f'<h2>{notebook_file}</h2>')
                
                for cell in nb.cells:
                    if cell.cell_type == 'markdown':
                        html_content.append(markdown.markdown(cell.source))
                    elif cell.cell_type == 'code':
                        # Add code cell
                        html_content.append('<div class="code-output">')
                        html_content.append(f'<pre><code>{cell.source}</code></pre>')
                        
                        # Add output if present
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
    
    # Create PDF
    html = HTML(string=''.join(html_content))
    css = CSS(string='''
        @page { margin: 1cm; }
        img { max-width: 100%; }
    ''')
    html.write_pdf('LalitNayyar_IIMK_Module4_Submission.pdf', stylesheets=[css])

if __name__ == '__main__':
    create_submission_pdf()
