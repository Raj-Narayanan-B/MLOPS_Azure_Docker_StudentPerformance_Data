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
    
    os.path.join("src","__init__.py"),
    os.path.join("src","exception.py"),
    os.path.join("src","logger.py"),
    os.path.join("src","utils.py"),

    os.path.join("src","components","__init__.py"),
    os.path.join("src","components","data_ingestion.py"),
    os.path.join("src","components","data_transformer.py"),
    os.path.join("src","components","model_trainer.py"),

    os.path.join("src","pipeline","__init__.py"),
    os.path.join("src","pipeline","predict_pipeline.py"),
    os.path.join("src","pipeline","train_pipeline.py")
]

for i in files:
    with open(i,"w"):
        pass