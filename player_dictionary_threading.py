# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 23:37:38 2021

@author: Nirmit
"""
def main():
    import threading
    from concurrent.futures import ThreadPoolExecutor
    from bs4 import BeautifulSoup
    import numpy as np
    
    import requests
    import pandas as pd
    # from understat import Understat
    import time 
    l1 = range(1,9610)
    player_dict = {}
    t=[]
    t_mean = []
    url = "https://understat.com/player/"
    url_list = [url+str(id) for id in l1]
    
    def dict_player(url):
        
        try:
          page = requests.get(url)
          # pageconnect = urlopen(url)
          page_html = BeautifulSoup(page.text, "html.parser")
          
          name = (str(page_html.title.text).split(' |')[0])
          # print(id)
          player_dict[name] = url.split('/')[-1]
           
        except KeyError:
            pass    
        except AttributeError:
            pass
        
    
    threads = [threading.Thread(target=dict_player, args=(url,)) for url in url_list]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
  
    
    return player_dict