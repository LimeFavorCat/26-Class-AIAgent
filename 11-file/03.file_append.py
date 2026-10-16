# 추가모드로 열기
with open('11-file/data/test.txt','a',encoding = 'utf-8') as f:
    f.write('이어쓰기\n')

    for i in range(11,21):
        f.write(str(i)+'번째 이어쓰기\n')
print('쓰기 완료')

# 덮어쓰기 막기
with open('11-file/data/test.txt','x') as f:
    f.write('즐거운 하루')

print('쓰기 완료')