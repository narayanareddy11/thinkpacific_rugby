# -*- coding: utf-8 -*-
"""
Created on 10 Nov 2021

"""
# Package imports
import streamlit as st


import pandas as pd
import matplotlib.pyplot as plt
import cmasher as cmr
import numpy as np
from bokeh.plotting import figure
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
# Use random seed
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

def page_fit():




    mypath = "images"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    list1= [] 
    for end1 in onlyfiles:
        dd= end1.split(".")[0]
        list1.append(dd)

        
   # print(list1)
   # print(onlyfiles)

    option = st.selectbox(
        'How would you like to be contacted?',
        (list1))

    #st.write('You selected:', option)


    col1, col2 = st.columns([1,1])
    col1.subheader('Player info ')
    image = Image.open('images/'+ option+'.png')
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






    #st.set_page_config(layout="wide")

    ### Data Import ###
    df_database = pd.read_csv("data_BuLi_13_20_cleaned.csv")
    types = ["Mean","Absolute","Median","Maximum","Minimum"]
    label_attr_dict = {"Goals":"goals","Halftime Goals":"ht_goals","Shots on Goal":"shots_on_goal","Distance Covered (in km)":"distance","Passes":"total_passes", "Successful Passes":"success_passes", "Failed Passes":"failed_passes", "Pass Success Ratio":"pass_ratio", "Ball Possession":"possession", "Tackle Success Ratio":"tackle_ratio", "Fouls Committed":"fouls", "Fouls Received":"got_fouled", "Offsides":"offside", "Corners":"corners"}
    label_attr_dict_teams = {"Goals Scored":"goals","Goals Received":"goals_received","Halftime Goals Scored":"ht_goals","Halftime Goals Received":"halftime_goals_received","Shots on opposing Goal":"shots_on_goal","Shots on own Goal":"shots_on_goal_received","Distance Covered (in km)":"distance","Passes":"total_passes", "Successful Passes":"success_passes", "Failed Passes":"failed_passes", "Pass Success Ratio":"pass_ratio", "Ball Possession":"possession", "Tackle Success Ratio":"tackle_ratio", "Fouls Committed":"fouls", "Fouls Received":"got_fouled", "Offsides":"offside", "Corners":"corners"}
    color_dict = {'1. FC Köln': '#fc4744', '1. FC Nürnberg':'#8c0303', '1. FC Union Berlin':'#edd134', '1. FSV Mainz 05':'#fa2323', 'Bayer 04 Leverkusen':'#cf0c0c', 'Bayern München':'#e62222', 'Bor. Mönchengladbach':'#1f9900', 'Borussia Dortmund':'#fff830', 'Eintracht Braunschweig':'#dbca12', 'Eintracht Frankfurt':'#d10606', 'FC Augsburg':'#007512', 'FC Ingolstadt 04':'#b50300', 'FC Schalke 04':'#1c2afc', 'Fortuna Düsseldorf':'#eb3838', 'Hamburger SV':'#061fc2', 'Hannover 96':'#127a18', 'Hertha BSC':'#005ac2', 'RB Leipzig':'#0707a8', 'SC Freiburg':'#d1332e', 'SC Paderborn 07':'#0546b5', 'SV Darmstadt 98':'#265ade', 'TSG Hoffenheim':'#2b82d9', 'VfB Stuttgart':'#f57171', 'VfL Wolfsburg':'#38d433', 'Werder Bremen':'#10a30b'}
    label_attr_dict_correlation = {"Goals":"delta_goals", "Halftime Goals":"delta_ht_goals","Shots on Goal":"delta_shots_on_goal","Distance Covered (in km)":"delta_distance","Passes":"delta_total_passes","Pass Sucess Ratio":"delta_pass_ratio","Possession":"delta_possession","Tackle Success Ratio":"delta_tackle_ratio","Fouls":"delta_fouls","Offside":"delta_offside","Corners":"delta_corners"}
    label_fact_dict = {"goals scored":'goals',"halftime goals scored":'ht_goals',"shots on the goal":'shots_on_goal',"distance covered (in km)":'distance',"total passes":'total_passes',"pass ratio":'pass_ratio',"possession ratio":'possession',"successful tackle ratio":'tackle_ratio',"fouls":'fouls',"offsides":'offside',"corners":'corners'}

    ### Helper Methods ###
    def get_unique_seasons_modified(df_data):
        #returns unique season list in the form "Season 13/14" for labels
        unique_seasons = np.unique(df_data.season).tolist()
        seasons_modified = []
        for s,season in enumerate(unique_seasons):
            if s==0:
                season = "‏‏‎ ‎‏‏‎ ‎" + season
            if s==len(unique_seasons)-1:
                season = season + "‏‏‎ ‎‏‏‎ ‎"
            seasons_modified.append(season.replace("-","/"))
        return seasons_modified

    def get_unique_matchdays(df_data):
        #returns minimum and maximum
        return np.unique(df_data.matchday).tolist()

    def get_unique_teams(df_data):
        unique_teams = np.unique(df_data.team).tolist()
        return unique_teams

    def filter_season(df_data):
        df_filtered_season = pd.DataFrame()
        seasons = np.unique(df_data.season).tolist() #season list "13-14"
        start_raw ='13-14' # start_season.replace("/","-").replace("‏‏‎ ‎‏‏‎ ‎","") #get raw start season "13-14"
        end_raw = '19-20' #end_season.replace("/","-").replace("‏‏‎ ‎‏‏‎ ‎","") #get raw end season "19-20"
        start_index = seasons.index(start_raw)
        end_index = seasons.index(end_raw)+1
        seasons_selected = seasons[start_index:end_index]
        df_filtered_season = df_data[df_data['season'].isin(seasons_selected)]
        return df_filtered_season

    def filter_matchday(df_data):
        df_filtered_matchday = pd.DataFrame()
        matchdays_list = list(range(0, 19))
        df_filtered_matchday = df_data[df_data['matchday'].isin(matchdays_list)]
        return df_filtered_matchday

    def filter_teams(df_data):
        df_filtered_team = pd.DataFrame()
        if all_teams_selected == 'Select teams manually (choose below)':
            df_filtered_team = df_data[df_data['team'].isin(selected_teams)]
            return df_filtered_team
        return df_data

    def stack_home_away_dataframe(df_data):
        df_data["game_id"] = df_data.index + 1
        delta_names = ['goals','ht_goals','shots_on_goal','distance','total_passes','pass_ratio','possession','tackle_ratio','fouls','offside','corners']
        for column in delta_names:
            h_delta_column = 'h_delta_'+ column
            a_delta_column = 'a_delta_'+ column
            h_column = 'h_'+ column
            a_column = 'a_'+ column
            df_data[h_delta_column] = df_data[h_column]-df_data[a_column]
            df_data[a_delta_column] = df_data[a_column]-df_data[h_column]
        #st.dataframe(data=df_data)
        column_names = ['distance','total_passes','success_passes','failed_passes','pass_ratio','possession','tackle_ratio','offside','corners','delta_goals','delta_ht_goals','delta_shots_on_goal','delta_distance','delta_total_passes','delta_pass_ratio','delta_possession','delta_tackle_ratio','delta_fouls','delta_offside','delta_corners']
        h_column_names = ['game_id','season','matchday','h_team','h_goals','a_goals','h_ht_goals','a_ht_goals','h_shots_on_goal','a_shots_on_goal','h_fouls','a_fouls']
        a_column_names = ['game_id','season','matchday','a_team','a_goals','h_goals','a_ht_goals','h_ht_goals','a_shots_on_goal','h_shots_on_goal','a_fouls','h_fouls']
        column_names_new = ['game_id','season','matchday','location','team','goals','goals_received','ht_goals','ht_goals_received','shots_on_goal','shots_on_goal_received','fouls','got_fouled','distance','total_passes','success_passes','failed_passes','pass_ratio','possession','tackle_ratio','offside','corners','delta_goals','delta_ht_goals','delta_shots_on_goal','delta_distance','delta_total_passes','delta_pass_ratio','delta_possession','delta_tackle_ratio','delta_fouls','delta_offside','delta_corners']
        for column in column_names: 
            h_column_names.append("h_" + column)
            a_column_names.append("a_" + column)
        df_home = df_data.filter(h_column_names)
        df_away = df_data.filter(a_column_names)
        df_home.insert(3,'location','h')
        df_away.insert(3,'location','a')
        df_home.columns = column_names_new
        df_away.columns = column_names_new
        df_total = df_home.append(df_away, ignore_index=True).sort_values(['game_id','season', 'matchday'], ascending=[True,True, True])
        df_total_sorted = df_total[['game_id','season','matchday','location','team','goals','goals_received','delta_goals','ht_goals','ht_goals_received','delta_ht_goals','shots_on_goal','shots_on_goal_received','delta_shots_on_goal','distance','delta_distance','total_passes','delta_total_passes','success_passes','failed_passes','pass_ratio','delta_pass_ratio','possession','delta_possession','tackle_ratio','delta_tackle_ratio','fouls','got_fouled','delta_fouls','offside','delta_offside','corners','delta_corners']]
        return df_total_sorted

    def group_measure_by_attribute(aspect,attribute,measure):
        df_data = df_data_filtered
        df_return = pd.DataFrame()
        if(measure == "Absolute"):
            if(attribute == "pass_ratio" or attribute == "tackle_ratio" or attribute == "possession"):
                measure = "Mean"
            else:
                df_return = df_data.groupby([aspect]).sum()            
        
        if(measure == "Mean"):
            df_return = df_data.groupby([aspect]).mean()
            
        if(measure == "Median"):
            df_return = df_data.groupby([aspect]).median()
        
        if(measure == "Minimum"):
            df_return = df_data.groupby([aspect]).min()
        
        if(measure == "Maximum"):
            df_return = df_data.groupby([aspect]).max()
        
        df_return["aspect"] = df_return.index
        if aspect == "team":
            df_return = df_return.sort_values(by=[attribute], ascending = False)
        return df_return
        
    ########################
    ### ANALYSIS METHODS ###
    ########################

    def plot_x_per_team(attr,measure): #total #against, #conceived
        rc = {'figure.figsize':(8,4.5),
            'axes.facecolor':'#0e1117',
            'axes.edgecolor': '#0e1117',
            'axes.labelcolor': 'white',
            'figure.facecolor': '#0e1117',
            'patch.edgecolor': '#0e1117',
            'text.color': 'white',
            'xtick.color': 'white',
            'ytick.color': 'white',
            'grid.color': 'grey',
            'font.size' : 8,
            'axes.labelsize': 12,
            'xtick.labelsize': 8,
            'ytick.labelsize': 12}
        
        plt.rcParams.update(rc)
        fig, ax = plt.subplots()
        ### Goals
        attribute = label_attr_dict_teams[attr]
        df_plot = pd.DataFrame()
        df_plot = group_measure_by_attribute("team",attribute,measure)
        if specific_team_colors:
            ax = sns.barplot(x="aspect", y=attribute, data=df_plot.reset_index(), palette = color_dict)
        else:
            ax = sns.barplot(x="aspect", y=attribute, data=df_plot.reset_index(), color = "#b80606")
        y_str = measure + " " + attr + " " + "per Game"
        if measure == "Absolute":
            y_str = measure + " " + attr
        if measure == "Minimum" or measure == "Maximum":
            y_str = measure + " " + attr + "in a Game"
        ax.set(xlabel = "Team", ylabel = y_str)
        plt.xticks(rotation=66,horizontalalignment="right")
        if measure == "Mean" or attribute in ["distance","pass_ratio","possession","tackle_ratio"]:
            for p in ax.patches:
                ax.annotate(format(p.get_height(), '.2f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha = 'center',
                    va = 'center', 
                    xytext = (0, 18),
                    rotation = 90,
                    textcoords = 'offset points')
        else:
            for p in ax.patches:
                ax.annotate(format(str(int(p.get_height()))), 
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha = 'center',
                    va = 'center', 
                    xytext = (0, 18),
                    rotation = 90,
                    textcoords = 'offset points')
        st.pyplot(fig)

    def plt_attribute_correlation(aspect1, aspect2):
        df_plot = df_data_filtered
        rc = {'figure.figsize':(5,5),
            'axes.facecolor':'#0e1117',
            'axes.edgecolor': '#0e1117',
            'axes.labelcolor': 'white',
            'figure.facecolor': '#0e1117',
            'patch.edgecolor': '#0e1117',
            'text.color': 'white',
            'xtick.color': 'white',
            'ytick.color': 'white',
            'grid.color': 'grey',
            'font.size' : 8,
            'axes.labelsize': 12,
            'xtick.labelsize': 12,
            'ytick.labelsize': 12}
        plt.rcParams.update(rc)
        fig, ax = plt.subplots()
        asp1 = label_attr_dict_correlation[aspect1]
        asp2 = label_attr_dict_correlation[aspect2]
        if(corr_type=="Regression Plot (Recommended)"):
            ax = sns.regplot(x=asp1, y=asp2, x_jitter=.1, data=df_plot, color = '#f21111',scatter_kws={"color": "#f21111"},line_kws={"color": "#c2dbfc"})
        if(corr_type=="Standard Scatter Plot"):
            ax = sns.scatterplot(x=asp1, y=asp2, data=df_plot, color = '#f21111')
        #if(corr_type=="Violin Plot (High Computation)"):
        #    ax = sns.violinplot(x=asp1, y=asp2, data=df_plot, color = '#f21111')
        ax.set(xlabel = aspect1, ylabel = aspect2)
        st.pyplot(fig, ax)

    
    row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))

    df_stacked = stack_home_away_dataframe(df_database)

    # st.sidebar.text('')
    # st.sidebar.text('')
    # st.sidebar.text('')
    ### SEASON RANGE ###
    # st.sidebar.markdown("**First select the data range you want to analyze:** 👇")
    unique_seasons = get_unique_seasons_modified(df_database)
    #start_season, end_season = st.sidebar.select_slider('Select the season range you want to include', unique_seasons, value = ["‏‏‎ ‎‏‏‎ ‎13/14","19/20‏‏‎ ‎‏‏‎ ‎"])
    df_data_filtered_season = filter_season(df_stacked)        

    # ### MATCHDAY RANGE ###
    unique_matchdays = get_unique_matchdays(df_data_filtered_season) #min and max matchday
    #selected_matchdays =  '19' #st.sidebar.select_slider('Select the matchday range you want to include', unique_matchdays, value=[min(unique_matchdays),max(unique_matchdays)])
    df_data_filtered_matchday = filter_matchday(df_data_filtered_season)        

    # ### TEAM SELECTION ###
    unique_teams = get_unique_teams(df_data_filtered_matchday)
    all_teams_selected = st.sidebar.selectbox('Do you want to only include specific teams? If the answer is yes, please check the box below and then select the team(s) in the new field.', ['Include all available teams','Select teams manually (choose below)'])
    # if all_teams_selected == 'Select teams manually (choose below)':
    #     selected_teams = st.sidebar.multiselect("Select and deselect the teams you would like to include in the analysis. You can clear the current selection by clicking the corresponding x-button on the right", unique_teams, default = unique_teams)
    df_data_filtered = filter_teams(df_data_filtered_matchday) 
    
       # df = get_data_from_excel()
    df_data_1_F = get_data_from_excel("fiji_rugby.xlsx", option)
   # dimensions = df_data_1_F.shape
    #print(dimensions,"iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print(df_data_1_F.iloc[-1:],"ppppppppppppp")
    
    uuu= df_data_1_F.tail(1)
    #print("jjjjjjjjj", df_data_1_F["Matches"].iloc[-1], "llllllllllllllllllllll")
    
    ### SEE DATA ###
    row6_spacer1, row6_1, row6_spacer2 = st.columns((.2, 7.1, .2))
    with row6_1:
        st.subheader("Currently selected data:")

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
        total_shots_in_df = df_data_filtered['shots_on_goal'].sum()
        str_shots = "👟⚽ " + df_data_1_F["Min"].iloc[-1] + "  Min"
       # str_goals = "🥅 " + df_data_1_F["Starter"].iloc[-1] + "Starter"

        st.markdown(str_shots)

    row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
    with row3_1:
        st.markdown("")
        
        str_shots = "👟⚽ " + df_data_1_F["Min"].iloc[-1] + " Min"


        see_data = st.expander('You 1 can click here to see the raw data first 👉')
        with see_data:
            st.dataframe(data=df_data_1_F.reset_index(drop=True))
    st.text('')



    ### TEAM ###
    row4_spacer1, row4_1, row4_spacer2 = st.columns((.2, 7.1, .2))
    with row4_1:
        st.subheader('Analysis per Team')
    row5_spacer1, row5_1, row5_spacer2, row5_2, row5_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
    with row5_1:
        st.markdown('Investigate a vtttttttttttttttttt    es the most goals per game? How does your team compare in terms of distance ran per game?')    
        plot_x_per_team_selected = st.selectbox ("Which attribute do you want to analyze?", list(label_attr_dict_teams.keys()), key = 'attribute_team')
        plot_x_per_team_type = st.selectbox ("Which measure do you want to analyze?", types, key = 'measure_team')
        specific_team_colors = st.checkbox("Use team specific color scheme")
    with row5_2:
        if all_teams_selected != 'Select teams manually (choose below)' or selected_teams:
            plot_x_per_team(plot_x_per_team_selected, plot_x_per_team_type)
        else:
            st.warning('Please select at least one team')
            
    
    


   # import streamlit as st
   # import matplotlib.pyplot as plt

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    
    data_Position = dict(df_player_info['Position'].value_counts())#df_player_info.Position.value_counts().to_frame()
    
   # for i in data_Position:
    #    print(i, "ooooo")
    print(data_Position.keys, "tttttttttttttttttttttttt", data_Position.values())
    
    labels = data_Position.keys()
    sizes = data_Position.values()
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    
    
    

    #import streamlit as st


    # source = data.seattle_weather()

    # c = alt.Chart(source).mark_bar(
    #     cornerRadiusTopLeft=3,
    #     cornerRadiusTopRight=3
    # ).encode(
    #     x='month(date):O',
    #     y='count():Q',
    #     color='weather:N'
    # )

    # st.write(c)