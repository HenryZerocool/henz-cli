# Environment Setup

1. install python
2. to install cli open terminal and run:

        pip3 install -e .

3. to uninstall run:

        pip3 uninstall henzcli

## Before submit Pull Request

**Note:** There are recommendations for plugins and settings in `.vscode`. Following will make it safer to code in the repo

1. Please format your code using `black` in your command line:

        black .\henzcli

2. Please check your code using `flake8` linter in your command line:

        flake8 .
