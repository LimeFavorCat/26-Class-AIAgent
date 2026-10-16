# 키워드 인자 (매개변수를 전달할때 변수명을 같이 전달하면 순서를 바꿔도 작동함)
def display_info(academy, name, classroom):
    print(f'Academy : {academy}, Name : {name}, ClassRoom : {classroom}')

display_info('더조은', '홍길동', '704호')


# 기본 값 넣기
def display_info2(name, classroom, academy = '더조은'):
    print(f'Academy : {academy}, Name : {name}, ClassRoom : {classroom}')

# 순서대로 넣기, 기본값이 있는 매개변수 생략가능
display_info2('홍길동', '704호')
display_info2('홍길동', '704호', '더조은')

# 매개변수를 명시적으로 기입 가능
display_info2(classroom='704호', name='홍길동')
