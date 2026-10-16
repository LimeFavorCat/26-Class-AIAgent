'''
* 기본환경 : 모든 개발환경에 공통적으로 설치됨
* 가상환경 : 해당 프로젝트에서만 사용하는 패키지 설치

* 가상환경 만들기
    터미널이서(cmd) python -m venv [가상환경이름]

* 가상환경 활성화
    가상환경이 있는 폴더에서 [가상환경이름]\Scripts\activate
'''

import requests

def get_ex():
    response = requests.get('https://google.com')
    print(f'Status Code : {response.status_code}')
    print(response.text)

if __name__ == '__main__':
    get_ex()
    
r = requests.get('https://www.naver.com/')
print(r)
print(r.headers['content-type'])
print(r.text)
print(r.json)