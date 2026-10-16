# encoding = [list]를 활용해 맞는 인코딩 탐색 / json.load() 함수로 json 읽어오기 -> 딕셔너리로 반환

import json

# encoding 탐색
def enco(file_path):
    encodings = ['utf-8','EUC-KR','CP949']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding= enc) as f:
                return enc
        except UnicodeDecodeError:
            if enc == 'CP949':
                return None
"""

# 파일 열기
file = '11-file/data/data.json'
with open(file, 'r', encoding=enco(file)) as f:
    data = json.load(f)

print(data)
print(type(data))
print(f'이름 : {data['name']}({data['age']})')
print(f'보유기술 : {data['skills']}')
print(f'최고 숙련도 : {data['skills'][0]}')
print()


# data2.json 여러개의 {}가 있을때
add_string = ''
students = []
file = '11-file/data/data2.json'
with open(file, 'r', encoding=enco(file)) as f:
    
    for line in f:
        line = line.strip()
        add_string += line

        if line == '}':
            student_dict = json.loads(add_string)
            students.append(student_dict)
            
            add_string = ''

print('====== [ 변환된 students 리스트 ] ======')
print(students)

print('\n====== [ 한 명씩 출력 ] ======')
for std in students:
    print(f'이름 : {std['name']} | 나이 : {std['age']} | 보유기술 : {', '.join(std['skills'])}')
    print(f'이름 : {std['name']}({std['age']})')
    print(f'보유기술 : {', '.join(std['skills'])}')
    print()
"""


# data3.json 여러개의 {}가 줄바꿈이 있을 때
add_string = ""
students = []
file = '11-file/data/data3.json'
with open(file, 'r', encoding=enco(file)) as f:
    for line in f:
        if not line:  # 바닥(빈행)을 만났을 경우
            continue
        line = line.strip()
        add_string += line

        if line == '}':
            students.append(json.loads(add_string))
            add_string = ''

print('======= [변환된 학생 리스트] ======')
print(students)


print('\n======= [학생별 정보 출력] ======')
for student in students:
    print(f'{student['name']}({student['age']}) | 보유기술 : {', '.join(student['skills'])}\n')
















add_string = ''
students = []
file = '11-file/data/data3.json'
with open(file, 'r', encoding=enco(file)) as f:
    
    for line in f:
        line = line.strip()
        add_string += line

        if line == '}':
            student_dict = json.loads(add_string)
            students.append(student_dict)
            
            add_string = ''

print('====== [ 변환된 students 리스트 ] ======')
print(students)

print('\n====== [ 한 명씩 출력 ] ======')
for std in students:
    print(f'이름 : {std['name']} | 나이 : {std['age']} | 보유기술 : {', '.join(std['skills'])}')
    print(f'이름 : {std['name']}({std['age']})')
    print(f'보유기술 : {', '.join(std['skills'])}')
    print()