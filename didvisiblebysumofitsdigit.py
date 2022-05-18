num = int(input("enter two digits: "))
var1 = 0
var2 = 0 + num
var3 = 0
while num > 0:
    digit = num % 10
    var1 = var1 + digit
    num = num // 10

    var3 = (var2 / var1)

    print(var3)
