import nbformat
from nbconvert import HTMLExporter
import markdown
import os
from datetime import datetime

def create_professional_submission():
    """Create a professional submission with emojis and elegant formatting"""
    
    # Professional color scheme
    colors = {
        'primary': '#1976D2',      # Professional blue
        'secondary': '#424242',    # Dark gray
        'accent': '#2E7D32',       # Forest green
        'success': '#43A047',      # Green
        'warning': '#FDD835',      # Yellow
        'error': '#E53935',        # Red
        'background': '#F5F5F5',   # Light gray
        'text': '#212121'          # Near black
    }
    
    html_template = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>IIMK Module 4 Submission - Lalit Nayyar</title>
        <style>
            body {{
                font-family: 'Segoe UI', Arial, sans-serif;
                line-height: 1.6;
                color: {colors['text']};
                max-width: 1100px;
                margin: 0 auto;
                padding: 20px;
                background: white;
            }}
            .header {{
                text-align: center;
                margin-bottom: 40px;
                padding: 40px;
                background: linear-gradient(135deg, {colors['primary']}, #1565C0);
                color: white;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            .section {{
                margin: 30px 0;
                padding: 25px;
                background: white;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            .emoji-header {{
                display: flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 20px;
            }}
            .emoji {{
                font-size: 1.5em;
                margin-right: 8px;
            }}
            h1 {{ 
                color: white;
                font-size: 2.5em;
                margin-bottom: 20px;
            }}
            h2 {{ 
                color: {colors['primary']};
                font-size: 2em;
                border-bottom: 2px solid {colors['primary']};
                padding-bottom: 10px;
            }}
            h3 {{ 
                color: {colors['secondary']};
                font-size: 1.5em;
            }}
            code {{ 
                background: {colors['background']};
                padding: 3px 6px;
                border-radius: 4px;
                font-family: 'Consolas', monospace;
            }}
            pre {{ 
                background: {colors['background']};
                padding: 15px;
                border-radius: 6px;
                overflow-x: auto;
                border-left: 4px solid {colors['primary']};
            }}
            img {{ 
                max-width: 100%;
                height: auto;
                margin: 20px auto;
                border-radius: 6px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                display: block;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }}
            th, td {{
                padding: 12px;
                border: 1px solid #e0e0e0;
                text-align: left;
            }}
            th {{ 
                background: {colors['primary']};
                color: white;
            }}
            tr:nth-child(even) {{
                background: {colors['background']};
            }}
            .page-break {{ 
                page-break-after: always;
                height: 0;
                margin: 0;
                border: 0;
            }}
            .notebook-title {{
                background: linear-gradient(135deg, {colors['primary']}, #1565C0);
                color: white;
                padding: 20px;
                margin: 30px 0;
                border-radius: 6px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            .output_png img {{
                display: block;
                margin: 25px auto;
                max-width: 850px;
            }}
            .key-point {{
                background: #E3F2FD;
                padding: 15px;
                border-radius: 6px;
                margin: 15px 0;
                border-left: 4px solid {colors['primary']};
            }}
            @media print {{
                body {{ margin: 20mm; }}
                .page-break {{ page-break-after: always; }}
                pre {{ white-space: pre-wrap; }}
                .header, .notebook-title {{
                    -webkit-print-color-adjust: exact;
                    print-color-adjust: exact;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📊 Customer Behavior Analysis Project</h1>
            <h2 style="color: white; border: none;">🎯 Data-Driven Decision Making Analysis</h2>
            <p><strong>📚 Course:</strong> IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers</p>
            <p><strong>👨‍🎓 Student Name:</strong> Lalit Nayyar</p>
            <p><strong>📧 Email ID:</strong> lalitnayyar@gmail.com</p>
            <p><strong>📅 Date:</strong> May 5, 2025</p>
        </div>
    '''
    
    try:
        # Add README content with emojis
        with open('README.md', 'r', encoding='utf-8') as f:
            readme_content = f.read()
            
            # Add emojis to section headers
            readme_content = readme_content.replace('# Project Overview', '# 📋 Project Overview')
            readme_content = readme_content.replace('## Dataset Description', '## 📊 Dataset Description')
            readme_content = readme_content.replace('## Analysis Structure', '## 🔍 Analysis Structure')
            readme_content = readme_content.replace('## Key Features', '## 🌟 Key Features')
            readme_content = readme_content.replace('## Learning Outcomes', '## 🎯 Learning Outcomes')
            readme_content = readme_content.replace('## Assessment Criteria', '## 📝 Assessment Criteria')
            
            html_content = html_template
            html_content += f'<div class="section"><h2>📑 Project Documentation</h2>{markdown.markdown(readme_content)}</div>'
            html_content += '<div class="page-break"></div>'
        
        # Process notebooks
        notebooks = [
            ('LalitNayyarIIMKMod4_analysis_fin.ipynb', '🔍'),
            ('LalitNayyarIIMKMod4_descriptive_analysis_fin.ipynb', '📊'),
            ('LalitNayyarIIMKMod4_predictive_analysis_fin.ipynb', '🔮')
        ]
        
        # Configure HTML exporter
        html_exporter = HTMLExporter()
        html_exporter.exclude_input_prompt = True
        html_exporter.exclude_output_prompt = True
        
        # Process each notebook
        for notebook_file, emoji in notebooks:
            if os.path.exists(notebook_file):
                print(f"Processing {notebook_file}...")
                
                # Read notebook
                with open(notebook_file, 'r', encoding='utf-8') as f:
                    nb = nbformat.read(f, as_version=4)
                
                # Update visualization style
                for cell in nb.cells:
                    if cell.cell_type == 'code' and 'plt' in str(cell.source):
                        cell.source = cell.source.replace("plt.style.use('default')", """
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = [12, 6]
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
    '#1976D2',  # Professional blue
    '#2E7D32',  # Forest green
    '#C62828',  # Deep red
    '#7B1FA2',  # Purple
    '#F57C00',  # Orange
    '#0097A7'   # Teal
])
""")
                
                # Convert to HTML
                (body, resources) = html_exporter.from_notebook_node(nb)
                
                # Add to main HTML with emoji
                html_content += f'<div class="section"><div class="notebook-title"><h2>{emoji} {notebook_file}</h2></div>'
                html_content += body
                html_content += '</div><div class="page-break"></div>'
            else:
                print(f"Warning: {notebook_file} not found")
        
        # Close HTML
        html_content += '</body></html>'
        
        # Save HTML
        output_file = 'LalitNayyar_IIMK_Module4_Submission.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"\nProfessional submission with emojis created: {output_file}")
        print("\nTo create the final PDF:")
        print("1. Open the HTML file in Chrome")
        print("2. Press Ctrl+P (or Command+P)")
        print("3. Set Destination to 'Save as PDF'")
        print("4. Enable 'Background graphics'")
        print("5. Set margins to 'Default'")
        print("6. Save as 'LalitNayyar_IIMK_Module4_Submission.pdf'")
        
    except Exception as e:
        print(f"Error creating submission: {e}")

if __name__ == '__main__':
    create_professional_submission()
