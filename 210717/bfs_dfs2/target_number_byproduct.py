from itertools import product

def solution(numbers, target):
    length = len(numbers)
    # 전체 가능한 case 구하기
    cases = []
    for _ in range(length):
        cases.append([-1, 1])
    cases = list(product(*cases)) #곱집합 product

    # target 인 경우만 count 하기
    count = 0
    for case in cases:
        s = 0
        for i in range(length):
            s += case[i] * numbers[i]
        if s == target:
            count += 1
    return count

print(solution([1, 1, 1, 1, 1], 3))


#
def solution(numbers, target):
    tree = [0]
    for num in numbers:
        sub_tree = []
        for tree_num in tree:
            sub_tree.append(tree_num + num)
            sub_tree.append(tree_num - num)
        tree = sub_tree
    return tree.count(target)



#

answer = 0 

def dfs(idx, numbers, total_sum, target): 
    global answer 
    n = len(numbers) # 마지막 원소까지 계산했다면 return 
    if idx == n - 1: 
        # 타겟 넘버를 만드는 경우 
        if total_sum == target: 
            answer += 1 
            return 
        # 다음 원소를 더할 경우 
        dfs(idx + 1, numbers, total_sum + numbers[idx + 1], target) 
        # 다음 원소를 뺄 경우 
        dfs(idx + 1, numbers, total_sum - numbers[idx + 1], target) 
        
def solution(numbers, target): 
    global answer 
    dfs(-1, numbers, 0, target) 
    return answer

