def brute(n):
  num = 20
  while True:
    for i in range(1,n+1):
      if num % i != 0:
        break
      else:
        print i
        print n
        if i == n:
          return num
      num+=1
    
print brute(2)
