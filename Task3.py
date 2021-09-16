Sign = ['+', '-']
Number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
user_input = input("Enter the formula: ")
result = 0
for i in range(len(Number)):
    if user_input[0] == Number[i]:
       result = int(user_input[0])

for i in range(len(user_input)):
    index = False
    if i % 2 == 0:
        for j in range(len(Number)):
            if user_input[i] == Number[j]:
                index = True
        if index == False:
            result = "None"
            break
    else:
        for k in range(len(Sign)):
            if user_input[i] == Sign[k]:
                index = True
        if index == False:
            result = "None"
            break
        if user_input[i] == "+":
            result = result + int(user_input[i+1])
        else:
            result = result - int(user_input[i+1])
print("(" + str(index) + "; " + str(result) + ")")
