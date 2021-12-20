# -*- coding: utf-8 -*-
"""
Created on 10 Nov 2021

"""
# Package imports
import streamlit as st
import plotly.express as px  # pip install plotly-express


import pandas as pd
import matplotlib.pyplot as plt
import cmasher as cmr
import numpy as np
#from scipy import stats
import scipy.stats
import math, os
from bokeh.plotting import figure
from bokeh.models import Legend
import time
import base64
import collections

import matplotlib.pyplot as plt

import streamlit as st
# Add pages -- see those files for deatils within
#from page_fit import page_fit
#from page_fiji_players import page_fiji_players
from PIL import Image
# Use random seed
import numpy as np

import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from  matplotlib.ticker import FuncFormatter
import seaborn as sns
from os import listdir
from os.path import isfile, join


@st.cache
def get_data_from_excel(File, sheet_name):
    df = pd.read_excel(
        io=File,
        engine="openpyxl",
        sheet_name=sheet_name,
    # skiprows=3,
        usecols="A:O",
        nrows=25,
    )
    # Add 'hour' column to dataframe
    #df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

def fiji_rugby1():
    currentDirectory = os.getcwd()

    mypath =  'images'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    list1= [] 
    for end1 in onlyfiles:
        dd= end1.split(".")[0]
        list1.append(dd)

        
   # print(list1)
   # print(onlyfiles)

    option = st.selectbox(
        'Select Fiji Rugby Player:',
        (list1))

    #st.write('You selected:', option)


    col1, col2 = st.columns([1,1])
    col1.subheader('Player info ')
   # currentDirectory = os.getcwd()
    image = Image.open( 'images/'+ option+'.jpg')
    col1.image(image, caption=None)


    # def plot_x_per_team(attr,measure): #total #against, #conceived
    #     rc = {'figure.figsize':(8,4.5),
    #         'axes.facecolor':'#0e1117',
    #         'axes.edgecolor': '#0e1117',
    #         'axes.labelcolor': 'white',
    #         'figure.facecolor': '#0e1117',
    #         'patch.edgecolor': '#0e1117',
    #         'text.color': 'white',
    #         'xtick.color': 'white',
    #         'ytick.color': 'white',
    #         'grid.color': 'grey',
    #         'font.size' : 8,
    #         'axes.labelsize': 12,
    #         'xtick.labelsize': 8,
    #         'ytick.labelsize': 12}
    #image = Image.open(option+'.PNG')
    #col2.image(image, caption=None)

    df_player_info = get_data_from_excel("fiji_rugby.xlsx", "Players")
  #  print(option, "ooooooooooooooooooooooooooooooo")
    df_player_info = df_player_info.set_index(['Name'])
    # print( df_player_info.loc[option], "nnnnnnnnnnnnnnnnnnnnnnnnn")
    # print( df_player_info.loc[option]['Birthdate'], "nnnnnnnnnnnnnnnnnnnnnnnnn")
    dimensions = df_player_info.shape
    print(dimensions)


    # for name in df_player_info.loc[df_player_info['Name']]: 
    #     if str(name).strip("\n") == str(option).strip("\n"):
    #         print("ggggggggggggggg")
    
    #if df_player_info["Name"] == option:
     #   print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    
    col2.text(' ')
    col2.text(' ')
    col2.text(' ')
    col2.text(' ')
    col2.text(f"Name:  " + str(option))
    col2.text( f"Team: " + str(df_player_info.loc[option.strip()]['Team']) )
    col2.text(
        f"Position:  " + str(df_player_info.loc[option]['Position']))
    col2.text(f"Birthday:  " + str(df_player_info.loc[option]['Birthdate']) )
    col2.text( f"Height:  " + str(df_player_info.loc[option]['Height']))
    col2.text(
        f"Age:  " + str(df_player_info.loc[option]['Age'])
        )
    col2.text(
        f"Height Ft/In:  " + str(df_player_info.loc[option]['Height Ft/In'])
        )
    col2.text(
        f"Weight  st/lb:  " + str(df_player_info.loc[option]['Weight  st/lb'])
        )



       # df = get_data_from_excel()
    df_data_1_F = get_data_from_excel("fiji_rugby.xlsx", option)
   # dimensions = df_data_1_F.shape
    #print(dimensions,"iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
   # print(df_data_1_F.iloc[-1:],"ppppppppppppp")
    
    uuu= df_data_1_F.tail(1)
   # print("jjjjjjjjj", df_data_1_F["Matches"].iloc[-1], "llllllllllllllllllllll")
    
    ### SEE DATA ###
    row6_spacer1, row6_1, row6_spacer2 = st.columns((.2, 7.1, .2))
    with row6_1:
        st.subheader("PLAYER SPECIALITIES:")

    row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3, row2_3, row2_spacer4, row2_4, row2_spacer5   = st.columns((.2, 1.6, .2, 1.6, .2, 1.6, .2, 1.6, .2))
    with row2_1:
       # unique_games_in_df = df_data_filtered.game_id.nunique()
        str_games = "🏟️ " + df_data_1_F["Matches"].iloc[-1] + "  Matches"
        st.markdown(str_games)
    with row2_2:
        
        str_team_w= "🏃‍♂️ " + df_data_1_F["W/D/L"].iloc[-1] + " - W/D/L"
        st.markdown(str_team_w)
    with row2_3:
      #  total_goals_in_df = df_data_filtered['goals'].sum()
      #  str_goals = "🥅 " + str(total_goals_in_df) + " Goals"
        str_goals = "🥅 " + df_data_1_F["Starter"].iloc[-1] + "  Starter"

        st.markdown(str_goals)
    with row2_4:
       # total_shots_in_df = df_data_filtered['shots_on_goal'].sum()
        str_shots = "👟⚽ " + df_data_1_F["Min"].iloc[-1] + "  Min"
       # str_goals = "🥅 " + df_data_1_F["Starter"].iloc[-1] + "Starter"

        st.markdown(str_shots)

    row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
    with row3_1:
        st.markdown("")
        
        str_shots = "👟⚽ " + df_data_1_F["Min"].iloc[-1] + " Min"


        see_data = st.expander('You 1 can click here to see  the 🏃  ' + option  +'   🥅  raw data 👉')
        with see_data:
            st.dataframe(data=df_data_1_F.reset_index(drop=True))



    st.markdown(":two_men_holding_hands: fiji Rugby evaluation using age, weight and matches")
    
    df_data_plyer_st= get_data_from_excel("fiji_rugby.xlsx", "player_st")
    chart_data = pd.DataFrame(
        df_data_plyer_st, #np.random.randn(60, 3),
        
        #index = df_data_plyer_st.iloc[: , :0]
    )
       # columns=["a", "b", "c", "d"])

   # print("gggggggggggggggggg", chart_data, "llllllllllllllllllllllllllllllllll")
    #print("gggggggggggggggggg", df_data_plyer_st, "llllllllllllllllllllllllllllllllll")

    st.bar_chart(chart_data)

    # ### TEAM ###
    # row4_spacer1, row4_1, row4_spacer2 = st.columns((.2, 7.1, .2))
    # with row4_1:
    #     st.subheader('Analysis per Team')
    # row5_spacer1, row5_1, row5_spacer2, row5_2, row5_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
    # with row5_1:
    #     st.markdown('Investigate a vtttttttttttttttttt    es the most goals per game? How does your team compare in terms of distance ran per game?')    
    #     plot_x_per_team_selected = st.selectbox ("Which attribute do you want to analyze?", list(label_attr_dict_teams.keys()), key = 'attribute_team')
    #     plot_x_per_team_type = st.selectbox ("Which measure do you want to analyze?", types, key = 'measure_team')
    #     specific_team_colors = st.checkbox("Use team specific color scheme")
    # with row5_2:
    #     if all_teams_selected != 'Select teams manually (choose below)' or selected_teams:
    #         plot_x_per_team(plot_x_per_team_selected, plot_x_per_team_type)
    #     else:
    #         st.warning('Please select at least one team')
            
    
    

    st.markdown(":two_men_holding_hands: Equal aspect  Position by fiji players")
    
    data_Position = dict(df_player_info['Position'].value_counts())#df_player_info.Position.value_counts().to_frame()
    
   # for i in data_Position:
    #    print(i, "ooooo")
    #print(data_Position.keys, "tttttttttttttttttttttttt", data_Position.values())
    
    labels = data_Position.keys()
    sizes = data_Position.values()
   # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Equal aspect  Position ratio fiji Rugby', fontsize=14, pad=20)
#fig_hourly_sales = st.pyplot(fig1)
    
    #------------------------------------------------------------------------
      #-------------------------------------------
    st.markdown("""---""")
  
  # SALES BY PRODUCT LINE [BAR CHART]
    sales_by_product_line = (
#  df_selection.groupby(by=["Country"]).sum()[["RPI Scores"]]
    df_player_info.groupby(by=["Position"]).sum()[["Fiji"]].sort_values(by="Fiji")

)
    fig_product_sales = px.bar(
    sales_by_product_line,
    x="Fiji",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>RugbyPosition  by Fiji total Matches  </b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
    fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
    
    
    right_column, left_column = st.columns(2)
    left_column.pyplot(fig1, use_container_width=True)
    right_column.plotly_chart(fig_product_sales, use_container_width=True)
    
    #--------------------------------------------------------------------------

    see_data = st.expander('You can click here to see the  fiji players  🏃‍♂️🏃‍♂️ raw data first 👉')
    with see_data:
        st.dataframe(data=df_player_info.reset_index(drop=True))