''' My Attempt was Greedy Fail '''


# def longest_slide_down(pyramid):
#     result = 0
#     idx = 0
#     count = 0
#     for row in pyramid:
#         if count < 1:
#             print(f'added a : ' , row[0])
#             result += row[0] 
#             count += 1 
#         else :
#             if row[idx] and row[idx+1] and row[idx] > row[idx+1]:
#                 result += row[idx]
#                 print(f'added a : ' , row[idx])
#             else:
#                 result += row[idx+1]
#                 print(f'added b : ' , row[idx+1])
#                 idx+=1  
                
#     return result

# # print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))
# # print(longest_slide_down([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))
# print(longest_slide_down([[10], [10, 20], [10, 10, 20], [10, 90, 10, 20]]))

''' No Recursion / Backtracking need --> Dynamic Programming implemented. '''


def longest_slide_down(pyramid):
    dp = [ row[:] for row in pyramid] #copy pyramid to not change original pyramid
    
    for r in range(len(dp)-2, -1, -1): # second-last row neednot have to update
        for c in range(len(dp[r])):
            dp[r][c] += max(dp[r+1][c], dp[r+1][c+1]) # updating every rows from down to up
            
    return dp[0][0] # value of updated first row is the maximum sum.

print(longest_slide_down([[10], [10, 20], [10, 10, 20], [10, 90, 10, 20]]))