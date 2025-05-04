import nbformat
from jupyter_client.kernelspec import KernelSpecManager
from jupyter_core.paths import jupyter_data_dir
import json

def trust_notebook():
    # Read the notebook
    notebook_path = 'LalitNayyarIIMKMod4_descriptive_analysis_1.ipynb'
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Update notebook metadata
    nb.metadata.update({
        'kernelspec': {
            'display_name': 'Python 3',
            'language': 'python',
            'name': 'python3'
        },
        'trusted': True,
        'language_info': {
            'codemirror_mode': {
                'name': 'ipython',
                'version': 3
            },
            'file_extension': '.py',
            'mimetype': 'text/x-python',
            'name': 'python',
            'nbconvert_exporter': 'python',
            'pygments_lexer': 'ipython3',
            'version': '3.9.0'
        }
    })
    
    # Save the notebook with updated metadata
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    trust_notebook()
