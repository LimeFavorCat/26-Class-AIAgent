# return에 값이 2개 이상이면 자동으로 튜플로 만듦
def tm():
    sum = 5 + 10
    multiple = 5 * 10
    return sum, multiple


result = tm()
print(result, type(result))
a, b = tm()
print(a, b, type(a),type(b))

