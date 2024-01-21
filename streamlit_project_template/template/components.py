import streamlit as st
from src import callbacks


### This is where you define your components. Every component is a piece of your applicaton
def component_say_hello():
    st.header('Hello World!')
