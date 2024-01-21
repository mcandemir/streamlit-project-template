import streamlit as st
from src import callbacks


### This is where you define your components. Every component is a piece of your applicaton
def component_say_hello():
    st.button('Home', on_click=callbacks.set_page_home)
    st.header('Hello World!')


def component_change_page():
    st.write('Where do you want to go?')
    st.button('Page 1', on_click=callbacks.set_page_mypage1)
    st.button('Page 2', on_click=callbacks.set_page_mypage2)


def component_mypage1_title():
    st.write('My Page 1')

def component_mypage2_title():
    st.write('My Page 2')