# TODO
num = input("Number: ")
sum1 = 0
if len(num) not in [13, 15, 16]:
    print("INVALID")
    exit()
if (int(num[0:2]) not in [34, 37, 51, 52, 53, 54, 55] and int(num[0]) != 4):
    print("INVALID")
    exit()
temp = num[-2::-2]
for i in temp:
    sum1 += int(i)*2 if int(i)*2 < 10 else sum(int(x) for x in str(int(i)*2))
temp = num[-1::-2]
for i in temp:
    sum1 += int(i)
if str(sum1)[-1] != "0":
    print(str(sum1)[-1])
    print("INVALID")
    exit()
array = [3, 4, 5]
type = array.index(int(num[0]))
if type == 0:
    print("AMEX")
elif type == 1:
    print("VISA")
elif type == 2:
    print("MASTERCARD")