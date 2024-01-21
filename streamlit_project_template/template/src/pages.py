"""
this is where you define your pages (as classes with static "loadPage" functions)
and build your pages with the components you created
"""

import streamlit as st
from src import components



# HOME PAGE ================================================================================
class HomePage():
    """
    Your Home / Landing Page

    Here you can add your defined components under the loadPage() function
    """
    @staticmethod
    def loadHomePage():
        components.component_say_hello()
        components.component_change_page()


# EXAMPLE PAGE ================================================================================
class MyPage1():
    """
    Example Page 1
    """
    @staticmethod
    def loadMyPage1():
        components.component_say_hello()
        components.component_mypage1_title()


# ML PAGE ================================================================================
class MyPage2():
    """
    Example Page 2
    """
    @staticmethod
    def loadMyPage2():
        components.component_say_hello()
        components.component_mypage2_title()
