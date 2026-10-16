prices = [10000 * i for i in range(1,4)]
# 20% 할인된 가격을 리스트로 만들어 출력. lambda 함수 활용

discounted_price = [(lambda price : price * 0.8)(i) for i in prices]
print(discounted_price)
