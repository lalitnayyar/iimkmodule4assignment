import nbformat
from nbconvert import HTMLExporter
import markdown
import os
from datetime import datetime

def create_high_contrast_submission():
    """Create a submission with improved visibility and readability"""
    
    # High contrast color scheme
    colors = {
        'primary': '#0D47A1',      # Darker blue for better contrast
        'secondary': '#1B1B1B',    # Near black for text
        'accent': '#1B5E20',       # Dark green
        'background': '#FFFFFF',   # Pure white background
        'text': '#000000',        # Pure black text
        'link': '#0D47A1',        # Dark blue for links
        'header_bg': '#1565C0',   # Bright blue for headers
        'code_bg': '#F5F5F5'      # Light gray for code
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
                line-height: 1.8;
                color: {colors['text']};
                max-width: 1200px;
                margin: 0 auto;
                padding: 30px;
                background: {colors['background']};
                font-size: 16px;
            }}
            .header {{
                text-align: center;
                margin-bottom: 50px;
                padding: 40px;
                background: {colors['header_bg']};
                color: white;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            }}
            .section {{
                margin: 40px 0;
                padding: 30px;
                background: white;
                border-radius: 10px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                border: 1px solid #E0E0E0;
            }}
            h1 {{ 
                color: white;
                font-size: 2.8em;
                margin-bottom: 25px;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
                letter-spacing: 0.5px;
            }}
            h2 {{ 
                color: {colors['primary']};
                font-size: 2.2em;
                border-bottom: 3px solid {colors['primary']};
                padding-bottom: 15px;
                margin-top: 40px;
                margin-bottom: 25px;
                letter-spacing: 0.3px;
            }}
            h3 {{ 
                color: {colors['secondary']};
                font-size: 1.8em;
                margin-top: 30px;
                margin-bottom: 20px;
            }}
            p {{
                font-size: 1.1em;
                line-height: 1.8;
                margin-bottom: 1.2em;
            }}
            code {{ 
                background: {colors['code_bg']};
                padding: 4px 8px;
                border-radius: 4px;
                font-family: 'Consolas', monospace;
                font-size: 1.1em;
                color: #000000;
            }}
            pre {{ 
                background: {colors['code_bg']};
                padding: 20px;
                border-radius: 8px;
                overflow-x: auto;
                border-left: 5px solid {colors['primary']};
                margin: 25px 0;
                font-size: 1.1em;
                line-height: 1.6;
            }}
            img {{ 
                max-width: 100%;
                height: auto;
                margin: 30px auto;
                border-radius: 8px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.1);
                display: block;
                border: 1px solid #E0E0E0;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 25px 0;
                font-size: 1.1em;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            th, td {{
                padding: 15px;
                border: 1px solid #D0D0D0;
                text-align: left;
            }}
            th {{ 
                background: {colors['primary']};
                color: white;
                font-weight: 600;
            }}
            tr:nth-child(even) {{
                background: #F8F9FA;
            }}
            tr:hover {{
                background: #F0F0F0;
            }}
            .page-break {{ 
                page-break-after: always;
                height: 0;
                margin: 0;
                border: 0;
            }}
            .notebook-title {{
                background: {colors['primary']};
                color: white;
                padding: 25px;
                margin: 40px 0;
                border-radius: 8px;
                font-size: 1.4em;
                box-shadow: 0 2px 6px rgba(0,0,0,0.2);
            }}
            .output_png img {{
                display: block;
                margin: 35px auto;
                max-width: 1000px;
            }}
            .key-point {{
                background: #E3F2FD;
                padding: 20px;
                border-radius: 8px;
                margin: 20px 0;
                border-left: 5px solid {colors['primary']};
                font-size: 1.1em;
            }}
            .emoji {{
                font-size: 1.4em;
            }}
            .dataframe {{
                font-size: 1.1em;
                margin: 25px 0;
            }}
            .dataframe th {{
                background: {colors['primary']};
                color: white;
                font-weight: 600;
                padding: 12px;
            }}
            .output_text {{
                font-size: 1.1em;
                line-height: 1.6;
                margin: 20px 0;
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
                }}
                .header, .notebook-title {{
                    -webkit-print-color-adjust: exact;
                    print-color-adjust: exact;
                }}
                img {{
                    max-width: 800px;
                    page-break-inside: avoid;
                }}
                h2, h3 {{
                    page-break-after: avoid;
                }}
                table {{
                    page-break-inside: avoid;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📊 Customer Behavior Analysis Project</h1>
            <h2 style="color: white; border: none; font-size: 2em;">🎯 Data-Driven Decision Making Analysis</h2>
            <p style="font-size: 1.2em; margin-top: 20px;"><strong>📚 Course:</strong> IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers</p>
            <p style="font-size: 1.2em;"><strong>👨‍🎓 Student Name:</strong> Lalit Nayyar</p>
            <p style="font-size: 1.2em;"><strong>📧 Email ID:</strong> lalitnayyar@gmail.com</p>
            <p style="font-size: 1.2em;"><strong>📅 Date:</strong> May 5, 2025</p>
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
                
                # Update visualization style for better visibility
                for cell in nb.cells:
                    if cell.cell_type == 'code' and 'plt' in str(cell.source):
                        cell.source = cell.source.replace("plt.style.use('default')", """
plt.style.use('seaborn-v0_8-bright')
plt.rcParams['figure.figsize'] = [14, 8]
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['lines.linewidth'] = 2.5
plt.rcParams['font.size'] = 12
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
    '#0D47A1',  # Dark blue
    '#1B5E20',  # Dark green
    '#B71C1C',  # Dark red
    '#4A148C',  # Dark purple
    '#E65100',  # Dark orange
    '#01579B'   # Dark teal
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
        
        print(f"\nHigh contrast submission created: {output_file}")
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
    create_high_contrast_submission()
