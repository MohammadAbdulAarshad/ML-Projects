from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj if line.strip() and not line.startswith("-e")]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name = 'MLPROJECT',
version = '0.0.1',
author ='Arsh',
author_email = 'abdulaarshadmohammad@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)