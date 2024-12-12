## RCRS (Riot Champion Recommendation System) 😃

Riot Game API를 활용하여 개발하는 웹 애플리케이션 프로젝트.

op.gg처럼 소환사의 정보를 통해서 소환사에게 필요한 정보를 알려주는 사이트를 만들어보자. 🥵
(개인용 API KEY라 요청할 수 있는 데이터가 한정되어있다.) 😭

## 설치 및 실행 방법 (개발하면서 맥북이랑 윈도우 왔다갔다 할 때 사용)

1. 프로젝트 클론

```bash
git clone https://github.com/Joinjun001/riot_champ_recommand.git
cd riot_champ_recommand
```

2. Python 환경 설정

```bash
python -m venv venv
source venv/bin/activate  # Windows는 venv\Scripts\activate
pip3 install -r requirements.txt
```

3. API 키 설정
   Riot Developer Portal에서 API 키를 발급받아야 합니다.
   app.py 파일의 api_key 변수에 발급받은 키를 추가합니다:

```python
api_key = "YOUR_RIOT_API_KEY"
```

4. 애플리케이션 실행

```python

   python3 app.py # 실행안되면 python app.py이나 flask run (flask run은 debug mode가 off가 될수 있으므로 비추천)
```

## 📖 참고 자료

- [Riot Games API 공식 문서](https://developer.riotgames.com/)
- [Flask 공식 문서](https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html)
- 챔피언, 아이콘 데이터가 있는 API 사이트 [communitydragon.org](https://www.communitydragon.org/)
- [README 쓸 줄 몰라서 본 사이트](https://www.easy-me.com/d)

## 🛠 개발일지

### 2024.12.05

- index.html (유저가 닉네임 검색하는 화면) 구현 완료
- result.html (소환사 정보를 보여주는 화면) 구현 완료

### 2024.12.10

- 개발환경에 따라서 요청헤더 부분 에러 해결 (User-Agent 부분 수정)

### 2024.12.11

- API_KEYS 같은 기본 정보를 담는 settings.py
- app.py에 다 때려박았었는데 함수들을 정리해서 helpers.py 추가

### 2024.12.12

- 20경기의 승패 데이터를 가져와서 승률을 보여주는 기능 구현완료

## 보완할 점

### result.html

- 현재 다시 검색을 눌러야 다시 index.html로 돌아가는데, result.html에 그냥 input창 만들어서 바로바로 검색 가능하게 만들기
- 다른 통계로 뭘 보여줘야 할 지 생각하기
- 20전 승률을 api에서 가져올 때 속도가 너무 느린거 개선하기.
