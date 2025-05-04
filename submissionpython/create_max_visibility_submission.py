import nbformat
from nbconvert import HTMLExporter
import markdown
import os
from datetime import datetime

def create_max_visibility_submission():
    """Create a submission with maximum visibility and readability"""
    
    # Maximum contrast colors
    colors = {
        'primary': '#000000',      # Pure black for maximum contrast
        'secondary': '#1A237E',    # Very dark blue
        'header_bg': '#1565C0',    # Bright blue for headers
        'text': '#000000',         # Pure black text
        'link': '#0D47A1',         # Dark blue links
        'table_header': '#1565C0', # Bright blue table headers
        'code_bg': '#F8F9FA',      # Very light gray for code
        'border': '#000000'        # Black borders
    }
    
    html_template = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>IIMK Module 4 Submission - Lalit Nayyar</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap');
            
            body {{
                font-family: 'Open Sans', Arial, sans-serif;
                line-height: 2.0;
                color: {colors['text']};
                max-width: 1200px;
                margin: 0 auto;
                padding: 40px;
                background: #FFFFFF;
                font-size: 18px;
                font-weight: 400;
            }}
            .header {{
                text-align: center;
                margin-bottom: 60px;
                padding: 50px;
                background: {colors['header_bg']};
                color: white;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                border: 2px solid {colors['border']};
            }}
            .section {{
                margin: 50px 0;
                padding: 40px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                border: 1px solid {colors['border']};
            }}
            h1 {{ 
                color: white;
                font-size: 3.2em;
                margin-bottom: 30px;
                font-weight: 700;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }}
            h2 {{ 
                color: {colors['primary']};
                font-size: 2.4em;
                border-bottom: 3px solid {colors['primary']};
                padding-bottom: 15px;
                margin-top: 50px;
                margin-bottom: 30px;
                font-weight: 700;
            }}
            h3 {{ 
                color: {colors['secondary']};
                font-size: 2.0em;
                margin-top: 40px;
                margin-bottom: 25px;
                font-weight: 600;
            }}
            p {{
                font-size: 1.2em;
                line-height: 2.0;
                margin-bottom: 1.5em;
                color: {colors['text']};
            }}
            strong {{
                font-weight: 600;
                color: {colors['primary']};
            }}
            code {{ 
                background: {colors['code_bg']};
                padding: 5px 10px;
                border-radius: 5px;
                font-family: 'Consolas', monospace;
                font-size: 1.1em;
                color: #000000;
                border: 1px solid #CCCCCC;
            }}
            pre {{ 
                background: {colors['code_bg']};
                padding: 25px;
                border-radius: 10px;
                overflow-x: auto;
                border: 2px solid {colors['border']};
                margin: 30px 0;
                font-size: 1.1em;
                line-height: 1.8;
            }}
            img {{ 
                max-width: 100%;
                height: auto;
                margin: 40px auto;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                display: block;
                border: 2px solid {colors['border']};
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 30px 0;
                font-size: 1.1em;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                border: 2px solid {colors['border']};
            }}
            th, td {{
                padding: 18px;
                border: 1px solid {colors['border']};
                text-align: left;
            }}
            th {{ 
                background: {colors['table_header']};
                color: white;
                font-weight: 600;
                font-size: 1.2em;
            }}
            tr:nth-child(even) {{
                background: #F8F9FA;
            }}
            tr:hover {{
                background: #E3F2FD;
            }}
            .notebook-title {{
                background: {colors['secondary']};
                color: white;
                padding: 30px;
                margin: 40px 0;
                border-radius: 10px;
                font-size: 1.6em;
                box-shadow: 0 2px 8px rgba(0,0,0,0.2);
                border: 2px solid {colors['border']};
                font-weight: 600;
            }}
            .output_png img {{
                display: block;
                margin: 40px auto;
                max-width: 1100px;
                border: 2px solid {colors['border']};
            }}
            .key-point {{
                background: #E3F2FD;
                padding: 25px;
                border-radius: 10px;
                margin: 25px 0;
                border: 2px solid {colors['secondary']};
                font-size: 1.2em;
                color: {colors['text']};
            }}
            .emoji {{
                font-size: 1.6em;
            }}
            .dataframe {{
                font-size: 1.2em;
                margin: 30px 0;
                border: 2px solid {colors['border']};
            }}
            .dataframe th {{
                background: {colors['table_header']};
                color: white;
                font-weight: 600;
                padding: 15px;
                font-size: 1.1em;
            }}
            .output_text {{
                font-size: 1.2em;
                line-height: 1.8;
                margin: 25px 0;
                color: {colors['text']};
            }}
            ul, ol {{
                font-size: 1.2em;
                line-height: 2.0;
                margin: 20px 0;
                padding-left: 30px;
            }}
            li {{
                margin-bottom: 15px;
                color: {colors['text']};
            }}
            @media print {{
                body {{ 
                    margin: 25mm;
                    font-size: 12pt;
                }}
                .page-break {{ page-break-after: always; }}
                pre {{ 
                    white-space: pre-wrap;
                    font-size: 11pt;
                    border: 1px solid {colors['border']};
                }}
                .header, .notebook-title {{
                    -webkit-print-color-adjust: exact;
                    print-color-adjust: exact;
                }}
                img {{
                    max-width: 900px;
                    page-break-inside: avoid;
                }}
                h2, h3 {{
                    page-break-after: avoid;
                }}
                table {{
                    page-break-inside: avoid;
                }}
                p, li {{
                    page-break-inside: avoid;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📊 Customer Behavior Analysis Project</h1>
            <h2 style="color: white; border: none; font-size: 2.4em;">🎯 Data-Driven Decision Making Analysis</h2>
            <p style="font-size: 1.4em; margin-top: 25px; color: white;"><strong style="color: white;">📚 Course:</strong> IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers</p>
            <p style="font-size: 1.4em; color: white;"><strong style="color: white;">👨‍🎓 Student Name:</strong> Lalit Nayyar</p>
            <p style="font-size: 1.4em; color: white;"><strong style="color: white;">📧 Email ID:</strong> lalitnayyar@gmail.com</p>
            <p style="font-size: 1.4em; color: white;"><strong style="color: white;">📅 Date:</strong> May 5, 2025</p>
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
                
                # Update visualization style for maximum visibility
                for cell in nb.cells:
                    if cell.cell_type == 'code' and 'plt' in str(cell.source):
                        cell.source = cell.source.replace("plt.style.use('default')", """
plt.style.use('seaborn-v0_8-bright')
plt.rcParams['figure.figsize'] = [15, 8]
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['lines.linewidth'] = 2.5
plt.rcParams['font.size'] = 12
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
    '#000000',  # Black
    '#1565C0',  # Blue
    '#B71C1C',  # Red
    '#1B5E20',  # Green
    '#4A148C',  # Purple
    '#E65100'   # Orange
])
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'
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
        
        print(f"\nMaximum visibility submission created: {output_file}")
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
    create_max_visibility_submission()
