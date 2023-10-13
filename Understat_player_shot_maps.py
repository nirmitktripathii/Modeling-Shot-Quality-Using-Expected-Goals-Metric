# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 23:56:12 2021

@author: Nirmit
"""


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch,VerticalPitch
from highlight_text import fig_text
import matplotlib.patches as mpatches
from Understat_shot_maps import Understat_Shots_Map
from player_dictionary_threading import main



pldict = main() 
'''Python function file which returns the player_dictionary 
containing player_name-player_id as key-vallue pairs'''

text_color = '#ddced4'
player_name = ['Lionel Messi', 'Cristiano Ronaldo']
season = '2020'

pl_id = [(pldict[player]) for player in player_name]

df_list = Understat_Shots_Map(pl_id,player_name,season) 
'''Python function file, 
which takes in the player name and the year/season during which we want
 our shots data to be from (optional argument, if not given, gives shot 
data for all the available seasons) as arguments and returns a dataframe 
containing all the shots data from the particular season (seasons) and 
from that particular player. '''
     
for df in df_list:
    # df = pd.read_csv(path_name)
    df['X'] = pd.to_numeric(df['X'])
    df['Y'] = pd.to_numeric(df['Y'])
    df['xG'] = pd.to_numeric(df['xG'])
    df['minute'] = pd.to_numeric(df['minute'])
    
    df['X'] = df['X']*100
    df['Y'] = df['Y']*100
    
    df['xx'] = df['Y']
    df['yy'] = df['X']
    
    df['X'] = df['xx']
    df['Y'] = df['yy']
    
    df['X'] = df['X']*.8
    df['Y'] = df['Y']*1.2
    
    
    def plotShotMap():
        for x in range(len(df['X'])):
            if df['result'][x] == 'Goal': 
                    plt.scatter(df['X'][x],df['Y'][x], color = '#74c69d',s=df['xG'][x]*500,edgecolor='white',linewidth=2,alpha=.9)            
            elif df['result'][x] == 'MissedShots': 
                    plt.scatter(df['X'][x],df['Y'][x], color = '#E64C4C',s=df['xG'][x]*500,edgecolor='white',linewidth=2,alpha=.9)       
            elif df['result'][x] == 'BlockedShot': 
                    plt.scatter(df['X'][x],df['Y'][x], color = '#FFF712',s=df['xG'][x]*500,edgecolor='white',linewidth=2,alpha=.9)       
            elif df['result'][x] == 'SavedShot': 
                    plt.scatter(df['X'][x],df['Y'][x], color = '#111ED9',s=df['xG'][x]*500,edgecolor='white',linewidth=2,alpha=.9) 
            else:
                    plt.scatter(df['X'][x],df['Y'][x], color = '#F0F0F0',s=df['xG'][x]*500,edgecolor='white',linewidth=2,alpha=.9)
    
       
    
    fig, ax = plt.subplots(figsize=(13,8.5))
    fig.set_facecolor('#22312b')
    ax.patch.set_facecolor('#22312b')
    
    pitch = VerticalPitch(pitch_type='statsbomb', half = True,
                  pitch_color='#aabb97',stripe_color='#c2d59d', stripe=True, line_color='#c7d5cc', figsize=(13, 8),
                  constrained_layout=False, tight_layout=True)
    
    
    
    pitch.draw(ax=ax)
    
    # plt.ylim(0,60)
    
    plotShotMap()
    
    #The statsbomb pitch from mplsoccer
    
    s=f'{df.player[0]} Shot Map for 2020/21 season'
    fig_text(s=s,
            x=.23,y=.95,
            fontfamily='Andale Mono',
            fontsize=24,
            color='#ddced4'
    
    )
    
    total_shots = len(df)
    from matplotlib.lines import Line2D
    patches = []
    colors = ['#74c69d','#E64C4C','#FFF712','#111ED9','#F0F0F0'] 
    labels = ['Goals', 'Missed Shots', 'Blocked Shots', 'Saved Shots', 'Shots on Target']
    patches = [plt.plot([],[], marker="o",color=colors[i], label=labels[i],ms=10, ls="", mec=None,)[0] for i in range(len(df['result'].unique()))]
    
    plt.legend(handles=patches,loc = 'upper right',facecolor = 'black',labelcolor = text_color)
    # plt.legend()
    
    
    fig_text(s=f'Total Shots: {total_shots}',
            x=.27, y =.2, fontsize=14,fontfamily='Andale Mono',color='#554468')
    fig.text(.25,0.05,f'@NTripathii / twitter',fontstyle='italic',fontsize=12,fontfamily='Andale Mono',color=text_color)
    
    fig.text(.585,0.05,'*Circle radius proportional to xG',fontstyle='italic',fontsize=11,fontfamily='Andale Mono',color=text_color)
    
    
