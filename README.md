# PySpark Covid-19 analysis
The goal of the assignment is to address some queries regarding the Covid-19 pandemic at a global level, using Apache Spark.

This repo provides everything needed for a self-contained, local PySpark 1-node "cluster" running on your laptop, including a Jupyter notebook environment.

It uses [Visual Studio Code](https://code.visualstudio.com/) and the [devcontainer feature](https://code.visualstudio.com/docs/devcontainers/containers) to run the Spark/Jupyter server in Docker, connected to a VS Code dev environment frontend.

## Requirements

- Install [Docker Desktop]

- Open [Visual Studio Code]

- Install the [VS Code Remote Development pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

## Setup

1. Install required tools 

1. Git clone this repo to your laptop

1. Open the local repo folder in VS Code

1. Open the [VS Code command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) and select/type 'Reopen in Container'

1. Wait while the devcontainer is built and initialized, this may take several minutes

1. Wait a few moments for the Jupyter kernel to initialize... if after about 30 seconds or so the button on the upper-right still says 'Select Kernel', click that and select the option with 'ipykernel'


## Reference 
The project structure is from Josh Lane [pyspark-devcontainer repo](https://github.com/jplane/pyspark-devcontainer) 





