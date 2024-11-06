from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_req(file_path:str)->List[str]:
    '''
    returns List of names of packages
    '''
    req = []
    with open('requirements.txt', 'r+') as file:
        req = file.readlines()
        req = [line.replace('\n', '') for line in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)

    return req


setup(
    name='mlproject',
    version='0.0.1',
    author = 'karthikeyan',
    author_email='anumallakarthikeyan03@gmail.com',
    packages=find_packages(),
    install_requires = get_req('requirements.txt')
)