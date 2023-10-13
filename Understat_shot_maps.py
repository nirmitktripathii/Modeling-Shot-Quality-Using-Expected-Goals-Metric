# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 23:56:12 2021

@author: Nirmit
"""

import json
from bs4 import BeautifulSoup, SoupStrainer

from urllib.request import urlopen
import requests
import pandas as pd
# from understat import Understat
import time 
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from mplsoccer.pitch import Pitch,VerticalPitch
# from highlight_text import fig_text
# import matplotlib.patches as mpatches

def Understat_Shots_Map(player_id, player_name, season=0):
    print(player_id)
    t=[]
    df_list = []    
    for id in player_id:
        print(id)
        t0 = time.time()
        url = "https://understat.com/player/"+id
       
        page = requests.get(url)
        
        page_html = BeautifulSoup(page.text, "html.parser")
        print((str(page_html.title.text).split(' |')[0]))
        
        page_html = page_html.findAll('script')[3]
        
        json_raw_string = str(page_html)
        
        istart = json_raw_string.index("(")+2
        iend = json_raw_string.index("')")
        
        json_raw_string = json_raw_string[istart:iend]
        
        json_data = json_raw_string.encode("utf-8").decode("unicode escape")
        
        df = pd.json_normalize(json.loads(json_data))
        
        # player_dict[df['player'][0]] = id
            
        t.append(time.time()-t0)
        
        if season != 0:
            df = df[df['season'] == season].reset_index().drop(labels = 'index', axis = 1)
        else:
            pass
        df_list.append(df)
        df.head()
        # path_name = r'C:\Users\Nirmit\Desktop\Sasta wala Bet365\Football Analysis masterclass\Data Analysis\European Analysis\Player Database\Underrated\\' +player_name+f'\{player_name}_understat_Shots_2021.csv'
        # df.to_csv(path_name, index = False)
    return df_list
        
