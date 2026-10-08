'''
문제

사용자로부터 입력받기
경기장은 어디입니까?
이긴팀은 어디입니까?
진 팀은 어디입니까?
스코어는 몇대 몇 입니까?

오늘 문학경기장에서 야구경기가 열렸습니다
라이언과 한화의 치열한 공방전이 펼쳐졌습니다
결국 라이언은 한화를 1:3으로 이겼습니다
'''
"""
class Anaounce:
    def __init__(self,stadium,winner,loser,score):
        self.stadium = stadium
        self.winner = winner
        self.loser = loser
        self.score = score

    def result(self):
        txt = f'''\
==============================
오늘 {self.stadium}에서 야구경기가 열렸습니다
{self.winner}과 {self.loser}의 치열한 공방전이 펼쳐졌습니다
결국 {self.winner}은 {self.loser}를 {self.score}으로 이겼습니다
==============================
        '''
        print(txt)

ana = Anaounce(input("경기장은 어디입니까?"), input("이긴팀은 어디입니까?"), input("진 팀은 어디입니까?"), input("스코어는 몇대 몇 입니까?"))
ana.result()
"""

print('==============================\n오늘 {0}에서 야구경기가 열렸습니다\n{1}과 {2}의 치열한 공방전이 펼쳐졌습니다\n결국 {1}은 {2}를 {3}으로 이겼습니다\n=============================='.format(input("경기장은 어디입니까?"), input("이긴팀은 어디입니까?"), input("진 팀은 어디입니까?"), input("스코어는 몇대 몇 입니까?")))