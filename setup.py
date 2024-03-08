from setuptools import find_packages, setup
from typing import List

ignore = '-e .'

def get_requirements(filepath:str)->List[str]:
    """
    
    This function returns the list of requirements from requirements.txt
    
    """

    requirements = []
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if ignore in requirements:
            requirements.remove(ignore)

    return requirements

setup(
    name = 'e2e_ml_deployment',
    version = '0.1',
    author = 'Nemil Panchamia',
    author_email = 'p.nemil28@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)