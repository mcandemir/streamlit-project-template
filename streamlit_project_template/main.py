"""
This module contains the script to create templates
"""

import argparse
from .createtemplate import CreateTemplate


def main():
    """
    This is the script will be run by `streamlit-project-tempalte` command
    """
    template = CreateTemplate()

    parser = argparse.ArgumentParser(
        prog='Streamlit Project Template',
        description='A piece of script to create a project template for \
          mostly advanced streamlit applications',
        epilog='Text at the bottom of help')

    parser.add_argument('createtemplate')

    args = parser.parse_args()

    if args.createtemplate == 'createtemplate':
        template.create_template()
