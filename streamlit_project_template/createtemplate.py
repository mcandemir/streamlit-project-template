import os

class CreateTemplate():
    def __init__(self) -> None:
        # get the user's project base dir
        self.BASE_DIR = os.getcwd()

        # template modules of the streamlit app
        self.TEMPLATES= {
            'components': 'components/components.py',
            'pages': 'pages/pages.py',
            'callbacks': 'callbacks/callbacks.py',
        }

        # base templates (these will be copied to the user's project)
        # values will be set in _set_paths
        self.BASE_TEMPLATE_PATHS = {
            'components': '',
            'pages': '',
            'callbacks': '',
        }



    def createTemplate(self):
        # processes
        self._set_paths()
        self._create_components()
        pass


    def _create_components(self):
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


