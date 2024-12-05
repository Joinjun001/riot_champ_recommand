## RCRS (Riot Champion Recommendation System) 😃

Riot Game API를 활용하여 개발하는 웹 애플리케이션 프로젝트.

op.gg처럼 소환사의 정보를 통해서 소환사에게 필요한 정보를 알려주는 사이트를 만들어보자. 🥵
(개인용 API KEY라 요청할 수 있는 데이터가 한정되어있다.) 😭

## 📖 참고 자료

- [Riot Games API 공식 문서](https://developer.riotgames.com/)
- [Flask 공식 문서](https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html)
- 챔피언, 아이콘 데이터가 있는 API 사이트 [communitydragon.org](https://www.communitydragon.org/)
- [README 쓸 줄 몰라서 본 사이트](https://www.easy-me.com/d)

## 🛠 개발일지

### 2024.12.05

- index.html (유저가 닉네임 검색하는 화면) 구현 완료
- result.html (소환사 정보를 보여주는 화면) 구현 완료

## 보완할 점

### result.html

- 현재 다시 검색을 눌러야 다시 index.html로 돌아가는데, result.html에 그냥 input창 만들어서 바로바로 검색 가능하게 만들기
- 최근 소환사의 20전 경기 기록 ID를 가져와서 승패를 집계하고, 승률을 그래프로 시각화해서 보여주기
- 다른 통계로 뭘 보여줘야 할 지 생각하기
