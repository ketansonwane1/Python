def fun1():
    a=int(input("Enter a ---"))
    b=int(input("Enter b ---"))
    x=(a,b)
    print("Tuple is",x)
    print("Addition is",sum(x))
    s=x[0]+x[1]
    print("Addition is",s)
