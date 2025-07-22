import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(assctime)s]: %(message)s:')

project_name = "cnnClassifier"

list_of_files = [
    "Chicken-Disease-Classification/.github/workflows/.gitkeep",
    f"Chicken-Disease-Classification/src/{project_name}/__init__.py",
    f"Chicken-Disease-Classification/src/{project_name}/components/__init__.py",
    f"Chicken-Disease-Classification/src/{project_name}/utils/__init__.py",
    f"Chicken-Disease-Classification/src/{project_name}/config/__init__.py",
    f"Chicken-Disease-Classification/src/{project_name}/config/configuration.py",
    f"Chicken-Disease-Classification/src/{project_name}/pipeline/__init__.py",
    f"Chicken-Disease-Classification/src/{project_name}/entity/__innit__.py",
    f"Chicken-Disease-Classification/src/{project_name}/constants/__init__.py",
    "Chicken-Disease-Classification/config/config.yaml",
    "Chicken-Disease-Classification/dvc.yaml",
    "Chicken-Disease-Classification/params.yaml",
    "Chicken-Disease-Classification/requirements.txt",
    "Chicken-Disease-Classification/setup.py",
    "Chicken-Disease-Classification/research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory; {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename} at {filedir}")
    else:
        logging.info(f"{filename} already exists at {filedir} and is not empty. Skipping creation.")