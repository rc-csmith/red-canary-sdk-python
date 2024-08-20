import os
import shutil
import pydoc
import rcapi
  
OUTPUT_DIR = './docs'

# Create output directory if it does not exist
if os.path.exists(OUTPUT_DIR):
  shutil.rmtree(OUTPUT_DIR)

os.makedirs(OUTPUT_DIR)
os.makedirs(f'{OUTPUT_DIR}/models')
  
# Generate list of methods that should be documented
list_of_root_methods = ['rcapi']

for method in list_of_root_methods:
  with(open(f'{OUTPUT_DIR}/{method}.txt','w')) as file:
    file.write(f'{pydoc.render_doc(getattr(rcapi,method), renderer=pydoc.plaintext)}\n\n')

list_of_model_methods = [func for func in dir(rcapi.models) if not func.startswith("__")]
for method in list_of_model_methods:
  temp_method = getattr(rcapi.models, method)
  list_of_secondary_model_methods = [func for func in dir(temp_method) if not func.startswith("__") and not func.endswith('Collection') and not func.endswith('Resource')]
  for secondary_method in list_of_secondary_model_methods:
    with (open(f'{OUTPUT_DIR}/models/{method}.txt','a')) as file:
      file.write(f'{pydoc.render_doc(getattr(temp_method,secondary_method), renderer=pydoc.plaintext)}\n\n')