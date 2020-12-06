# Environment Setup

1. install python3
2. clone this repo:

        git clone https://github.com/HenryZerocool/henz-cli

3. to install cli open terminal and run:

        pip3 install -e .

4. to uninstall run:

        pip3 uninstall henzcli

## Before submit Pull Request

**Note:** There are recommendations for plugins and settings in `.vscode`. Following will make it safer to code in the repo

1. Please format your code using `black` in your command line:

        black .\henzcli

2. Please check your code using `flake8` linter in your command line:

        flake8 .

3. Please make sure your work pass all test:

        python -m unittest test

4. (Optional) If you want to check test coverage and then add more tests:

    4a. Option 1:

        coverage report -m

    4b. Option 2 (better readability):

        coverage report -m > ./test/coverage_report.log

    then open the log file

