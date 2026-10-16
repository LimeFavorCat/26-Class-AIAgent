# 파일 열기

# read() -> 전체 문자열을 str으로 저장
with open('11-file/data/with_test.txt','r',encoding='utf-8') as f:
    text = f.read()
    print(text)

    t1 = text.split('\n')
    print(t1)

# readline() -> 한 행을 읽어서 저장
with open('11-file/data/test.txt', 'r',encoding='utf-8') as f:
    text = f.readline()
    print(text)

# readlines() -> 모든 내용을 한 행씩 읽어와서 리스트로 저장
with open('11-file/data/test.txt', 'r',encoding='utf-8') as f:
    text_lines = f.readlines() 
    print(text_lines)

# 줄바꿈 문자 지우기
with open('11-file/data/test.txt', 'r',encoding='utf-8') as f:
    text_lines = [line.strip() for line in f.readlines()]
    print(text_lines)

    text_lines = f.read().splitlines()