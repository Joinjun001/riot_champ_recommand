from flask import Flask, request, render_template
import requests
from urllib import parse
import platform 

app = Flask(__name__)

# Riot API Key 24시간마다 갱신 필요, 403에러 발생시 여기부터 보기 
api_key = "RGAPI-39f40a43-b085-4588-b0cb-c7fb1ce6fa57"  


# 운영 체제에 따른 User-Agent 설정
if platform.system() == "Darwin":  # macOS의 경우
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
elif platform.system() == "Windows":  # Windows의 경우
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
else:  # 기타 운영 체제
    user_agent = "Mozilla/5.0"


REQUEST_HEADERS = {
    # Mac OS 환경의 요청 헤더 
    "User-Agent": user_agent,
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-39f40a43-b085-4588-b0cb-c7fb1ce6fa57"
}


# 메인페이지 (사용자가 닉네임을 검색)
@app.route('/')
def home():
    return render_template('index.html')

# 사용자가 닉네임을 검색하면 search한테 post요청을 함, search는 입력받은 닉네임과 태그를 들고 
# riot api한테 찾아가서 소환사 정보를 달라 한다.
@app.route('/search', methods=['POST'])
def search():
    # 사용자 입력 처리
    user_input = request.form['userInput']  # 사용자가 입력한 값 (예: "Faker#KR1")
    nickname, tagline = "", ""

    if "#" in user_input:
        nickname, tagline = user_input.split("#", 1)  # #을 기준으로 분리
    else:
        return "잘못된 입력 형식입니다. 닉네임과 태그라인을 #으로 구분하여 입력하세요."

    # Riot API 호출
    encoded_name = parse.quote(nickname)
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{encoded_name}/{tagline}"
    response = requests.get(url, headers=REQUEST_HEADERS)
    if response.status_code != 200:
        return f"Riot API 요청 실패: {response.status_code}"
    
    player_id = response.json()

    # {'puuid': '37I3NLp4u1JHu6Pivd32cehW2ix6vkDl46-Q-Tr7BkAt3OTszePvGXYlqwrf9iWt_84bh8CwhzKUUw', 
    #  'gameName': '굳세게버텨', 
    #  'tagLine': 'KR1'}

    # PUUID로 Summoner 정보 가져오기
    puuid = player_id.get('puuid', 'PUUID 없음')
    if puuid == 'PUUID 없음':
        return f"사용자를 찾을 수 없습니다: {nickname}#{tagline}"

    summoner_url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    player_response = requests.get(summoner_url, headers=REQUEST_HEADERS)
    if player_response.status_code != 200:
        return f"Summoner 정보 요청 실패: {player_response.status_code}"

    player = player_response.json()

    matches_url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=420&start=0&count=20"
    matches_response = requests.get(matches_url, headers=REQUEST_HEADERS)
    if matches_response.status_code != 200:
        return f"최근 20경기 정보 요청 실패: {matches_response.status_code}"
    
    matches = matches_response.json()

    print(matches)
    # ['KR_7405526313', 'KR_7405438580', 'KR_7405384187', ...]

    match_res = requests.get(f"https://asia.api.riotgames.com/lol/match/v5/matches/{matches[0]}", headers=REQUEST_HEADERS)
    if match_res.status_code != 200:
        return f"최근 20경기 정보 요청 실패: {match_res.status_code}"
    
    match_res = match_res.json()

    print(match_res)


    # 결과를 페이지에 표시
    return render_template('result.html', player=player, puuid=puuid, player_id=player_id,match_res=match_res)


if __name__ == '__main__':
    app.run(debug=True)