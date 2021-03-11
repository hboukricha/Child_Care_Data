# Project Working Steps
- The project working steps are described as Software Development Life Cycle (SDLC) steps.
- The working model within SDLC was iterative, i.e. start with required simple features and increment iteratively to further additional / more  complex features.

## Step1: Requirement Analysis
This step was not really relevant in this example project but could be mapped to task specification provided by the task provider (BCAI-T). 

### Task Specification
Please provide an integrable API (library) in a language of your choice which allows a user, in this case, another SW-developer to retrieve / query data from a source file (csv file). An example file is included in this project under /tests/child_care_data.csv. The provided API must allow the user to specify a path to the source file and to filter data according to a specified year and location. Please note, that the task provider is not only interested in code quality but also in provided documentation, tests, and CI/CD behavior. 

- Project Delivery: Ideally within [Github](https://github.com/)
- Deadline: **12.03.2021**

## Step2: Requirement Definition
- *Req1*: API *must* allow user to specify path to source file
- *Req2*: API *must* allow user to filter data according to year and location
- *Req3*: API developer *must* provide documentation, tests, and work with CI/CD 'behavior'

## Step3: Designing the API
- *Prerequisites*: 
    - Choose suitable language, IDE, code hosting platform
    - Perform "getting started" tutorials if newbie to language or IDE or hosting platform 

- *Decisions*:
    - Choice of **language**: Decided to choose **python** for its simplicity and for providing helpful data analysis libraries like pandas, numpy, or matplotlib. As stated by community, python is easy to use for newbies. As virtual environment, venv is chosen as a simple getting started environment. 
    - Choice of **IDE**: Decided to choose **vscode** as recommended by community, i.e. second best IDE after pycharm and because it supports many other languages besides python.
    - Choice of **code hosting platform**: Decided to choose **GitHub** for version control and collaboration on opensource projects and also because it is a preferred option by task provider

- *Design & Architecture*:
    - In a first step, API is designed as composed of **two modules**. The first module holds the api itself and the second module implements behavior of the api. As such the first module is **encapsulating** the behavior of the second module. 
    - In a second step, the functions needed to fullfill requirements *Req1* and *Req2* were defined / declared (input/return parameters) within first and second module.

- *Implementation*
    - API fucntions were implemented one-by-one within **different feature branches** to keep always a working version in the master branch. During implementation the function behavior is tested, documented, and pushed in an iterative way (*Req3*). 
    - Link to source code: [childcaredatabw](https://github.com/hboukricha/Child_Care_Data)

## Step4: Testing
- Testing is performed in an **iterative** way "(pull)-implement-test-document-push" during implementation
- Used testing methods: **Manual tests** in a first place (quick tests) and **unittests** for a more comprehensive testing of, e.g., different values and combinations of function parameters  

## Step5: Deployment
- Local Deployment: Local installation of package ( python3 -m pip install . )
- Global Deployment: Package published (only the last two releases 0.0.4 and 0.0.5) within https://test.pypi.org/project/childcaredatabw/0.0.5/

# Challenges for a newbie to python vscode and GitHub :-)
- python: 
    - current experience: Alomost a newbie. Only working with existing code and packages, to use, extend, and debug existing code. Starting a project from 'scratch' is a new experience.
    - too many python versions with different dependencies and different tools versions, e.g., package installers, linting, and documentation. One feels lost at the beginning as it feels like having different worlds for the same thing. Documentation in the web and the communities (e.g., Stack Overflow) is diverging and often not working, so one needs to compose input from different sources to fix a bug or understand best practices. While python is liked for its simplicity, writing clean code can become confusing with increasing code complexity. Working on the basis of conventions is a risk. 
- vscode: 
    - Current experience: Newbie.
    - too many extensions and offers for support resulting in unstable behavior, e.g., pylint shows random behavior despite being enabled within IDE. 
- GitHub:
    - Current experience: Newbie.
    - Due to the tied time schedule, did not manage to figure out provided GitHub actions like automating CI/CD using a GitHub workflow.  