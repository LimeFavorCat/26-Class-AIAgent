# 일반적인 풀이
class Square:
    def __init__(self,height,width):
        self.widht = width
        self.height = height

    def calc_extent(self):
        return self.widht * self.height / 2

class Student:
    def set(self, name, score):
        self.name = name
        self.score = score

    def display_score(self):
        print(self.name)
        sum = 0
        count = 0
        for key, value in self.score.items():
            sum += value
            count += 1
            print(f'{key} : {value}')
        print(f'합계 : {sum}\n평균 : {sum/count}\n')

if __name__ == '__main__':
    sq = Square(10,10)
    print(sq.calc_extent())

    st = Student()
    st.set('이름',{'과목1' : 100, '과목2' : 50 })
    st.display_score()