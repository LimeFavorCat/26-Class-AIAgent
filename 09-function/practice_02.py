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
import math

BOUNDARY = 2

def calculate_mask_size(radius,center):
    height = math.ceil(1 + radius + abs(center[0]))
    weight = math.ceil(1 + radius + abs(center[1]))
    return 1 + height * 2 if height > weight else 1 + weight * 2 , (height, weight)

def calculate_coordinates(r=1.0, center=(0,0), points = 5, start_angle=0.0):
    """
    정오각형의 5개 꼭짓점 좌표를 반환하는 함수
    :param r: 외접원의 반지름
    :param cx: 중심점의 x좌표
    :param cy: 중심점의 y좌표
    :param start_angle: 첫 번째 점의 시작 각도 (도, degree 단위)
    :return: (x, y) 좌표 튜플들의 리스트
    """
    coordinates = []
    cy, cx = center
    for k in range(5):
        # 360/n 도씩 회전하며 각 꼭짓점의 각도를 라디안으로 변환
        angle_rad = math.radians(start_angle + 360/points * k)
        
        # 삼각함수를 이용한 좌표 계산
        x = cx + r * math.cos(angle_rad)
        y = cy + r * math.sin(angle_rad)
        
        # 소수점 4자리까지 반올림하여 저장
        coordinates.append((round(x, 4), round(y, 4)))
        
    return coordinates


def build_line(point1, point2, image_size:int):
    # 좌표계와 배열 인덱스 맞추기
    line = [[0 for i in range(image_size)] for j in range(image_size)]
    y1, x1 = point1
    y2, x2 = point2
    m = (y2 - y1) / (x2 - x1) 
    y_max = int((image_size-1)/2)

    # 기울기 0인 경우
    if m == 0 :
        result = []
        for j in range(image_size): 
            result.append([BOUNDARY if y_max - j == round(y1) else 0 for i in range(image_size)])
            print(result[-1])
        return result

    # 그 외 선 그리기
    for i in range(image_size):
        y_pos = y_max - i
        x_pos = round((y_pos - y1)/m + x1) + y_max
        if x_pos > 0 and x_pos < image_size:
            line[i][x_pos] = BOUNDARY
        print(line[i])
    print()
    return line

class Side:
    @staticmethod
    def merge_mask(mask1, rule, mask2):
        mask_size = len(mask1) if len(mask1) > len(mask2) else len(mask2)
        mask= []
        for y in range(mask_size):
            match rule:
                case 'and':
                    mask.append([int(mask1[y][x] * mask2[y][x]) for x in range(mask_size)])
                    print(mask[-1])
                case 'or':
                    mask.append([int(mask1[y][x] + mask2[y][x]) for x in range(mask_size)])
                    print(mask[-1])
        print()
        return mask

    def __init__(self, line, center = (0,0)):
        self.line = line
        self.mask = self.build_side_mask(line, center)
        self.center = center

    def build_side_mask(self,line,center):
        center_row, center_col = center
        mask_size = len(line)
        if BOUNDARY in line[center_row]: # 가로선 아님
            if center_col < line[center_row].index(BOUNDARY) : # 선이 중앙에서 오른쪽에 있음
                left = 0 # 왼쪽에 1 채워라
                right = 1 # 왼쪽에 1 채워라
            else:
                left = 1
                right = 0
            mask = []
            for row in line:
                if BOUNDARY in row:
                    line_pos = row.index(BOUNDARY)
                    mask.append([left for i in range(line_pos)] + [0] + [right for i in range(mask_size -1 -line_pos)])
                else:
                    mask.append([0 for index in range(mask_size)])
                print(mask[-1])
            print()
            return mask
        else: # 가로선 예외처리
            for i, row in enumerate(line):
                if row[0] == 2:
                    return [[1 for k in range(mask_size)] for v in range(i)] + [[0 for k in range(mask_size)] for v in range(mask_size - i)] 
            pass

    def build_side_mask_old(self,line,center):
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


# user input
star_radius = float(input("별의 반지름을 입력해 주세요 : "))
star_point = 5 # int(input("꼭지점 갯수를 입력해 주세요 : "))
star_center = (0,0) # int(input("Y 좌표 : ")), int(input("X 좌표 : ")) # x,y 좌표계로 받음

# calculate point
image_size, image_center = calculate_mask_size(star_radius, star_center)

print(f'{image_size} x {image_size} 픽셀 맵 - 중앙 인덱스 : {image_center}')
cordinates = calculate_coordinates(star_radius, star_center, star_point)
print(cordinates)

# calculate line
lines = []
for index, point in enumerate(cordinates):
    point2 = cordinates[(index+2) % len(cordinates)]
    line = build_line(point, point2, image_size)
    lines.append(line)

# build bit mask
sides = [Side(line, image_center) for line in lines]

backgrounds = [Side.merge_mask(sides[x].mask, 'and', sides[(x+1) % star_point].mask) for x in range(star_point)]

star_mask = Side.merge_mask(Side.merge_mask(Side.merge_mask(Side.merge_mask(backgrounds[0], 'or', backgrounds[1]), 'or', backgrounds[2]), 'or', backgrounds[3]), 'or', backgrounds[4])

# print
for i in star_mask:
    for j in i:
        print('  'if j == 1 else "**", end='')
    print()

