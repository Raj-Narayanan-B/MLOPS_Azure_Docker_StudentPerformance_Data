import os

dirs = [
    "artifacts",
    "notebooks",
    "templates",
    os.path.join("src","components"),
    os.path.join("src","pipeline")
]

for i in dirs:
    os.makedirs(i,exist_ok=True)
    with open(os.path.join(i,".gitkeep"),"w"):
        pass

files = [
    "setup.py",
    "requirements.txt",
    "README.md",
    os.path.join("src","__init__.py")
]

for i in files:
    with open(i,"w"):
        pass