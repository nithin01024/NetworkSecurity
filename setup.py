from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    requirements_list:List[str]=[]
    try:
        with open('requirements.txt') as file:
            # read lines from the file
            lines = file.readlines()
            ## process each line
            for line in lines:
                requirements= line.strip()
            # ignore empty lines and -e.
            if requirements and requirements!= '-e.':
                requirements_list.append(requirements)
    except FileNotFoundError:
        print('Requirements.txt file not exists')
    return requirements_list
print(get_requirements)

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Nithin',
    author_email='nithin.sonnaila23@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)