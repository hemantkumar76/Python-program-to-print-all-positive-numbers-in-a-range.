#hemant assignment 2 MY CAPTAIN 
positive_list = []

n = int(input("Enter the lower part of your list "))

m = int(input("Enter the upper part of your list "))

if n & m <0:

    print("There is no positive number in the given range")

else:

    for i in range(n,m+1):

        if i >= 0:

            positive_list.append(i)

    print("Positive numbers for  range {0} and {1} using for loop are {2}".format(n, m, positive_list))
