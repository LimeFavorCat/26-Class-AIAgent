num1 = 100
num2 = 200

x = 7
y = 3
f_result = num1 >= num2
t_result = x >= y

print('f_result =', f_result,', t_result =', t_result)

and_result = f_result and t_result
or_result = f_result or t_result
print(f'{f_result} and {t_result} = {and_result}')
print(f'{f_result} or {t_result} = {or_result}')
print(f'f_result not = {not f_result}')
print(f'f_result xor t_result = {f_result ^ t_result}')
print(f'f_result xor f_result = {f_result ^ f_result}')