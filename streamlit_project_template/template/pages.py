import streamlit as st
import components



# HOME PAGE ================================================================================
class HomePage():
    """
    Your Home / Landing Page

    Here you can add your defined components under the loadPage() function
    """
    @staticmethod
    def loadHomePage(): 
        components.component_say_hello()


# EXAMPLE PAGE ================================================================================
class MyPage1():
    """
    Example Page 1
    """
    @staticmethod
    def loadMyPage1():        
        pass


# ML PAGE ================================================================================
class MyPage2():
    """
    Example Page 2
    """
    @staticmethod
    def loadMyPage2():
        pass
