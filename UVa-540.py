counter = 0
endflag = False
while 1:
    counter += 1
    line_count = int(input())
    if line_count == 0:
        break
    else:
        print("Scenario #"+str(counter))
    inputs = []
    for i in range(line_count):
        inputs.append([int(q) for q in input().split()])
        inputs[i].pop(0)
    queue = []
    while True:
        flag = 0
        command = [q for q in input().split()]

        if command[0] == 'STOP':
            break
        elif command[0] == 'DEQUEUE':
            print(queue[0])
            queue.pop(0)
        elif command[0] == 'ENQUEUE':
            for k in range(len(queue)):
                if flag == 1:
                    break
                for j in range(len(inputs)):
                    if int(command[1]) in inputs[j] and int(queue[k]) in inputs[j]:
                        if k != len(queue) - 1:
                            if int(queue[k+1]) not in inputs[j]:
                                queue.insert(k + 1, command[1])
                                flag = 1
                                break
                        else:
                            queue.insert(k + 1, command[1])
                            flag = 1
                            break
            if flag == 0:
                queue.append(int(command[1]))