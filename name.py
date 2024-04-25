import sys
# try:
#     print("hello, my name is:", sys.argv[1])
#     print("the name of the file is:", sys.argv[0])
#     #  What is in sys.argv[0]? the name of the file
# except IndexError:
#     print("No arguments found")

# Another (better) way:
# if len(sys.argv) < 2:
#     print("No arguments found")
# elif len(sys.argv) > 3:
#     print("Too many arguments given")
# else:
#     print("hello, my name is:", sys.argv[1])
#     print("the name of the file is:", sys.argv[0])

# better formatted using sys.exit:
# if len(sys.argv) < 2:
#     sys.exit("No arguments found") #Prints the line but exits immediately ignoring any subsequent errors
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments given") #Prints the line but exits immediately ignoring any subsequent errors

# print("hello, my name is:", sys.argv[1])
# print("the name of the file is:", sys.argv[0])


# What if we have a multiple number of arguments?
if len(sys.argv) < 2:
    sys.exit("No arguments found") #Prints the line but exits immediately ignoring any subsequent errors
# for arg in sys.argv:
#     print("hello, my name is", arg)
# Use slices:
for arg in sys.argv[1:]:
    print("hello, my name is", arg)


