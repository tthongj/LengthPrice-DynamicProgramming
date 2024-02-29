def cut_rod(prices, n):
  revenue = [0 for i in range(n+1)]

  for i in range(1, n+1):  #Length of rod.
      max_val = -1
      for j in range(i):  #Cut the rod in to two pieces.
          max_val = max(max_val, prices[j] + revenue[i-j-1])
      revenue[i] = max_val

  return revenue[n]

if __name__ == "__main__":
  #prices[i] is the price of a rod of length i+1
  prices = [2, 3, 7, 8]
  length_of_rod = len(prices)
  print("Maximum revenue is", cut_rod(prices, length_of_rod))
