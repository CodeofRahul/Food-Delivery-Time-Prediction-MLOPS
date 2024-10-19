# in future if we plan to release our project as package or library in that case setup file will be very 
# important

# in python, setup.py is a module used to build and distribute PYthon packages. It typically contains 
# information about the package, such as its name, version, and dependencies, as well as instructions 
# for building and installing the package



from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Machine Learning Project"
VERSION = "0.0.1"
DESCRIPTION = "This is our Machine  Learning Project in Modular coding"
AUTHOR_NAME = "Rahul"
AUTHOR_EMAIL = "dummy@successanalytics.ai"

REQUIREMENTS_FILE_NAME = "requirement.txt"

HYPHEN_E_DOT = "-e ."
# Requirement.txt file open
# read
# \n -> ""

def get_requirements_list()-> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

        return requirement_list    



setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires = get_requirements_list()
     )