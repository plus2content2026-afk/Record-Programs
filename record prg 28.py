R={"OM":76, "JAI":45, "BOB":89, "ALI":65, "ANU":90, "TOM":82}
stack=[]
def PUSH(R):
    l1 = list(R.keys())
    for i in R:
        if R[i] > 75:
           stack.append(i)

    print(stack)
def POP():
    while len(stack)>0:
        print(stack.pop(),end=" ")
    else:
        print("Stack Underflow")
while True:
    choice = int(input("Enter 1 to push or 2 to pop,3 to stop"))
    if choice == 1:
        PUSH(R)
    elif choice ==2:
        POP()
    elif choice ==3:
        break
    
