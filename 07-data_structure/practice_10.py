"""
편의점에서 주말 알바의 근무시간을 저장한 튜플

문1. 주말 동한 일한 총 근무 시간의 합 구하기
문2. 일요일 근무 시간만 따로 떼어내어 sun_hours라는 새로운 튜플을 만들어 출력
문3. 토요일 오전 근무시간이 4시간에서 5시간으로 변경

"""
# 조건
work_hours = (4,5,3,4)


# 일반적 풀이
total_hour = sum(work_hours)
print(f'문1. 총 근무시간 : {total_hour}')

sun_hours = work_hours[2:]
print(f'문2. 일요일 근무시간 {sun_hours}')

work_hours = 5, *work_hours[1:]
print(f'문3. 변경된 근무시간 {work_hours}')


# 자습
def change(tup, index, value):
    return *tup[:index],value,*tup[index+1:]
print(change(work_hours,0,1))
print(change(work_hours,1,1))
print(change(work_hours,2,1))
print(change(work_hours,3,1))

print(sum(work_hours))

print(work_hours[2:])