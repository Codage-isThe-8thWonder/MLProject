from setuptools import find_packages, setup
from typing import List




HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
        this function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements




setup(
    name="mlproject",
    version="0.0.1",
    author = "Shreyash nagrale",
    author_email="shreyashnagrale260@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")

)



'''
to build virtual virtual environment :
    python -m venv .venv --without-pip
    .venv\Scripts\Activate.ps1
    python -m ensurepip --upgrade
    pip --version


Then you can install your al project dependencies by using :
    pip install -r requirements.txt

    
pip install -e .   :-  "Current project ko install karo, lekin editable mode me."

'''