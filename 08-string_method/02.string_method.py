st1 = 'He likes apples, and she does, like too'

# 문자열에서 특정 문자열의 갯수 구하기
print(st1.count('like'))

# find() -> 왼쪽에서 오른쪽으로 문자열 검색
p = st1.find('like')
print(p)
print(st1.find('like',p+1)) # start 옵션을 줘서 첫번째 like 무시
print(st1.find('love')) # 없을 경우 -1 반환

# rfind() -> 오른쪽에서부터 문자열 검색
print(st1.rfind('like')) 
print(st1.rfind('like',0,3)) 
print(st1.rfind('like',0,15)) 

# index() : find()와 기능은 같지만 없으면 예외 발생
# print(st1.index('love')) # ValueError: substring not found

# startswith() -> 시작하는 단어인지 검사
print(st1.startswith('He'))
print(st1.startswith('likes'))
print(st1.startswith('likes', 3))

# endswith() -> 끝나는 단어인지 검사
print(st1.endswith('like'))
print(st1.endswith('like',0,7))
print(st1.endswith('too'))