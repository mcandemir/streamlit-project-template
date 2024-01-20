import streamlit as st


def _set_page_home():
    st.session_state['selected_page'] = 'home'

def _set_state_something():
    st.session_state['state'] = 'something'
