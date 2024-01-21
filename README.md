# Streamlit Project Template

A streamlit project template to create cleaner code and cost-efficient maintable apps. 

## Template Hierarchy:
    MyProject
    |-- src
    |  |-- __init__.py 
    |  |-- callbacks.py
    |  |-- components.py
    |  |-- pages.py
    |-- .gitignore
    |-- app.py
    |-- Dockerfile
    |-- README.md
    |-- requirements.txt

## Installation:
```
$ pip install streamlit-project-template
$ streamlit-project-template createtemplate
```


## Docs:
- `MyProject:` This is the top-level project folder, which you initialize your application template.

- `src:` In this folder, you keep your modules for your application. It will start with 3 main modules (`callbacks.py`, `components.py`, `pages.py`) which are essential for this app architecture, but you can add more modules besides them.

- `__init__.py:` When calling a module that is in another directory, python might not be able to find it. To solve this problem, we will create an `__init__.py` file in `src`, in order to tell python to treat this folder as a library.

- `callbacks.py:` This file(s) will contain your streamlit callbacks.

    ```python
    def set_page_home():
        """
        example callback that will set the selected page to 'home'
        """
        st.session_state['selected_page'] = 'home'


    def set_page_mypage1():
        """
        example callback that will set the selected page to 'mypage1'
        """
        st.session_state['selected_page'] = 'mypage1'


    def set_page_mypage2():
        """
        example callback that will set the selected page to 'mypage2'
        """
        st.session_state['selected_page'] = 'mypage2'
    ```

- `components.py:` This is where you create your components. Each component is a one or multiple row of streamlit elements. This way you can use a component in multiple places without rewriting it and it will make maintaining easier and cost efficient.

    ```python
    def component_say_hello():
        """
        example component with a home button and header
        """
        st.button('Home', on_click=callbacks.set_page_home)
        st.header('Hello World!')


    def component_change_page():
        """
        example component with a page selection
        """
        st.write('Where do you want to go?')
        st.button('Page 1', on_click=callbacks.set_page_mypage1)
        st.button('Page 2', on_click=callbacks.set_page_mypage2)


    def component_mypage1_title():
        """
        example component with mypage1 page info
        """
        st.write('My Page 1')

    def component_mypage2_title():
        """
        example component with mypage2 page info
        """
        st.write('My Page 2')
    ```

- `pages.py:` In this file you will hold your pages as classes, which are built with components row by row as defined in yur `components.py` file(s).

    ```python
    # HOME PAGE 
    class HomePage():
        """
        Your Home / Landing Page
        Here you can add your defined components under the loadPage() function
        """
        @staticmethod
        def load_home_page():
            """
            example home page load function
            """
            components.component_say_hello()
            components.component_change_page()


    # MYPAGE1
    class MyPage1():
        """
        Example Page class
        """
        @staticmethod
        def load_mypage1():
            """
            example page load function
            """
            components.component_say_hello()
            components.component_mypage1_title()


    # MYPAGE2
    class MyPage2():
        """
        Example Page class
        """
        @staticmethod
        def load_mypage2():
            """
            example page load function
            """
            components.component_say_hello()
            components.component_mypage2_title()
    ```

- `app.py:` This is the main file you will run. It initialliy contains a page config, a session state which holds your current page name and the page navigation. All the session states should be initialized here, and the page navigation should be managed here in order to keep the project architecture organized and run one page at a time to reduce resource cost.

    ```python
    # set session states
    if 'selected_page' not in st.session_state:
        st.session_state['selected_page'] = 'home'


    # page navigation
    match st.session_state['selected_page']:
        case 'home':
            HomePage.load_home_page()

        case 'mypage1':
            MyPage1.load_mypage1()

        case 'mypage2':
            MyPage2.load_mypage2()
    ```

- `.gitignore:` Your standard `.gitignore` file.

- `Dockerfile:` Initial dockerfile which is configured to run streamlit.

- `README.md:` Introduce your project here.

- `requirements.txt`: Required packages for your application will be here.
