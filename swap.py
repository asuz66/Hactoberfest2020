def swap(num1, num2):
        print("Before swapping : " + str(num1) + ' ' + str(num2))
        temp = num1
        num1 = num2
        num2 = temp
        print("After swapping : " + str(num1) + ' ' + str(num2))

swap(10, 20)
