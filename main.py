import streamlit as st
from streamlit_option_menu import option_menu

import predict
import visualize_h

def main():
    st.markdown("""
        <style>
        .menu-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: white;
            padding: 5px;
            border-radius: 5px;
        }
        .menu-container .menu-title {
            font-size: 20px;
            font-weight: bold;
        }
        .menu-container .additional-info {
            font-size: 18px;
            color: black;
        }
        </style>
        <div class="menu-container">
            <span class="menu-title"></span>
            <span class="additional-info">Edit by: Ngô Thị Diễm Thúy</span>
        </div>
    """, unsafe_allow_html=True)

    app = option_menu(
        menu_title="MAIN MENU", 
        options=["Dashboard", "Predict"],
        # icons = ["car-front", "calculator", "search", "info-circle-fill"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "5!important", "background-color": 'white'},
            "icon": {"color": "black", "font-size": "23px"}, 
            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "0px", "--hover-color": "#BDE4F5"},
            "nav-link-selected": {"background-color": "#2BB2EF"},
        }
    )

    if app == "Predict":
        predict.app()
    elif app == "Dashboard":
        visualize_h.main()

if __name__ == "__main__":
    main()