'''
pandas API : 데이터 분석 밎 조작을 위한 라이브러리
    > CSV, Excel, Json, SQL등 다양한 형식의 데이터를 쉽게 읽어올 수 있음
    > 결측치(빈 데이터) 채우기/삭제, 중복 데이터 제거, 데이터 타입 변환 등의 전처리가 용이
    > 대용량 데이터도 빠르게 처리

설치 필요 : pip install pandas openpyxl
'''
import pandas as pd

PATH = '11-file/data/'
# 엑셀 파일 읽어오기
df = pd.read_excel('11-file/data/students.xlsx')
# df = pd.read_excel('11-file/data/students.xlsx',sheet_name='Sheet1')
print(df,'\n')
print(df.head(),'\n')

# json 파일 읽어오기
file = PATH + 'data_list.json'
df = pd.read_json(file)
print(df,'\n')

file = PATH + 'data_list2.json'
df = pd.read_json(file)
print(df,'\n')

file = PATH + 'data.json'
df = pd.read_json(file)
print(df,'\n')


# 일반 json 모듈로 파일을 읽어서 딕셔너리로 가져오기
file = PATH + 'data.json'
import json
with open(file,'r',encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame([data])
print(df)