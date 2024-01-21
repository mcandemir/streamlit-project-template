"""
this is where you define your components
every component is a piece of row of your application
"""

import streamlit as st
from src import callbacks


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
