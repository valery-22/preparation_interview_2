numbers = [1, 2, 3, 4, 5]

def solution(numbers):
    #TODO: Implement the solution here
    n = len(numbers)
    result = []
    for i in range((n + 1) // 2):
        result.append(numbers[i] + numbers[n - 1 - i])
    return result
    
print(solution(numbers))