## RCRS (Riot Champion Recommendation System) 😃

Riot Game API를 활용하여 개발하는 웹 애플리케이션 프로젝트.

op.gg처럼 소환사의 정보를 통해서 소환사에게 필요한 정보를 알려주는 사이트를 만들어보자. 🥵
(개인용 API KEY라 요청할 수 있는 데이터가 한정되어있다.) 😭

개인용 API로는 요청속도와 요청개수에 제한이 있어서 정말 기본적인 구성으로만 만들수 있었다.

## 개발언어

API 요청 : Python
프론트엔드 : JS, HTML, CSS

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
