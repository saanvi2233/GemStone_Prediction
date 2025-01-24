from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements file and returns a list of dependencies.
    Removes '-e .' if present, as it's used for editable installs.
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        # Remove '-e .' if it exists in the requirements
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Sanvi Gupta',
    author_email='sanvi@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
