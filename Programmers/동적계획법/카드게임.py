def solution(left, right):
    result = [[0 for _ in range(len(left)+1)]for _ in range(len(right)+1)]
    for r in range(len(right)):
        for l in range(len(left)):
            if left[l] > right[r]:result[r][l] = result[r-1][l] +  right[r]
            else:result[r][l] = max(result[r-1][l-1],result[r][l-1])

    return result[len(right)-1][len(left)-1]
