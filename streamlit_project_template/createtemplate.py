import os

class CreateTemplate():
    def __init__(self) -> None:
        
        self.BASE_DIR = os.getcwd()



    def createTemplate(self):
        # for template_dir in self.TEMPLATE_DIRS:
        #     os.makedirs(os.path.join(CURRENT_DIR, template_dir))
        
        # for template_file in self.TEMPLATE_FILES:
        #     with open(os.path.join(CURRENT_DIR, template_file), 'w', ) as f:
        #         pass
        
        self._set_paths()
        # self._create_components()
        pass


    def _create_components(self):

        os.path.abspath(__file__)


        # name = 'components/components.py'
        # os.makedirs(os.path.dirname(name), exist_ok=True)
        # with open(name, "w") as f:
        #     # with open('')


        #     f.write(
        #         """import streamlit as st
        #         ### This is where you define your components. Every component is a piece of your applicaton
        #         def component_input_form():
        #             st.text_area(label="Name:")
        #             """)




        # # with open(os.path.join(self.BASE_DIR, 'components\components.py')) as f:
        # #     f.write('')

        # pass
    
    def _set_paths(self):
        path = os.path.abspath(__file__)
        path = path[:path.rfind('\\')]

        component_template_path = os.path.join(path, 'template\components.py')
        print(component_template_path)

        with open(component_template_path, 'r') as f:
            print(f.read())


