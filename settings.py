# 전역 변수, API_KEY 등등.. 
import platform

# Riot API Key (필요 시 업데이트)
API_KEY = "RGAPI-4a1710d3-a808-4aca-b2c0-a96fd51e0102"

# 운영 체제에 따른 User-Agent 설정
if platform.system() == "Darwin":  # macOS
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
elif platform.system() == "Windows":  # Windows
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
else:  # 기타 운영 체제
    USER_AGENT = "Mozilla/5.0"

# 공통 요청 헤더
REQUEST_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": API_KEY,
}

