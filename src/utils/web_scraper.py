import requests
import pandas as pd
from tqdm import tqdm
import os, sys; sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from config import *

def get_request_map_positions(recoltable_name: str, skip: int) -> dict:
    """
    Sends an HTTP request to dofus db API that gets a recoltable's map positions
    
    PARAMETERS
    ----------
    recoltable_name: str
        A recoltable name.
    skip: int
        Number of requests elements to skip. 
        Since this specific request has a 10 records limit per request, we will skip incremently 10 to get all the data. 
        
    RETURNS
    -------
    dict
        A json object corresponding to the requests response and contains, the recoltable map positions and quantities per map position. 
    """
    url = DOFUSDB_API_URL
    payload = {'resources[$in][]': RECOLTABLE_IDS[recoltable_name],
               '$skip': skip,
               'lang': 'fr'}
    response = requests.get(url, params=payload)  
    return response.json()

def parse_response(response: dict, recoltable_name: str) -> pd.DataFrame:
    """
    Parses a GET HTTP request and extracts recoltable map positions and quantities per map position

    Parameters
    ----------
    response : dict
        Response returned by GET HTTP request to dofus db on a recoltable map positions
    recoltable_name: str
        A recoltable name.

    Returns
    -------
    pd.DataFrame
        A dataframe containing the input recoltable map positions and quantities per map position 

    """
    x = response['data']
    X, Y, Q, WM = [], [], [], []
    for i in range(len(x)):
        p = x[i]['pos']
        X.append(p['posX'])
        Y.append(p['posY'])
        Q.append(sum([x[i]['quantities'][j]['quantity'] if x[i]['quantities'][j]['item']==RECOLTABLE_IDS[recoltable_name] else 0 for j in range(len(x[i]['quantities']))]))
        WM.append(p['worldMap'])
    df = pd.DataFrame({'x': X, 'y': Y})
    return df

def get_recoltable_map_positions(recoltable_name: str) -> pd.DataFrame:
    """
    Applies 10 requests on dofusdb API and parses the responses to get all the recoltable map positions

    Parameters
    ----------
    recoltable_name: str
        A recoltable name.
        
    Returns
    -------
    pd.DataFrame
        A dataframe containing the recoltable map positions from 10 GET requests (skip+=10 at each iteration)   
    
    """
    df = pd.DataFrame()
    for skip in tqdm(range(0, NMAX_RESPONSES[recoltable_name], 10)):
        res = get_request_map_positions(recoltable_name=recoltable_name, skip=skip)
        dfi = parse_response(res, recoltable_name)
        df = pd.concat([df, dfi], ignore_index=True)
    df = df.drop_duplicates()
    df = discrete_zone(df)
    df[recoltable_name] = 1
    return df

def discrete_zone(df: pd.DataFrame):
    df.loc[(df.x<-20) & (df.y<-30), 'zone'] = 'bonta'
    df.loc[(df.x>=3) & (df.y<=-20), 'zone'] = 'astrub'
    df.loc[(df.x>=4) & (df.y>=4) & (df.y<=9), 'zone'] = 'village'
    df.loc[(df.x>=0) & (df.y>=22) & (df.y<=28), 'zone'] = 'scara'
    df = df.dropna(subset='zone').reset_index(drop=True)
    return df

def merge_to_old(df_old: pd.DataFrame, df:pd.DataFrame):
    df_res = df_old.merge(df, how='outer', on=['x', 'y', 'zone']).fillna(0)
    for col in df_res.columns[3:]:
        df_res[col] = df_res[col].astype(int)
    df_res = df_res.sort_values(['zone', 'x', 'y'])
    return df_res
