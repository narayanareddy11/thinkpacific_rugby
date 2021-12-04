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


def page_fiji_players():
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
        st.subheader("Average Rating:")
        st.subheader(f"{average_rating} {star_rating}")
    with right_column:
        st.subheader("Average Rugby:")
        st.subheader(f"{average_sale_by_transaction}")

    st.markdown("""---""")

    row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3, row2_3, row2_spacer4, row2_4, row2_spacer5   = st.columns((.2, 1.6, .2, 1.6, .2, 1.6, .2, 1.6, .2))
    with row2_1:
        unique_games_in_df =  100# df_data_filtered.game_id.nunique()
        str_games = "🏟️ " + str(unique_games_in_df) + " Matches"
        st.markdown(str_games)
    with row2_2:
        unique_teams_in_df =300 #len(np.unique(df_data_filtered.team).tolist())
        t = " Teams"
        if(unique_teams_in_df==1):
            t = " Team"
        str_teams = "🏃‍♂️ " + str(unique_teams_in_df) + t
        st.markdown(str_teams)
    with row2_3:
        total_goals_in_df =  900 #df_data_filtered['goals'].sum()
        str_goals = "🥅 " + str(total_goals_in_df) + " Goals"
        st.markdown(str_goals)
    with row2_4:
        total_shots_in_df =  900 #df_data_filtered['shots_on_goal'].sum()
        str_shots = "👟⚽ " + str(total_shots_in_df) + " Shots"
        st.markdown(str_shots)

    row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
    with row3_1:
        st.markdown("")
        see_data = st.expander('You can click here to see the raw data first 👉')
        with see_data:
            st.dataframe(data=df.reset_index(drop=True))
    st.text('')

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

    st.markdown("""---""")
    
    st.markdown(":two_men_holding_hands: Fiji Rugby \t\t Team")

    #if all_teams_selected == 'Include all available teams':
    row16_spacer1, row16_1, row16_2, row16_3, row16_4, row16_spacer2  = st.columns((0.5, 1.5, 1.5, 1, 2, 0.5))
    with row16_1:
        st.markdown("👟 Shots on Goal")
        st.markdown("🏃‍♂️ Distance (in km)")
        st.markdown("🔁 Passes")
        st.markdown("🤹‍♂️ Possession")
        st.markdown("🤕 Fouls")
        st.markdown("🚫 Offside")
        st.markdown("📐 Corners")
    with row16_2:
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "7") #str(df_match_result.iloc[0]['shots_on_goal']))
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "119.98" )#str(df_match_result.iloc[0]['distance']))
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "302") #str(df_match_result.iloc[0]['total_passes']))
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "0.27") #str(df_match_result.iloc[0]['possession']))
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+"16") #str(df_match_result.iloc[0]['fouls']))
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "5") #str(df_match_result.iloc[0]['offside']))
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "0") #str(df_match_result.iloc[0]['corners']))
    with row16_4:
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "25" )#str(df_match_result.iloc[1]['shots_on_goal']))
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "114")#str(df_match_result.iloc[1]['distance']))
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "834")#str(df_match_result.iloc[1]['total_passes']))
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "4")#str(df_match_result.iloc[1]['possession']))
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "9")#str(df_match_result.iloc[1]['fouls']))
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "6")#str(df_match_result.iloc[1]['offside']))
        st.markdown(" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ "5") #str(df_match_result.iloc[1]['corners']))

   # import streamlit as st
   # import matplotlib.pyplot as plt


    st.markdown("""---""")
    st.markdown(":two_men_holding_hands: Fiji Rugby \t\t Team")
    
    
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    
    plt.title('Sports Attainment \n\n \n \n', fontsize=14, pad=20)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

   # st.pyplot(fig1)
    


 
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

# #SALES BY HOUR [BAR CHART]
#     sales_by_hour = df_selection.groupby(by=["RPI Score"]).sum()[["Influence"]]
#     fig_hourly_sales = px.bar(
#     sales_by_hour,
#     x=sales_by_hour.index,
#     y="Influence",
#     title="<b>RPI Score by Influence</b>",
#     color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
#     template="plotly_white",
# )
#     fig_hourly_sales.update_layout(
#     xaxis=dict(tickmode="linear"),
#     plot_bgcolor="rgba(0,0,0,0)",
#     yaxis=(dict(showgrid=False)),
# )

    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
    right_column.pyplot(fig1)
  #  right_column.plotly_chart(fig_product_sales, use_container_width=True)
  
    st.markdown("""---""")
    st.markdown(":two_men_holding_hands: Fiji Rugby \t\t Team")
  
    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    # Group data together
    hist_data = [x1, x2, x3]
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    # Create distplot with custom bin_size
    fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])
    # Plot!
    st.plotly_chart(fig, use_container_width=True)
    
    
    
    