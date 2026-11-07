# CI/CD Fundamentals Practice
This project demostrates a simple continuous integration using python, github and github actions. 
The pipeline automatically runs test whenever code is pushed to the main branch or a pull request is opened against main.
## Purpose
The purpose of this exercise is to understand how Continuous Integration works in software development.
I created a simple Python function that calculates a payment total. I then wrote an automated test to check whether the function returns the correct result.
Finally, I configured GitHub Actions to run the test automatically when code is pushed to GitHub.
## Tools and Technologies
- Python: Used to write the application and automated test.
- Git: Used to track changes to the project.
- GitHub: Used to store the project repository.
- GitHub Actions: Used to automate the testing process.
- GitHub Codespaces: Used as the online development environment.
- YAML: Used to configure the GitHub Actions workflow.
## Setup and Requirements
To run this project, you need:
- Python 3.12 or a compatible Python 3 version.
- Git.
- A GitHub account (to view the repository and workflow).
### Getting Started
1. Clone the repository:

   git clone (https://github.com/faithOkolie/cicd-practice)

2. Move into the project directory:

   cd cicd-practice

3. Run the automated test:

   python -m unittest
## Project Steps
### 1. Created a Python application
Created app.py and wrote a function called calculate_total.
The function adds a payment amount and fee.

### 2. Created an automated test
Created test_app.py using Python's unittest module.
The test checks whether 1000 + 50 returns 1050.

### 3. Tested the application
Ran the following command:
python -m unittest
The test passed when the function returned the expected result.

### 4. Created a GitHub Actions workflow
Created a workflow file at:
.github/workflows/ci.yml
Configured it to run whenever code is pushed to the main branch
or a pull request is opened against main.

### 5. Pushed the project to GitHub
Used Git commands to add, commit and push the project files.

### 6. Verified the pipeline
Opened the Actions tab in GitHub and checked the workflow run
to confirm that the automated test completed successfully.

## How the CI Pipeline Works
1. A developer makes changes to the code.
2. The developer pushes the changes to GitHub.
3. GitHub Actions detects the update.
4. GitHub Actions checks out the repository.
5. Python is configured on the runner.
6. The automated test runs.
7. GitHub reports whether the test passed or failed.

If the test fails, the workflow reports an error so the developer can fix the problem.
## What I Learned
From this exercise, I learned:

- What Continuous Integration means.
- How automated testing helps identify errors early.
- How to write a basic Python unit test.
- How GitHub Actions automates testing.
- How YAML is used to configure workflows.
- How code changes can trigger an automated pipeline.
- How to inspect workflow results using the GitHub Actions tab.

I also learned that a CI pipeline can prevent code that fails
required tests from progressing through the development process.
## Project Status
Completed: Basic Continuous Integration pipeline.

Future improvements:
- Add more automated tests.
- Introduce code quality checks.
- Build a Docker image.
- Push the image to Amazon ECR.
- Extend the pipeline to deploy the application.