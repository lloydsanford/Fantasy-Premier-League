import requests
import json
import time

def get_data():
    """ Retrieve the fpl player data from the hard-coded url
    """
    response = requests.get("https://fantasy.premierleague.com/drf/bootstrap-static")
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    responseStr = response.text
    data = json.loads(responseStr)
    return data

def get_individual_player_data(player_id):
    """ Retrieve the player-specific detailed data

    Args:
        player_id (int): ID of the player whose data is to be retrieved
    """
    base_url = "https://fantasy.premierleague.com/drf/element-summary/"
    full_url = base_url + str(player_id)
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data

def get_entry_data(entry_id):
    """ Retrieve the summary data for a specific entry/team

    Args:
        entry_id (int) : ID of the team whose data is to be retrieved
    """
    base_url = "https://fantasy.premierleague.com/drf/entry/"
    full_url = base_url + str(entry_id) + "/history"
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data

def get_entry_gws_data(entry_id):
    """ Retrieve the gw-by-gw data for a specific entry/team

    Args:
        entry_id (int) : ID of the team whose data is to be retrieved
    """
    base_url = "https://fantasy.premierleague.com/drf/entry/"
    gw_data = []
    for i in range(1, 39):
        full_url = base_url + str(entry_id) + "/event/" + str(i)
        response = ''
        while response == '':
            try:
                response = requests.get(full_url)
            except:
                time.sleep(5)
        if response.status_code != 200:
            raise Exception("Response was code " + str(response.status_code))
        data = json.loads(response.text)
        gw_data += [data]
    return data

def get_entry_transfers_data(entry_id):
    """ Retrieve the transfer data for a specific entry/team

    Args:
        entry_id (int) : ID of the team whose data is to be retrieved
    """
    base_url = "https://fantasy.premierleague.com/drf/entry/"
    full_url = base_url + str(entry_id) + "/transfers"
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data
