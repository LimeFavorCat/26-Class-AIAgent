'''
문1 : 2개의 수를 넣으면 그 사이의 숫자들의 합계 구하기
'''

"""
def sumbtw(start:int, end:int)-> int:
    return sum(range(start,end+1))

def draw_triangle(height:int):
    for i in range(1,height+1): print('*'*i)

def draw_triangle2(height:int):
    for i in range(height):
        star = '*'*(1 + 2 * i)
        print(star.center(1+height*2))

def draw_triangle3(height:int):
    for i in range(height):
        star = ' '*(1 + 2 * i)
        print(star.center(1+height*2,'*'))


def draw_triangle4(size:int, dot = ' ', fill='*'):
    weight = 7 + size * 6
    height = 1 + size * 6

    # 맨위 한줄
    print(dot * weight)

    # part 1
    for i in range(size):
        star = fill*(1 + 2 * i)
        print(star.center(weight,dot))

    # part 2
    for i in range(size - size//4):
        star = fill*(weight - 4 - i*size*2)
        print(star.center(weight,dot))

    # part 3
    for i in range(size + size//4):
        star = fill*(size*2 - i*(1+size//4)) + dot *(1 + i*size) + fill*(size*2 - i*(1+size//4))
        print(star.center(weight,dot))

    # 맨아래 한줄
    print(dot * weight)


def draw_triangle5(size:int, dot = ' ', fill='*'):
    weight = 7 + size * 6
    height = 1 + size * 6

    # 맨위 한줄
    print(dot * weight)

    # part 1
    for i in range(size):
        star = fill*(1 + 2 * i)
        print(star.center(weight,dot))

    # part 2
    for i in range(size - size//4):
        star = fill*(weight - 4 - i*(size//3))
        print(star.center(weight,dot))

    # part 3
    for i in range(size + size//2):
        star = fill*(size*2 - i*(1+size//4)) + dot *(1 + i*(size//2)) + fill*(size*2 - i*(1+size//4))
        print(star.center(weight,dot))

    # 맨아래 한줄
    print(dot * weight)



print(sumbtw(1,5))

draw_triangle(5)
draw_triangle2(5)
draw_triangle3(8)
draw_triangle4(4)
draw_triangle4(5,' ','@')
draw_triangle4(8)
draw_triangle4(10)
draw_triangle5(10)
"""

"""도전!! 예쁜 별 그리기"""
import copy
lines=[1,2,3,4,5]

# 순서 -> 기울기 구하기. 각 높이별 진행도 기록 (두 직선의 진행도 확인하여 비활성화)

# 5개의 꼭지점 구하기 -> size 받음 -> (size+1) *2 크기의 박스 생성

BOUNDARY = 2

class Side:
    def __init__(self,line,center):
        if line[center[0]][center[1]] == BOUNDARY:
            raise ValueError("중심점은 경계 위에 놓을 수 없습니다.")
        self.line = line
        self.mask = self.build_side_mask(line,center)
        self.center = center

    def build_side_mask(self,line,center):
        mask = []
        seen_boundary = False
        for row in line:
            mask_row = []
            hit_in_row = False
            for pixel in row:
                if pixel == BOUNDARY:
                    seen_boundary = hit_in_row = True
                    mask_row.append(0)
                else:
                    mask_row.append(1 if hit_in_row else -1)
            if hit_in_row and not seen_boundary:
                mask_row = [1] * len(row)
            mask.append(mask_row)
        center_row, center_col = center
        center_side = mask[center_row][center_col]
            
        return [
            [
                1 if value == 0 else value * center_side
                for value in row
            ] 
            for row in mask
        ]




        result = copy.deepcopy(l)
        vhit = -1
        for i,y in enumerate(result):
            hhit = -1
            for j,point in enumerate(y):
                if point == 2: vhit, hhit = 1, 1
                result[i][j] = hhit
            if vhit == 1 and hhit == -1 : result[i] = [1 for t in range(len(y))]
            print(result)
        if result[c[0]][c[1]] == - 1: 
            result = [[-element for element in row] for row in result]
        print(result)
        return result

sample_line = [[0,0,0,0,2],[0,0,0,2,0],[0,0,2,0,0],[0,2,0,0,0],[2,0,0,0,0],[0,0,0,0,0]]
sample_centor = (2,1)

sample = Side(sample_line,sample_centor)


import math

def get_pentagon_coordinates(r=1.0, cx=0.0, cy=0.0, start_angle=0.0):
    """
    정오각형의 5개 꼭짓점 좌표를 반환하는 함수
    :param r: 외접원의 반지름
    :param cx: 중심점의 x좌표
    :param cy: 중심점의 y좌표
    :param start_angle: 첫 번째 점의 시작 각도 (도, degree 단위)
    :return: (x, y) 좌표 튜플들의 리스트
    """
    coordinates = []
    
    for k in range(5):
        # 72도씩 회전하며 각 꼭짓점의 각도를 라디안으로 변환
        angle_rad = math.radians(start_angle + 72 * k)
        
        # 삼각함수를 이용한 좌표 계산
        x = cx + r * math.cos(angle_rad)
        y = cy + r * math.sin(angle_rad)
        
        # 소수점 4자리까지 반올림하여 저장
        coordinates.append((round(x, 4), round(y, 4)))
        
    return coordinates

# 반지름이 1이고 중심이 (0, 0)인 정오각형 좌표 출력
pentagon = get_pentagon_coordinates(r=1, cx=0, cy=0, start_angle=0)

print("정오각형의 각 꼭짓점 좌표:")
for i, coord in enumerate(pentagon, 1):
    print(f"점 {i}: {coord}")


