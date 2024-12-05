from flask import Flask, request, render_template
import requests
from urllib import parse

app = Flask(__name__)

# Riot API Key 24시간마다 갱신 필요, 401에러 일시 여기부터 보기 
api_key = "RGAPI-0215398d-8e78-4508-b076-fd1204e854e9"  
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
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
    user_nickname = request.form['nickname']
    tag_line = request.form['tagline']
    
    # Riot API 호출
    encoded_name = parse.quote(user_nickname)
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{encoded_name}/{tag_line}"
    player_id = requests.get(url, headers=REQUEST_HEADERS).json()

    print(f"player id : {player_id}")
    
    # PUUID로 Summoner 정보 가져오기
    puuid = player_id.get('puuid', 'PUUID 없음')
    if puuid == 'PUUID 없음':
        # 오류 결과를 페이지에 표시 
        return f"사용자를 찾을 수 없습니다: {user_nickname}#{tag_line}"

    summoner_url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    player = requests.get(summoner_url, headers=REQUEST_HEADERS).json()

    print(f"player : {player}")
    # 결과를 페이지에 표시
    return render_template('result.html', player=player, puuid=puuid, player_id=player_id)

if __name__ == '__main__':
    app.run(debug=True)