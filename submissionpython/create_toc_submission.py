import nbformat
from nbconvert import HTMLExporter
import markdown
import os
from datetime import datetime

def create_toc_submission():
    """Create a submission with table of contents and page numbers"""
    
    # Color scheme
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
            
            @page {{
                size: A4;
                margin: 25mm 20mm;
            }}
            
            body {{
                font-family: 'Open Sans', Arial, sans-serif;
                line-height: 1.8;
                color: {colors['text']};
                max-width: 1200px;
                margin: 0 auto;
                padding: 40px;
                background: #FFFFFF;
                font-size: 16px;
                counter-reset: page 1;
            }}
            
            /* Table of Contents Styles */
            .toc {{
                margin: 40px 0;
                padding: 30px;
                background: {colors['header_bg']};
                border-radius: 12px;
                border: 2px solid {colors['border']};
            }}
            
            .toc h2 {{
                color: {colors['primary']};
                margin-bottom: 25px;
                border-bottom: 2px solid {colors['primary']};
            }}
            
            .toc ul {{
                list-style: none;
                padding: 0;
                margin: 0;
            }}
            
            .toc li {{
                margin: 10px 0;
                padding: 5px 0;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }}
            
            .toc a {{
                color: {colors['primary']};
                text-decoration: none;
                font-size: 1.1em;
            }}
            
            .toc .dots {{
                border-bottom: 2px dotted {colors['primary']};
                flex: 1;
                margin: 0 10px;
            }}
            
            .toc .page-number {{
                color: {colors['primary']};
                font-weight: 600;
            }}
            
            /* Page Numbers */
            .page {{
                position: relative;
                margin-bottom: 30px;
                page-break-after: always;
            }}
            
            .page-number {{
                position: running(pageNumber);
                text-align: center;
                font-size: 12pt;
                color: {colors['text']};
            }}
            
            @page {{
                @bottom-center {{
                    content: "Page " counter(page);
                }}
            }}
            
            /* Rest of the styles */
            [Previous styles from create_aligned_submission.py...]
        </style>
    </head>
    <body>
        <div class="page">
            <div class="header">
                <h1>📊 Customer Behavior Analysis Project</h1>
                <h2 style="color: {colors['primary']}; border: none;">🎯 Data-Driven Decision Making Analysis</h2>
                <p style="font-size: 1.3em;"><strong>📚 Course:</strong> IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers</p>
                <p style="font-size: 1.3em;"><strong>👨‍🎓 Student Name:</strong> Lalit Nayyar</p>
                <p style="font-size: 1.3em;"><strong>📧 Email ID:</strong> lalitnayyar@gmail.com</p>
                <p style="font-size: 1.3em;"><strong>📅 Date:</strong> May 5, 2025</p>
            </div>
        </div>
        
        <div class="page">
            <div class="toc">
                <h2>📑 Table of Contents</h2>
                <ul>
                    <li>
                        <a href="#project-overview">Project Overview</a>
                        <span class="dots"></span>
                        <span class="page-number">1</span>
                    </li>
                    <li>
                        <a href="#dataset-description">Dataset Description</a>
                        <span class="dots"></span>
                        <span class="page-number">2</span>
                    </li>
                    <li>
                        <a href="#initial-analysis">Initial Data Analysis</a>
                        <span class="dots"></span>
                        <span class="page-number">3</span>
                    </li>
                    <li>
                        <a href="#descriptive-analysis">Descriptive Analysis</a>
                        <span class="dots"></span>
                        <span class="page-number">8</span>
                    </li>
                    <li>
                        <a href="#diagnostic-analysis">Behavior Diagnostic Analysis</a>
                        <span class="dots"></span>
                        <span class="page-number">15</span>
                    </li>
                    <li>
                        <a href="#predictive-analysis">Predictive Analysis</a>
                        <span class="dots"></span>
                        <span class="page-number">22</span>
                    </li>
                    <li>
                        <a href="#conclusions">Conclusions and Recommendations</a>
                        <span class="dots"></span>
                        <span class="page-number">28</span>
                    </li>
                </ul>
            </div>
        </div>
    '''
    
    try:
        # Add README content with emojis and section IDs
        with open('README.md', 'r', encoding='utf-8') as f:
            readme_content = f.read()
            
            # Add emojis and IDs to section headers
            readme_content = readme_content.replace('# Project Overview', '<h1 id="project-overview">📋 Project Overview</h1>')
            readme_content = readme_content.replace('## Dataset Description', '<h2 id="dataset-description">📊 Dataset Description</h2>')
            readme_content = readme_content.replace('## Analysis Structure', '<h2 id="analysis-structure">🔍 Analysis Structure</h2>')
            readme_content = readme_content.replace('## Key Features', '<h2 id="key-features">🌟 Key Features</h2>')
            readme_content = readme_content.replace('## Learning Outcomes', '<h2 id="learning-outcomes">🎯 Learning Outcomes</h2>')
            readme_content = readme_content.replace('## Assessment Criteria', '<h2 id="assessment-criteria">📝 Assessment Criteria</h2>')
            
            html_content = html_template
            html_content += f'<div class="page section"><h2>📑 Project Documentation</h2>{markdown.markdown(readme_content)}</div>'
        
        # Process notebooks with section IDs
        notebooks = [
            ('LalitNayyarIIMKMod4_analysis_fin.ipynb', '🔍', 'initial-analysis', 'Initial Data Analysis'),
            ('LalitNayyarIIMKMod4_descriptive_analysis_fin.ipynb', '📊', 'descriptive-analysis', 'Descriptive Analysis'),
            ('LalitNayyarIIMKMod4_behavior_diagnostic_analysis_fin.ipynb', '🔬', 'diagnostic-analysis', 'Behavior Diagnostic Analysis'),
            ('LalitNayyarIIMKMod4_predictive_analysis_fin.ipynb', '🔮', 'predictive-analysis', 'Predictive Analysis')
        ]
        
        # Configure HTML exporter
        html_exporter = HTMLExporter()
        html_exporter.exclude_input_prompt = True
        html_exporter.exclude_output_prompt = True
        
        # Process each notebook
        for notebook_file, emoji, section_id, section_title in notebooks:
            if os.path.exists(notebook_file):
                print(f"Processing {notebook_file}...")
                
                # Read notebook
                with open(notebook_file, 'r', encoding='utf-8') as f:
                    nb = nbformat.read(f, as_version=4)
                
                # Update visualization style
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
                
                # Add to main HTML with emoji and section ID
                html_content += f'''
                <div class="page section">
                    <div class="notebook-title" id="{section_id}">
                        <h2>{emoji} {section_title}</h2>
                    </div>
                    {body}
                </div>
                '''
            else:
                print(f"Warning: {notebook_file} not found")
        
        # Add conclusions section
        html_content += '''
        <div class="page section">
            <h2 id="conclusions">📝 Conclusions and Recommendations</h2>
            <div class="key-point">
                <p>Final insights and recommendations based on the comprehensive analysis...</p>
            </div>
        </div>
        '''
        
        # Close HTML
        html_content += '</body></html>'
        
        # Save HTML
        output_file = 'LalitNayyar_IIMK_Module4_Submission.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"\nSubmission with TOC created: {output_file}")
        print("\nTo create the final PDF:")
        print("1. Open the HTML file in Chrome")
        print("2. Press Ctrl+P (or Command+P)")
        print("3. Set Destination to 'Save as PDF'")
        print("4. Set Paper size to A4")
        print("5. Enable 'Background graphics'")
        print("6. Set margins to 'Default'")
        print("7. Save as 'LalitNayyar_IIMK_Module4_Submission.pdf'")
        
    except Exception as e:
        print(f"Error creating submission: {e}")

if __name__ == '__main__':
    create_toc_submission()
