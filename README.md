conda create -p student_performance python=3.11.5 -y

Create a conda environment named student_performance with python version 3.11.5 
Here, -p will specify the terminal to create the environment to be in the pwd

# FOR AZURE
Run from terminal:
docker build -t testdockerkrish.azurecr.io/mltest:latest .

docker login testdockerkrish.azurecr.io

docker push testdockerkrish.azurecr.io/mltest:latest