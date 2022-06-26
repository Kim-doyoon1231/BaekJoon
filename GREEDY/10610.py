num = input()
num_list=[]
zero = False
digit_sum = 0
for i in num:
    num_list.append(int(i))
    digit_sum += int(i)
    if int(i) == 0:
        zero = True
if not zero or digit_sum % 3 != 0:
    print(-1)
else:
    num_list.sort(reverse = True)
    for i in num_list:
        print(i, end = '')


# 30의 배수의 조건 - 3의 배수여야 한다. 0이 포함되어 있어야 한다.