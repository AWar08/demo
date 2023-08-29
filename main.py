import streamlit as st

from streamlit_option_menu import option_menu


import app1, account
st.set_page_config(
        page_title="Main Menu",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Main Menu',
                options=['Account','App','About'],
                icons=["person-circle","p-circle","info-circle"],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )
            
        if app == "About":
         st.sidebar.header("About")
         st.sidebar.info("ZONE 1 = Infront of the main office")
         st.sidebar.info("ZONE 2 = Infront of civil department ")
         st.sidebar.info("ZONE 3 = Infront of the mini canteen")

        
        if app == "Account":
            account.app()
        if app == "App":
            app1.app()        
             
    run()            
         