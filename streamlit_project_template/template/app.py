import streamlit as st
from pages import HomePage, MyPage1, MyPage2


# page config
st.set_page_config(page_title="My Project", layout="wide", initial_sidebar_state="collapsed")


# set session states
if 'selected_page' not in st.session_state:
    st.session_state['selected_page'] = 'home'


# page navigation
match st.session_state['selected_page']:
    case 'home':
        HomePage.loadHomePage()

    case 'mypage1':
        MyPage1.loadMyPage1()
    
    case 'mypage2':
        MyPage2.loadMyPage2()