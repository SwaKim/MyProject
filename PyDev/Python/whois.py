#!/usr/bin/python
#-*- coding: utf-8 -*-

import os

def get_whois(url):
    command = "whois " + url
    process = os.popen(command) #os.popen은 시스템 명령어를 실행시킨 결과값을 읽기 모드 형태의 파일 객체로 리턴한다.
    results = str(process.read())
    return results

print(get_whois('8.8.8.8'))

"""
## 요구사항 2
질의한 IP에 대해 whois 실행 결과를 반환하는 REST API 서버를 구축하고 싶습니다.
1. 전달받은 IP에 대해 whois 정보를 조회하는 기능을 구현해보세요.
2. 다음과 같은 리퀘스트를 수신할 수 있는 API 서버를 구축해보세요. `GET /api/whois?q=8.8.8.8`. 여기서 8.8.8.8은 조회하고자 하는 IP 주소값이 들어갑니다.
3. `GET /api/whois?q=8.8.8.8`가 q로 전달한 IP의 whois 정보를 반환하도록 구현해주세요.
"""