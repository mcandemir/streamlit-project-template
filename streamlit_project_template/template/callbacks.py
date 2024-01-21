import streamlit as st


def set_page_home():
    st.session_state['selected_page'] = 'home'

def set_page_mypage1():
    st.session_state['selected_page'] = 'mypage1'

def set_page_mypage2():
    st.session_state['selected_page'] = 'mypage2'

def set_state_something():
    st.session_state['state'] = 'something'
