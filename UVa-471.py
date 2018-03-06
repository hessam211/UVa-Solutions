def is_unique(num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] == num[j]:
                return False
    return True

cout = int(input())

for i in range(cout):
    trash = input()
    i = 1
    num = int(input())
    while i * num < 10000000000:
        if is_unique(str(i)) == True and is_unique(str(i*num)) == True:
            print(i*num,"/" ,i, "=",num)
        i += 1
    print("\n")