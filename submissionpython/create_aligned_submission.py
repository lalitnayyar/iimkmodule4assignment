import nbformat
from nbconvert import HTMLExporter
import markdown
import os
from datetime import datetime

def create_aligned_submission():
    """Create a submission with better alignment and no white fonts"""
    
    # Color scheme without white fonts
    colors = {
        'primary': '#1A237E',      # Dark blue
        'secondary': '#424242',    # Dark gray
        'header_bg': '#E8EAF6',    # Light blue background
        'text': '#000000',         # Black text
        'link': '#1A237E',         # Dark blue links
        'table_header': '#E8EAF6', # Light blue table headers
        'code_bg': '#F5F5F5',      # Light gray code background
        'border': '#1A237E',       # Dark blue borders
        'highlight': '#FFE0B2'     # Light orange highlight
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
                line-height: 1.8;
                color: {colors['text']};
                max-width: 1200px;
                margin: 0 auto;
                padding: 40px;
                background: #FFFFFF;
                font-size: 16px;
            }}
            .header {{
                text-align: left;
                margin-bottom: 50px;
                padding: 40px;
                background: {colors['header_bg']};
                color: {colors['primary']};
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                border: 2px solid {colors['border']};
            }}
            .section {{
                margin: 40px 0;
                padding: 30px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                border: 1px solid {colors['border']};
            }}
            h1 {{ 
                color: {colors['primary']};
                font-size: 2.8em;
                margin-bottom: 25px;
                font-weight: 700;
                text-align: left;
            }}
            h2 {{ 
                color: {colors['primary']};
                font-size: 2.2em;
                border-bottom: 3px solid {colors['primary']};
                padding-bottom: 12px;
                margin-top: 40px;
                margin-bottom: 25px;
                font-weight: 600;
                text-align: left;
            }}
            h3 {{ 
                color: {colors['secondary']};
                font-size: 1.8em;
                margin-top: 30px;
                margin-bottom: 20px;
                font-weight: 600;
                text-align: left;
            }}
            p {{
                font-size: 1.2em;
                line-height: 1.8;
                margin-bottom: 1.2em;
                text-align: justify;
                color: {colors['text']};
            }}
            strong {{
                font-weight: 600;
                color: {colors['primary']};
            }}
            code {{ 
                background: {colors['code_bg']};
                padding: 4px 8px;
                border-radius: 4px;
                font-family: 'Consolas', monospace;
                font-size: 1.1em;
                color: {colors['text']};
                border: 1px solid {colors['border']};
            }}
            pre {{ 
                background: {colors['code_bg']};
                padding: 20px;
                border-radius: 8px;
                overflow-x: auto;
                border: 2px solid {colors['border']};
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
                border: 2px solid {colors['border']};
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 25px 0;
                font-size: 1.1em;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                border: 2px solid {colors['border']};
            }}
            th, td {{
                padding: 15px;
                border: 1px solid {colors['border']};
                text-align: left;
            }}
            th {{ 
                background: {colors['table_header']};
                color: {colors['primary']};
                font-weight: 600;
                font-size: 1.1em;
            }}
            tr:nth-child(even) {{
                background: {colors['code_bg']};
            }}
            tr:hover {{
                background: {colors['highlight']};
            }}
            .notebook-title {{
                background: {colors['header_bg']};
                color: {colors['primary']};
                padding: 25px;
                margin: 35px 0;
                border-radius: 8px;
                font-size: 1.4em;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                border: 2px solid {colors['border']};
                text-align: left;
            }}
            .output_png img {{
                display: block;
                margin: 35px auto;
                max-width: 1000px;
            }}
            .key-point {{
                background: {colors['header_bg']};
                padding: 20px;
                border-radius: 8px;
                margin: 20px 0;
                border: 2px solid {colors['border']};
                font-size: 1.1em;
                color: {colors['text']};
            }}
            .emoji {{
                font-size: 1.4em;
                color: {colors['primary']};
            }}
            .dataframe {{
                font-size: 1.1em;
                margin: 25px 0;
                text-align: left;
            }}
            .dataframe th {{
                background: {colors['table_header']};
                color: {colors['primary']};
                font-weight: 600;
                padding: 12px;
            }}
            .output_text {{
                font-size: 1.1em;
                line-height: 1.6;
                margin: 20px 0;
                color: {colors['text']};
                text-align: left;
            }}
            ul, ol {{
                font-size: 1.1em;
                line-height: 1.8;
                margin: 20px 0;
                padding-left: 25px;
                text-align: left;
            }}
            li {{
                margin-bottom: 12px;
                color: {colors['text']};
            }}
            @media print {{
                body {{ 
                    margin: 25mm;
                    font-size: 11pt;
                }}
                .page-break {{ page-break-after: always; }}
                pre {{ 
                    white-space: pre-wrap;
                    font-size: 10pt;
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
            <h2 style="color: {colors['primary']}; border: none;">🎯 Data-Driven Decision Making Analysis</h2>
            <p style="font-size: 1.3em;"><strong>📚 Course:</strong> IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers</p>
            <p style="font-size: 1.3em;"><strong>👨‍🎓 Student Name:</strong> Lalit Nayyar</p>
            <p style="font-size: 1.3em;"><strong>📧 Email ID:</strong> lalitnayyar@gmail.com</p>
            <p style="font-size: 1.3em;"><strong>📅 Date:</strong> May 5, 2025</p>
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
            ('LalitNayyarIIMKMod4_predictive_analysis_fin.ipynb', '🔮'),
            ('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_fin.ipynb', '🔬')
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
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = [14, 7]
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11
plt.rcParams['lines.linewidth'] = 2.0
plt.rcParams['font.size'] = 11
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
    '#1A237E',  # Dark blue
    '#BF360C',  # Dark orange
    '#1B5E20',  # Dark green
    '#4A148C',  # Dark purple
    '#212121',  # Near black
    '#01579B'   # Navy blue
])
plt.rcParams['axes.edgecolor'] = '#212121'
plt.rcParams['axes.labelcolor'] = '#212121'
plt.rcParams['xtick.color'] = '#212121'
plt.rcParams['ytick.color'] = '#212121'
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
        
        print(f"\nAligned submission created: {output_file}")
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
    create_aligned_submission()
