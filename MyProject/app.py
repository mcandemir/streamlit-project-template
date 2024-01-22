"""
this is the main module where you set your initial sessions states
and navigate your page with respect to `selected_page` session state
"""

import streamlit as st
from src.pages import HomePage, MyPage1, MyPage2


# page config
st.set_page_config(page_title="My Project", layout="centered", initial_sidebar_state="collapsed")


# set session states
if 'selected_page' not in st.session_state:
    st.session_state['selected_page'] = 'home'


# page navigation
match st.session_state['selected_page']:
    case 'home':
        HomePage.load_home_page()

    case 'mypage1':
        MyPage1.load_mypage1()

    case 'mypage2':
        MyPage2.load_mypage2()
