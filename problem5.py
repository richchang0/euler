def brute(n):
  num = 0
  check_range = list(reversed(range(1,n+1)))
  while True:
    if num != 0 and check_divisible(num, check_range):
      return num
    else:
      #num += n
      num += 2520 #given smallest number divisible by 1-10.
                  #adding this makes this solution specific to inputing 20 
 
def check_divisible(num, check_range):
  for i in check_range:
    if num % i != 0:
      return False
  return True

print brute(20)
