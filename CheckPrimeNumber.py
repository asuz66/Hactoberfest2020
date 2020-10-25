from numpy.lib.scimath import sqrt

def check_primenumber(num):
    count = 0
    for i in range(1, int(sqrt(num))+1):
        if num % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False
         

print(check_primenumber(13))
