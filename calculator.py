def calculator(n1,n2,op):
    match op:
        case '+':
            ans=n1+n2
        case '-':
            ans=n1-n2
        case '*':
            ans=n1*n2
        case '/':
            if n2==0:
                return "Answer is infinity"
            elif n1==0:
                return "Answer is zero"
            else:
                ans=n1/n2
        case'%':
            if n2==0:
              return "Modulus is not possible"
            else:
                ans=n1%n2   
        case _:
            return "Invalid operator"
    return ans       
i=1
while i==1:
    n1,n2=map(int,input("Enter the two operands(add space in between)").split())
    op=input("Enter operator")
    print(calculator(n1,n2,op))
    i=int(input("Enter 0 to exit, 1 to continue"))