# **kwargs : dictionary가 전잘됨
# kwargs는 변수명으로 관습적으로 kwargs로 쓴다.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name = '홍길동')
print_info(name = '김미영', age=23, city='Seoul')

info = {'name':'김미영', 'age':23, 'city':'Seoul'}
# print_info(info) # error -> info라는 딕셔너리 객체 단 1개를 전달하여
print_info(**info) # **로 언패킹을 해서 전달함