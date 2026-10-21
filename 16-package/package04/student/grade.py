def grade(score):
    if score < 0 or score > 100:
        return'정상적인 범위의 값을 넣어주세요'
    else:
        if score < 60:
            return "F"
        elif score < 65:
            return "D"
        elif score < 70:
            return "D+"
        elif score < 75:
            return "C"
        elif score < 80:
            return "C+"
        elif score < 85:
            return "B"
        elif score < 90:
            return "B+"
        elif score < 95:
            return "A"
        else:
            return "A+"

if __name__ == "__main__":
    print(grade(60))
    print(grade(101))