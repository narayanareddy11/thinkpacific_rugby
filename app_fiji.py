# -*- coding: utf-8 -*-
"""
Created on 10 Nov 2021
"""
# Streamlit
import streamlit as st
# Add pages -- see those files for deatils within
from fiji_rugby import fiji_rugby1
from rugby import rugby1
from PIL import Image
# Use random seed
import numpy as np
np.random.seed(1)

# Set the default elements on the sidebar
#st.set_page_config(page_title='Fiji Analyser')
st.set_page_config(page_title="Fiji Rugby", page_icon=":palm_tree:", layout="wide")

logo, name = st.sidebar.columns(2)
with logo:
    image = Image.open('dd.PNG')
    st.image(image, caption=None)

with name:
    st.markdown("<h1 style='text-align: left; color: grey;'> \
                Fiji Analyser </h1>", unsafe_allow_html=True)

#st.sidebar.write(" ")
def main():
    """
    Register pages to Explore and Fit:
        page_fiji_players - contains page with players data and brief explanations
        page_Fiji_performance - contains various functions that allows player performance and data reading from xlsx
        
    """

    pages = {
        "Rugby": rugby1,
        "fiji_Rugby": fiji_rugby1,
    }

    #st.sidebar.title("Main options")

    # Radio buttons to select desired option
    page = st.sidebar.radio("Select:", tuple(pages.keys()))
                                
    # Display the selected page with the session state
    pages[page]()

    # Write About
    side = st.sidebar
    side.header('Fiji Contact')
    side.write("📧 info@thinkpacific.com")
    side.write("📲 +44 113 335 9919")
  #  side.write("[![Star](https://img.shields.io/github/stars/dmf95/nhl-expansion-twitter-app.svg?logo=github&style=social)](https://github.com/dmf95/nhl-expansion-twitter-app)")
    side.write("[![Follow](https://img.shields.io/twitter/follow/@thinkpacific?style=social)](https://twitter.com/@thinkpacific)")
    
if __name__ == "__main__":
    main()


#  ---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
  #  st.markdown(hide_st_style, unsafe_allow_html=True)