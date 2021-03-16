def solution(budgets, M):
    budgets = sorted(budgets)
    left_sum = sum(budgets)
    max_budget = budgets[-1]
    min_budget = budgets[0]
    length  = len(budgets)
    budget_arr = [0 for _ in range(max_budget+1)]
    for budget in budgets: budget_arr[budget] += 1
    up_count = 0
    for upper_limit in range(max_budget,-1,-1):
        if left_sum <= M: return upper_limit
        up_count += budget_arr[upper_limit] 
        left_sum -= up_count
        
#     budgets = sorted(budgets)
#     left_sum = sum(budgets)
#     max_budget = budgets[-1]
#     min_budget = budgets[0]
#     length = len(budgets)-1

#     hi = 0



#     for upper_limit in range(max_budget,-1,-1):
#         count = 0

#         for i in range(length, -1, -1):
#             if budgets[i] > upper_limit :
#                 count += 1

#                 hi+=count
#             else : break
#         length -= count
#         left_sum -= hi


#         if left_sum <= M : return upper_limit
#     return 1
