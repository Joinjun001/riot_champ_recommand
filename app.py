from flask import Flask, request, render_template
from helpers import get_riot_account, get_summoner_by_puuid, get_match_ids_by_puuid, get_match_data

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    # 사용자 입력 처리
    user_input = request.form['userInput']
    if "#" not in user_input:
        return "잘못된 입력 형식입니다. 닉네임과 태그라인을 #으로 구분하여 입력하세요."

    nickname, tagline = user_input.split("#", 1)

    # Riot API로 사용자 정보 가져오기
    player_id = get_riot_account(nickname, tagline)
    if not player_id:
        return f"사용자를 찾을 수 없습니다: {nickname}#{tagline}"

    puuid = player_id.get("puuid")
    if not puuid:
        return "PUUID 정보를 가져올 수 없습니다."

    # 소환사 정보 가져오기
    player = get_summoner_by_puuid(puuid)
    if not player:
        return "소환사 정보를 가져올 수 없습니다."

    # 최근 경기 ID 가져오기
    matches = get_match_ids_by_puuid(puuid,20)
    if not matches:
        return "최근 경기 정보를 가져올 수 없습니다."

    # 특정 경기 데이터 가져오기 (예: 첫 번째 경기)
    match_data = get_match_data(matches[0])
    if not match_data:
        return "경기 데이터를 가져올 수 없습니다."

    # 경기 데이터에서 승패 정보 확인
    participants = match_data["metadata"]["participants"]
    if puuid in participants:
        player_index = participants.index(puuid)
        player_win = match_data["info"]["participants"][player_index]["win"]
    else:
        return "경기 데이터에서 사용자를 찾을 수 없습니다."

    # 결과를 페이지에 표시
    return render_template(
        'result.html',
        player=player,
        puuid=puuid,
        player_id=player_id,
        match_data=match_data,
        matches=matches,
        player_win=player_win,
    )

if __name__ == '__main__':
    app.run(debug=True)