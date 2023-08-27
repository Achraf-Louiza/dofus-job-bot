import requests
import pandas as pd
from tqdm import tqdm
import os, sys; sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from config import *

def get_request_map_positions(recoltable_id: int, skip: int) -> dict:
    """
    Sends an HTTP request to dofus db API that gets a recoltable's map positions
    
    PARAMETERS
    ----------
    recoltable_id: int
        A recoltable id as defined in dofus db APIs. They can be checked in config file.
    skip: int
        Number of requests elements to skip. 
        Since this specific request has a 10 records limit per request, we will skip incremently 10 to get all the data. 
        
    RETURNS
    -------
    dict
        A json object corresponding to the requests response and contains, the recoltable map positions and quantities per map position. 
    """
    url = DOFUSDB_API_URL
    payload = {'resources[$in][]': recoltable_id,
               '$skip': skip,
               'lang': 'fr'}
    response = requests.get(url, params=payload)  
    return response.json()

def parse_response(response: dict, recoltable_id: int) -> pd.DataFrame:
    """
    Parses a GET HTTP request and extracts recoltable map positions and quantities per map position

    Parameters
    ----------
    response : dict
        Response returned by GET HTTP request to dofus db on a recoltable map positions
    recoltable_id: int
        A recoltable id as defined in dofus db APIs. They can be checked in config file.

    Returns
    -------
    pd.DataFrame
        A dataframe containing the input recoltable map positions and quantities per map position 

    """
    x = res['data']
    X, Y, Q, WM = [], [], [], []
    for i in range(len(x)):
        p = x[i]['pos']
        X.append(p['posX'])
        Y.append(p['posY'])
        Q.append(sum([x[i]['quantities'][j]['quantity'] if x[i]['quantities'][j]['item']==recoltable_id else 0 for j in range(len(x[i]['quantities']))]))
        WM.append(p['worldMap'])
    df = pd.DataFrame({'quantity': Q, 'x': X, 'y': Y, 'worldMap': WM})
    return df

def get_recoltable_map_positions(recoltable_id: int) -> pd.DataFrame:
    """
    Applies 10 requests on dofusdb API and parses the responses to get all the recoltable map positions

    Parameters
    ----------
    recoltable_id: int
        A recoltable id as defined in dofus db APIs. They can be checked in config file.
        
    Returns
    -------
    pd.DataFrame
        A dataframe containing the recoltable map positions from 10 GET requests (skip+=10 at each iteration)   
    
    """
    df = pd.DataFrame()
    for skip in tqdm(range(0, NMAX_RESPONSES, 10)):
        res = get_request_wheat_map_pos(recoltable_id=recoltable_id, skip=skip)
        dfi = parse_response(res)
        df = pd.concat([df, dfi], ignore_index=True)
    df.drop_duplicates()
    return df

def save_positions_csv(df_pos: pd.DataFrame, recoltable_name: str) -> None:
    """
    Saves a dataframe of a recoltable map positions into a csv file in the defined path (check config.py)

    Parameters
    ----------
    df_pos : pd.DataFrame
        A dataframe of a recoltable map positions
    recoltable_name: str
        A recoltable name (such as: wheats, oats, etc.)
        
    """
    df_pos.to_csv(RECOLTABLE_MAP_POSITIONS_FILE_PATH(recoltable_name), index=False)



