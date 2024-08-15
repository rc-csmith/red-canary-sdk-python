import pydoc
import rcapi
  
OUTPUT_DIR = './docs'

# Generate list of methods that should be documented

list_of_root_methods = ['rcapi']

for method in list_of_root_methods:
  with(open(f'{OUTPUT_DIR}/{method}.txt','w')) as file:
    file.write(f'{pydoc.render_doc(getattr(rcapi,method), renderer=pydoc.plaintext)}\n\n')

list_of_model_methods = [func for func in dir(rcapi.models) if not func.startswith("__")]

for method in list_of_model_methods:
  with (open(f'{OUTPUT_DIR}/{method}.txt','w')) as file:
    file.write(f'{pydoc.render_doc(getattr(rcapi.models,method), renderer=pydoc.plaintext)}\n\n')

