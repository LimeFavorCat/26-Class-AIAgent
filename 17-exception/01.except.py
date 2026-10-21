# 예외처리 : try - except(else) - finally
'''
try:
    result = 10 / 0
    print(result)
    print('try에서 실행됨')
except:
    print('오휴발생 0으로 나눌 수 없음')
finally:
    print('실행 끝')


try:
    num = int(input('숫자 입력 : '))
    result = 10 / num
except ValueError:
    print('숫자만 입력해야 합니다')
except ZeroDivisionError as e:
    print(f'0으로 나눌 수 없습니다. (에러 메세지 : {e})')
else:
    print('정상적으로 수행 완료')
finally:
    print('프로그램 종료')'''

try:
    f = open('17-exception/data.txt','r')
except FileNotFoundError:
    print('파일이 존재하지 않습니다')
else:
    print('파일을 성공적으로 읽었습니다.')
finally: # 오류가 나도 finally 안에 있으면 무조건 실행됨
    print('작업을 끝냈습니다')
