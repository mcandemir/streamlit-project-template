"""
this module contains the template creation steps and the functions
"""

import os

class CreateTemplate():
    """
    this is the class which handles template creations
    """
    def __init__(self) -> None:
        """
        set initial values at the initialization
        """
        # get the user's project base dir
        self.base_dir = os.getcwd()

        # template modules of the streamlit app
        self.templates= {
            'app': './app.py',
            'callbacks': 'src/callbacks.py',
            'components': 'src/components.py',
            'pages': 'src/pages.py',
            '__init__': 'src/__init__.py',
        }

        # base templates (these will be copied to the user's project)
        # values will be set in _set_paths
        self.base_template_paths = {
            'app': '',
            'callbacks': '',
            'components': '',
            'pages': '',
            '__init__': '',
        }


    def create_template(self):
        """
        creates the template files by calling needed functions
        """
        self._set_paths()
        self._create_srcfiles()
        self._create_dockerfile()
        self._create_requirements()
        self._create_readme()


    def show_template(self):
        """
        print out the template
        """
        for file in self.templates.values():
            print(file)


    def _create_srcfiles(self):
        """
        this will create the main template files
        """
        for template, file in self.templates.items():
            # make the template dirs and files
            os.makedirs(os.path.dirname(file), exist_ok=True)


            # write the contents to template files
            with open(file, "w", encoding="utf8") as f:
                with open(self.base_template_paths[template], 'r', encoding="utf8") as f2:
                    component_template_content = f2.read()
                f.write(component_template_content)


    def _set_paths(self):
        """
        this will set the actual path of the package template files to be copied
        """
        path = os.path.abspath(__file__)
        path = path[:path.rfind('\\')]
        path = os.path.join(path, 'template/')

        for base_template in self.base_template_paths:
            self.base_template_paths[base_template] = os.path.join(path,
                                                                   f'{base_template}.py',
                                                                   ).replace('/', '\\')


    def _create_dockerfile(self):
        """
        create the dockerfile
        """
        with open('./Dockerfile', 'w', encoding="utf8") as f:
            f.write("""FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y \\
    build-essential \\
    curl \\
    software-properties-common \\
    git \\
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]""")


    def _create_requirements(self):
        """
        create requirements file
        """
        with open('./requirements.txt', 'w', encoding="utf8") as f:
            f.write("""streamlit""")

    def _create_readme(self):
        """
        create readme file
        """
        with open('./README.md', 'w', encoding="utf8") as f:
            f.write("""# My Project""")

    def _create_gitignore(self):
        """
        create gitignore file
        """
        with open('./.gitignore', 'w', encoding="utf8") as f:
            f.write("""__pycache__/""")
