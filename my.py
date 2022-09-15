total=0
count=0
average=0
maximum=None
minimum=None
input_num=[]

while True:
    try:
        num=input("Please enter a number：")
        if num=='done':
            break
        else:
            num=float(num)
            input_num.append(num)

    except:
        print("Invaild number.Please try again.")
        continue


    if maximum is None:
        maximum=num
        minimum=num
    elif maximum<num:
        maximum=num
    elif minimum>num:
        minimum=num
for itervar in input_num:
    total=total+itervar
    count=count+1
average=total/count
print(total,count,average)
print("Maximum is: ",maximum)
print("Minimum is: ",minimum)
