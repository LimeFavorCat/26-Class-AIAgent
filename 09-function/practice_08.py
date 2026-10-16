# 문제 1 - 카페주문 - 메뉴와 사이즈 2개를 입력받으며 사이즈 기본값 small
def order(menu, size='small'):
    print(f'주문 완료 : {menu}, {size} 사이즈로 주문 받았습니다.')

order('아이스 아메리카노')
order('아샷추','medium')
print()

# 문제 2 - 택배 배송정보 - 받는사람, 주소, 전화번호를 입력받음. 순서와 상관없이 입력받기
def cupang(user, address, tel):
    print(f'받는 사람 : {user} / 주소 : {address} / 전화번호 : {tel}\n')

cupang(address='강남',tel='010-1234-1234', user='홍길동')

# 문제 3 - 결제한 금액 합계 - 매번 길이가 달라져야 함 (tuple)
def diplay_sum(*args):
    result = 0
    for i in args:
        result += i
        print(f'+ {i:3,d}')
    print(f'총액 : {result:3,d}\n')

diplay_sum(12000,8000,9000,23000)

# 문제 4 - 회원가입 - 사람마다 입력하는 정보의 개수가 다를 수 있음 (dict)
def get_user_info(**kwargs):
    print('회원가입 정보 ---')
    for key, value in kwargs.items():
        print(f'{key} : {value}')
    print()

get_user_info(user='홍길동',id='hong1234',password='12341234',email='hong1234@gmail.com')