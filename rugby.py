# -*- coding: utf-8 -*-
"""
Created on 10 Nov 2021

"""
import streamlit as st
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import numpy as np


@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="Kaggle Six Nations.xlsx",
        engine="openpyxl",
        sheet_name="All player stats",
    # skiprows=3,
        usecols="A:BR",
        nrows=220,
    )
    # Add 'hour' column to dataframe
    #df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df


@st.cache
def get_data_from_excel1(io, sheet_name, usecols, nrows):
    df = pd.read_excel(
        io=io,
        engine="openpyxl",
        sheet_name=sheet_name,
    # skiprows=3,
        usecols= usecols, #"A:BR",
        nrows= nrows #220,
    )
    return df

def Cumulativ(get_data_from_excel1):
    df2=get_data_from_excel1("Kaggle Six Nations.xlsx", "Cumulativ Awards, Participation", "A:N", 8)
    return df2



def pie_chart():
#  print(df2)
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
    df2 = Cumulativ(get_data_from_excel1)

    labe_pie = (df2.iloc[:, 0].tolist())
    labe_pie1 = '", "'.join(str(e) for e in labe_pie)
    labe_pie13= '"' +labe_pie1 + '"' 
  #  print(labe_pie13, "rrrrrrrr")
    return tuple(labe_pie)

def pie_chart2():
   # df2=get_data_from_excel1("Kaggle Six Nations.xlsx", "Cumulativ Awards, Participation", "A:N", 8)
#  print(df2)
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
    df2 = Cumulativ(get_data_from_excel1)

    labe_pie = df2.iloc[:, 9].tolist()
   # labe_pie1 = '", "'.join(str(e) for e in labe_pie)
  #  labe_pie13= '"' +labe_pie1 + '"' 
  #  print(labe_pie, "nnnnnnnnnnnnnnnnnnnnn")
    return list(labe_pie)
    


def rugby1():
    main(get_data_from_excel)

# Players data
def main(get_data_from_excel):
  
    df = get_data_from_excel()
    Country = st.sidebar.multiselect(
    "Select the Country:",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)
    Forward_Back = st.sidebar.multiselect(
    "Select the Forward_Back:",
    options=df["Forward_Back"].unique(),
    default=df["Forward_Back"].unique()
)

    df_selection = df.query(
    "Country == @Country & Forward_Back == @Forward_Back"
)

    total_sales = int(df_selection["RPI Score"].sum())
    average_rating = round(df_selection["Six Nations Won"].mean(), 1)
    star_rating = ":star:" * int(round(average_rating, 0))
    average_sale_by_transaction = round(df_selection["RPI Score"].mean(), 2)


    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader("RPI Scores:")
        st.subheader(f"{total_sales:,}")
    with middle_column:
        st.subheader("Avg Rating:")
        st.subheader(f"{average_rating} {star_rating}")
    with right_column:
        st.subheader("Avg Rugby:")
        st.subheader(f"{average_sale_by_transaction}")

    st.markdown("""---""")

    row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3, row2_3, row2_spacer4, row2_4, row2_spacer5   = st.columns((.2, 1.6, .2, 1.6, .2, 1.6, .2, 1.6, .2))
    with row2_1:
        unique_games_in_df =  df_selection.Club.nunique()
        str_games = "🏟️ " + str(unique_games_in_df) + " Club"
        st.markdown(str_games)
    with row2_2:
        unique_teams_in_df_1 = df_selection.Player.nunique() #len(np.unique(df_data_filtered.team).tolist())
        str_games_1 = "🏃‍♂️ " + str(unique_teams_in_df_1) + " Players"
        st.markdown(str_games_1)
        # t = " Player"
        # if(unique_teams_in_df==1):
        #     t = " Team"
        # str_teams = "🏃‍♂️ " + str(unique_teams_in_df) + t
        # st.markdown(str_teams)
    with row2_3:
        total_goals_in_df =  df_selection.Country.nunique()
        str_goals = "🥅 " + str(total_goals_in_df) + " Country"
        st.markdown(str_goals)
    with row2_4:
        total_shots_in_df = df_selection.Forward_Back.value_counts()
        str_shots = "👟⚽  For: " + str(total_shots_in_df[0]) + " Back: "+str(total_shots_in_df[1] ) #+ " - Forward_Back"
        st.markdown(str_shots)

    row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
    with row3_1:
        st.markdown("")
        see_data = st.expander('You can click here to see the raw data first 👉')
        with see_data:
            st.dataframe(data=df.reset_index(drop=True))
    st.text('')

#----------------------------------------------------------------------


    st.markdown(":two_men_holding_hands: Rugby 6 Nations Predictor Rugby")
    
    df2=get_data_from_excel1("Kaggle Six Nations.xlsx", "Cumulativ Awards, Participation", "A:N", 8)
    
    

    
    labels =  pie_chart() #('England', 'France', 'Ireland', 'Italy', 'Scotland', 'Wales') 
  #  print(labels, "lllllllllllll", type(labels))
    sizes = pie_chart2() #[382154, 38214, 32154, 38215, 38215,38215]
   # print(sizes, "kkkkkkkk31111111111kkkkkk", type(sizes)) 
    
    
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    
    plt.title('Registered Players by  Country \n\n \n \n', fontsize=14, pad=20)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.



# --------      Bar chart 

    sales_by_product_line = (
#  df_selection.groupby(by=["Country"]).sum()[["RPI Scores"]]
    df2.groupby(by=["Country"]).sum()[["Total players"]].sort_values(by="Total players")

)
    fiji_fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total players",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Rugby Total players by Country </b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
    fiji_fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fiji_fig_product_sales, use_container_width=True)
    right_column.pyplot(fig1)
  #  right_column.plotly_chart(fig_product_sales, use_container_width=True)
  
  #--------------------------------------------------------------------------------------------

    st.markdown("""---""")
    
    df3 = get_data_from_excel1("Kaggle Six Nations.xlsx", "2019 Team Stats", "A:N", 7)
   # print(df3)

    st.markdown(":two_men_holding_hands: 2019 Team Rugby Stats \t\t Team")

    #if all_teams_selected == 'Include all available teams':
    row16_spacer1, row16_1, row16_2, row16_3, row16_4, row16_5, row16_6, row16_7,row16_8,row16_9,row16_spacer2  = st.columns((0.5, 1.2, 1.2, 1, 1.2,1.2, 1.2,1.2,1.2,1.2,0.5))
    with row16_1:
        st.markdown('🤹‍♂️**Country **')
        st.markdown(str(df3.iloc[0]['Country']))
        st.markdown(str(df3.iloc[1]['Country']))
        st.markdown(str(df3.iloc[2]['Country']))
        st.markdown(str(df3.iloc[3]['Country']))
        st.markdown(str(df3.iloc[4]['Country']))
        st.markdown(str(df3.iloc[5]['Country']))
        
                
        # st.markdown("🏃‍♂️ Distance (in km)")
        # st.markdown("🔁 Passes")
        # st.markdown("🤹‍♂️ Possession")
        # st.markdown("🤕 Fouls")
        # st.markdown("🚫 Offside")
        # st.markdown("📐 Corners")
    with row16_2:
        st.markdown('🏉**Points**')
        st.markdown(str(df3.iloc[0]['Points']))
        st.markdown(str(df3.iloc[1]['Points']))
        st.markdown(str(df3.iloc[2]['Points']))
        st.markdown(str(df3.iloc[3]['Points']))
        st.markdown(str(df3.iloc[4]['Points']))
        st.markdown(str(df3.iloc[5]['Points']))
    with row16_3:
        st.markdown('🏆**Tries**')
        st.markdown(str(df3.iloc[0]['Tries']))
        st.markdown(str(df3.iloc[1]['Tries']))
        st.markdown(str(df3.iloc[2]['Tries']))
        st.markdown(str(df3.iloc[3]['Tries']))
        st.markdown(str(df3.iloc[4]['Tries']))
        st.markdown(str(df3.iloc[5]['Tries']))
   
    with row16_4:
        st.markdown('🔁**Conv**')
        st.markdown(str(df3.iloc[0]['Conversions']))
        st.markdown(str(df3.iloc[1]['Conversions']))
        st.markdown(str(df3.iloc[2]['Conversions']))
        st.markdown(str(df3.iloc[3]['Conversions']))
        st.markdown(str(df3.iloc[4]['Conversions']))
        st.markdown(str(df3.iloc[5]['Conversions']))
             
    with row16_5:
        st.markdown('🤕**PenaltY**')
        st.markdown(str(df3.iloc[0]['Penalty Goals']))
        st.markdown(str(df3.iloc[1]['Penalty Goals']))
        st.markdown(str(df3.iloc[2]['Penalty Goals']))
        st.markdown(str(df3.iloc[3]['Penalty Goals']))
        st.markdown(str(df3.iloc[4]['Penalty Goals']))
        st.markdown(str(df3.iloc[5]['Penalty Goals']))
        
    with row16_6:
        st.markdown('🏃‍♂️**Drop**')
        st.markdown(str(df3.iloc[0]['Drop Goals']))
        st.markdown(str(df3.iloc[1]['Drop Goals']))
        st.markdown(str(df3.iloc[2]['Drop Goals']))
        st.markdown(str(df3.iloc[3]['Drop Goals']))
        st.markdown(str(df3.iloc[4]['Drop Goals']))
        st.markdown(str(df3.iloc[5]['Drop Goals']))
        
    with row16_7:
        st.markdown('📐**Metres**')
        st.markdown(str(df3.iloc[0]['Metres Gained']))
        st.markdown(str(df3.iloc[1]['Metres Gained']))
        st.markdown(str(df3.iloc[2]['Metres Gained']))
        st.markdown(str(df3.iloc[3]['Metres Gained']))
        st.markdown(str(df3.iloc[4]['Metres Gained']))
        st.markdown(str(df3.iloc[5]['Metres Gained']))

    with row16_8:
        st.markdown('🚫**Carries**')
        st.markdown(str(df3.iloc[0]['Carries']))
        st.markdown(str(df3.iloc[1]['Carries']))
        st.markdown(str(df3.iloc[2]['Carries']))
        st.markdown(str(df3.iloc[3]['Carries']))
        st.markdown(str(df3.iloc[4]['Carries']))
        st.markdown(str(df3.iloc[5]['Carries']))
    with row16_9:
        st.markdown('🏅**Beaten**')
        st.markdown(str(df3.iloc[0]['Defenders Beaten']))
        st.markdown(str(df3.iloc[1]['Defenders Beaten']))
        st.markdown(str(df3.iloc[2]['Defenders Beaten']))
        st.markdown(str(df3.iloc[3]['Defenders Beaten']))
        st.markdown(str(df3.iloc[4]['Defenders Beaten']))
        st.markdown(str(df3.iloc[5]['Defenders Beaten']))
        

  
  #-------------------------------------------
    st.markdown("""---""")
  
  # SALES BY PRODUCT LINE [BAR CHART]
    sales_by_product_line = (
#  df_selection.groupby(by=["Country"]).sum()[["RPI Scores"]]
    df_selection.groupby(by=["Country"]).sum()[["RPI Score"]].sort_values(by="RPI Score")

)
    fig_product_sales = px.bar(
    sales_by_product_line,
    x="RPI Score",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Rugby by Country </b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
    fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

#SALES BY HOUR [BAR CHART]
    sales_by_hour = df_selection.groupby(by=["RPI Score"]).sum()[["Influence"]]
    fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Influence",
    title="<b>RPI Score by Influence</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)
    fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
    right_column.plotly_chart(fig_product_sales, use_container_width=True)
    
    #-----------------------------

    
    st.markdown("""---""")
    st.markdown(":two_men_holding_hands: Distplot with Rugby Parameters 🏉 ")
    


    # Add histogram data
    x1 =  (df_selection.iloc[:, 21].tolist())
 #np.random.randn(200) - 2
    x2 = (df_selection.iloc[:, 24].tolist())
    x3 = (df_selection.iloc[:, 26].tolist())

   # x3 = np.random.randn(200) + 2
    # Group data together
    hist_data = [x1, x2, x3]
    group_labels = ['Weight In KG', 'RPI Score', 'Influence']
    # Create distplot with custom bin_size
    fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])
    # Plot!
    st.plotly_chart(fig, use_container_width=True)


    
    
    
    