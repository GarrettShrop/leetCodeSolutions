def solve_pyramid_dp(pyramid, target):
  pyramid_array = []
  start = 0

  for i in range(1,len(pyramid) + 1):
    row = [int(x) for x in pyramid[start:start + i]]
    pyramid_array.append(row)
    start += i

  n = len(pyramid_array)
  dp = [{} for _ in range(n)]
  paths = [{} for _ in range(n)]

  dp[0][0] = {pyramid_array[0][0]: True}
  paths[0][0] = {"": True}


  for i in range(n-1):
    for j in range(len(pyramid_array[i])):
      for product in dp[i][j]:
        #Left path
        new_product = product * pyramid_array[i+1][j]
        if new_product not in dp[i+1][j]:
          dp[i+1][j][new_product] = True
          for path in paths[i][j]:
            paths[i+1][j][path + "L"] = True
