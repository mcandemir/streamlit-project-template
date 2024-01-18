import os

class CreateTemplate():
    def __init__(self) -> None:
        
        self.BASE_DIR = os.getcwd()

        # self.TEMPLATE_DIRS = [
        #     'components/',
        #     'pages/',
        #     'callbacks/',
        #     ''
        # ]

        # self.TEMPLATE_FILES = [
        #     'app.py'
        #     'components/components.py',
        #     'pages/mainpage.py',
        #     'callbacks/callbacks.py',
        # ]


    def createTemplate(self):
        # for template_dir in self.TEMPLATE_DIRS:
        #     os.makedirs(os.path.join(CURRENT_DIR, template_dir))
        
        # for template_file in self.TEMPLATE_FILES:
        #     with open(os.path.join(CURRENT_DIR, template_file), 'w', ) as f:
        #         pass
        
        self._create_components()
        pass


    def _create_components(self):
        if 'components' not in os.listdir(self.BASE_DIR):
            os.makedirs(os.path.join(self.BASE_DIR, 'components'))

        print(os.path.exists(os.path.join(self.BASE_DIR, 'components')))

        with open(os.path.join(self.BASE_DIR, 'components\components.py')) as f:
            f.write('')

        pass