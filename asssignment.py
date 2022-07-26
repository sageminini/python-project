numbers = [10, 20, 33, 46, 55, 62, 70]
for val in numbers:
    if (val % 5 == 0):
        print(val)

def calculate_tax (income):
    """A function to calculate the tax from income"""
    if income <= 10000:
        taxAmount = 0
    else:
        taxAmount = (income - 10000) * 0.3
    
    print('The tax for the income',income, '=', taxAmount)

    
calculate_tax (45000)


number1 = 20
number2 = 30
i = int(20)
j = int(30)
prod=i*j
sum=i+j

if prod <= 1000:
    print(prod)
else:
    print(sum)


number1 = 40
number2 = 30
i = int(40)
j = int(30)
prod=i*j
sum=i+j

if prod <= 1000:
    print(prod)
else:
    print(sum)



    # A function for nth fibronacci number

    def fibonacci(n):
        if n <= 0:
            return incorrect
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibonacci(n-1)+fibonacci(n-2)


    print(fibonacci(13))

