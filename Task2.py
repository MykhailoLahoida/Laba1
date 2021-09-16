import sys
if sys.argv[1] == "add":
    print(int(sys.argv[2]) + int(sys.argv[3]))
elif sys.argv[1] == "subtract":
    print(int(sys.argv[2]) - int(sys.argv[3]))
elif sys.argv[1] == "multiply":
    print(int(sys.argv[2]) * int(sys.argv[3]))
elif sys.argv[1] == "divide":
    print(int(sys.argv[2]) / int(sys.argv[3]))
else:
    print("Incorrect input")