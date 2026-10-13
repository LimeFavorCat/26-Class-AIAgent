s= {1,2,3,1,2,3,4,5,3,5}

print(2 in s)
print(6 in s)

s.add(10)
print(s)

# update
s.update({1,2,3,4,5,6,7})
print(s)

# 개별 삭제 가능
s.remove(2)
print(s)

# 전체 삭제 : clear
s.clear()
print(s)