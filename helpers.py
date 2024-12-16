import requests
from urllib import parse
from settings import REQUEST_HEADERS
import sys

print(sys.path)

def get_riot_account(nickname, tagline):
    """Riot ID로 사용자 계정을 리턴합니다.
    {'puuid': '37I3...', 
    'gameName': '굳세게버텨', 
    'tagLine': 'KR1'}"""
    encoded_name = parse.quote(nickname)
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{encoded_name}/{tagline}"
    response = requests.get(url, headers=REQUEST_HEADERS)
    try:
        response = requests.get(url, headers=REQUEST_HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Riot ID로 사용자 계정을 가져오는 중 에러가 발생했습니다. {e}")
        return None

def get_summoner_by_puuid(puuid):
    """PUUID로 소환사 정보를 리턴합니다.
    {'id': 'nVki...', < 소환사의 랭크 정보를 불러올때 필요함.
    'accountId': 'cJ1CEy...', 
    'puuid': '37I3...', 
    'profileIconId': 1, 
    'revisionDate': 1733927988463, 
    'summonerLevel': 490}"""
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    response = requests.get(url, headers=REQUEST_HEADERS)
    try:
        response = requests.get(url, headers=REQUEST_HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"PUUID를 통해 소환사 정보를 얻는 중 에러가 발생했습니다. {e}")
        return None

def get_match_ids_by_puuid(puuid,count):
    """PUUID로 count 만큼 최근 경기ID를 리턴합니다.
    ['KR_7371672373', 'KR_7369291677', ...]"""
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=420&start=0&count={count}"
    response = requests.get(url, headers=REQUEST_HEADERS)
    try:
        response = requests.get(url, headers=REQUEST_HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"PUUID를 통해 {count}만큼의 경기ID를 얻는 중 에러가 발생했습니다. {e}")
        return None

def get_match_data(match_id):
    """경기 ID로 경기 데이터를 리턴합니다.
    경기에 있는 소환사의 승리유무는 여기서 가져옵니다."""
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = requests.get(url, headers=REQUEST_HEADERS)
    try:
        response = requests.get(url, headers=REQUEST_HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"경기 ID를 통해 경기 데이터를 얻는 중 에러가 발생했습니다. {e}")
        return None
    
def did_player_win_match(puuid, match_id):
    """puuid와 경기 ID로 플레이어의 승리 유무를 리턴합니다"""

    # 경기 ID로 해당 경기의 데이터를 얻는 API 
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    try:
        response = requests.get(url, headers=REQUEST_HEADERS)
        response.raise_for_status()
        match_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"match ID를 통해 match 데이터를 가져오는중 에러가 발생했습니다. {e}")
        return None
    
    # puuid를 통해 플레이어를 찾고, 플레이어가 있으면 승리유무를 불리언값으로 리턴한다.
    if puuid in match_data['metadata']['participants']:
        player_index = match_data['metadata']['participants'].index(puuid)
    else:
        return None
    player_info = match_data['info']['participants'][player_index]
    return player_info['win']

def win_percent_of_last_20_games(puuid):
    """puuid를 통해 소환사의 최근 20경기 승률을 가져옵니다.(로딩 김)"""
    summoner = get_summoner_by_puuid(puuid)
    matches = get_match_ids_by_puuid(summoner['puuid'], 20)

    wins = 0
    for match in matches:
        if did_player_win_match(summoner['puuid'], match):
            wins += 1
    return int((wins/len(matches)) * 100)

def get_ranked_stats(encrytped_summoner_id):
    """암호화된 summoner_id를 통해 소환사의 랭크 정보를 리턴합니다."""
    url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{encrytped_summoner_id}"

    try:    
        response = requests.get(url, headers=REQUEST_HEADERS)
        response.raise_for_status()
        ranked_stats = response.json()
        return ranked_stats
    except requests.exceptions.RequestException as e:
        print(f"encrytped_summoner_id로 소환사의 랭크 정보를 가져오는 중 에러가 발생했습니다. {e}")
        return None
    
