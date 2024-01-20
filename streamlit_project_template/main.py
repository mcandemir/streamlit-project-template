import os
import sys
import argparse
from .createtemplate import CreateTemplate


def main():
    template = CreateTemplate()

    parser = argparse.ArgumentParser(
        prog='Streamlit Project Template',
        description='A piece of script to create a project template for mostly advanced streamlit applications',
        epilog='Text at the bottom of help')

    parser.add_argument('createtemplate')

    args = parser.parse_args()

    if args.createtemplate == 'createtemplate':
        template.createTemplate()


