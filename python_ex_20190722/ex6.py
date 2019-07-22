def solution(mylist):
    answer = [[1,2,3],[4,5,6],[7,8,9]]
    print(answer)
    for i in range(len(mylist)):
        num = 0
        for j in range(len(mylist[i])):
            answer[i][j] = mylist[num][i]
            num += 1 
    return answer
list = [ [1,2,3], [4,5,6], [7,8,9] ]

print(solution(list))
