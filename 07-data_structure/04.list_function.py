str_list = ['국어', '영어', '수학', '국사', '컴퓨터']
print(str_list.index('영어'))
# print(str_list.index('파이썬')) # Value error : x is not in list

target = '파이썬'
if target in str_list:
    print(str_list.index(target))
else:
    print('데이터 없음')

target = '수학'
if target in str_list:
    print(str_list.index(target))
else:
    print('데이터 없음')
print('-' * 50)

# 항목추가 : 제일 뒤에 데이터 추가
str_list.append('파이썬')
print(str_list)

str_list.insert(2, '인공지능')
print(str_list)

# 데이터 정렬
# sorted : 데이터 원본은 안바뀜 (기본값 : 오름차순) 
print(sorted(str_list))
print(sorted(str_list, reverse= True))
print(str_list)
print('-' * 50)

# sort : 데이터 원본이 바뀜
str_list.sort()
print(str_list)

str_list.sort(reverse=True)
print(str_list)

# 데이터 삭제
target = '국어'
if target in str_list:
    str_list.remove(target)
print(str_list)

target = '세계사'
if target in str_list: # if문으로 예외처리 해야 오류를 막을 수 있다.
    str_list.remove(target)
print(str_list)

# 모든 데이터 삭제
str_list.clear()
print(str_list)  