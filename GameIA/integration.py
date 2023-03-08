import os
import importlib.util
from nbconvert import PythonExporter

# Caminho para o arquivo .ipynb
notebook_path = "C:\\Users\\Guilherme\\Desktop\\Inteligência_Artificial\\Projetos\\AI-Maze-Game-main\\GameIA\\BuscaLargura.ipynb"

# Caminho para salvar o arquivo Python gerado
python_path = "C:\\Users\\Guilherme\\Desktop\\Inteligência_Artificial\\Projetos\\AI-Maze-Game-main\\GameIA\\Busca.py"

# Converter o arquivo .ipynb em um arquivo Python
exporter = PythonExporter()
output, _ = exporter.from_filename(notebook_path)
with open(python_path, "w") as f:
    f.write(output)

# Importar o arquivo Python como um módulo
module_name = os.path.splitext(os.path.basename(python_path))[0]
spec = importlib.util.spec_from_file_location(module_name, python_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Utilizar as funções e variáveis definidas no arquivo Jupyter Notebook
result = module.my_function()
