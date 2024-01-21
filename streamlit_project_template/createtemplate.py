import os

class CreateTemplate():
    def __init__(self) -> None:
        # get the user's project base dir
        self.BASE_DIR = os.getcwd()

        # template modules of the streamlit app
        self.TEMPLATES= {
            'app': './app.py',
            'callbacks': 'src/callbacks.py',
            'components': 'src/components.py',
            'pages': 'src/pages.py',
            '__init__': 'src/__init__.py',
        }

        # base templates (these will be copied to the user's project)
        # values will be set in _set_paths
        self.BASE_TEMPLATE_PATHS = {
            'app': '',
            'callbacks': '',
            'components': '',
            'pages': '',
            '__init__': '',
        }


    def createTemplate(self):
        # processes
        self._set_paths()
        self._create_srcfiles()
        self._create_dockerfile()
        self._create_requirements()
        self._create_readme()
        pass


    def _create_srcfiles(self):
        for template in self.TEMPLATES:
            # make the template dirs and files
            os.makedirs(os.path.dirname(self.TEMPLATES[template]), exist_ok=True)


            # write the contents to template files
            with open(self.TEMPLATES[template], "w") as f:
                with open(self.BASE_TEMPLATE_PATHS[template], 'r') as f2:
                    component_template_content = f2.read()
                f.write(component_template_content)

    
    def _set_paths(self):
        # set the base template paths to be copied
        path = os.path.abspath(__file__)
        path = path[:path.rfind('\\')]

        for base_template in self.BASE_TEMPLATE_PATHS.keys():
            self.BASE_TEMPLATE_PATHS[base_template] = os.path.join(path, f'template\{base_template}.py')


    def _create_dockerfile(self):
        with open('./Dockerfile', 'w') as f:
            f.write("""FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \\
    build-essential \\
    curl \\
    software-properties-common \\
    git \\
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]""")


    def _create_requirements(self):
        with open('./requirements.txt', 'w') as f:
            f.write("""streamlit""")
    
    def _create_readme(self):
        with open('./README.md', 'w') as f:
            f.write("""# My Project""")
    
    def _create_gitignore(self):
        with open('./.gitignore', 'w') as f:
            f.write("""__pycache__/""")
