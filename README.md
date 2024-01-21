# Streamlit Project Template

A streamlit project template to create cleaner code and cost-efficient maintable apps. 

## Template Hierarchy:
     MyProject
    ├──  src
    │  ├──  __init__.py 
    │  ├──  callbacks.py
    │  ├──  components.py
    │  └──  pages.py
    ├──  .gitignore
    ├──  app.py
    ├──  Dockerfile
    ├──  README.md
    └──  requirements.txt

## Installation:
```
$ pip install streamlit-project-template
$ streamlit-project-template createtemplate
```


## Docs:
- ` MyProject:` This is the top-level project folder, which you initialize your application template.

- ` src:` In this folder, you keep your modules for your application. It will start with 3 main modules (`callbacks.py`, `components.py`, `pages.py`) which are essential for this app architecture, but you can add more modules besides them.

- ` __init__.py:` When calling a module that is in another directory, python might not be able to find it. To solve this problem, we will create an `__init__.py` file in `src`, in order to tell python to treat this folder as a library.

- ` callbacks.py:` This file(s) will contain your streamlit callbacks.

- ` components.py:` This is where you create your components. Each component is a one or multiple row of streamlit elements. This way you can use a component in multiple places without rewriting it and it will make maintaining easier and cost efficient.

- ` pages.py:` In this file you will hold your pages as classes, which are built with components row by row as defined in yur `components.py` file(s).

- ` app.py:` This is the main file you will run. It initialliy contains a page config, a session state which holds your current page name and the page navigation. All the session states should be initialized here, and the page navigation should be managed here in order to keep the project architecture organized and run one page at a time to reduce resource cost.

- ` .gitignore:` Your standard `.gitignore` file.

- ` Dockerfile:` Initial dockerfile which is configured to run streamlit.

- ` README.md:` Introduce your project here.

- ` requirements.txt`: Required packages for your application will be here.
