def average(*score):
    sum = 0
    for i in score:
        sum += i
    return sum / len(score)

if __name__ == "__main__":
    print(average(100,100,50,50,50,0))