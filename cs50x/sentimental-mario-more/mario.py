# TODO
height = -1
while not (1 <= height <= 8):
    try:
        height = int(input("Height: "))
    except ValueError:
        height = -1
space = height-1
count = 1
for i in range(height):
    print(" "*space+"#"*count+"  "+"#"*count)
    space -= 1
    count += 1