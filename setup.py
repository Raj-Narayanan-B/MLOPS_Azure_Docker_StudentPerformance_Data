from setuptools import setup, find_packages

def get_requirements(requirements_path:str):
    requirements=[]
    with open(requirements_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements

setup(
    name="MLOPS_Test",
    author="Raj",
    version="0.0.1",
    author_email="brajnarayanan.b@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)