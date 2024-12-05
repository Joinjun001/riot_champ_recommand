## RCRS (Riot Champion Recommendation System)
Riot Game API를 활용하여 챔피언 추천 시스템을 개발하는 웹 애플리케이션 프로젝트.

## 설치 및 실행 방법 

1. 프로젝트 클론
```bash
git clone https://github.com/Joinjun001/riot_champ_recommand.git
cd riot_champ_recommand
```

2. Python 환경 설정 
```bash
python -m venv venv
source venv/bin/activate  # Windows는 venv\Scripts\activate
pip install -r requirements.txt
```

3. API 키 설정 
Riot Developer Portal에서 API 키를 발급받아야 합니다.
app.py 파일의 api_key 변수에 발급받은 키를 추가합니다:
```python
api_key = "YOUR_RIOT_API_KEY"
```

4. 애플리케이션 실행 
`flask run`

참고 자료
[Riot Games API 공식 문서](https://developer.riotgames.com/)
[Flask 공식 문서](https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html)

