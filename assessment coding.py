# create a variable to accept user input integer
first_integer = int(input("Please enter an integer: "))
# create a variable to accept user input integer list, each integer seperated by comma
integer_list = str(input("Please enter a list of integer, seperated by comma: "))
# then split the str by comma, which the variable becomes a list
list_integer = integer_list.split(',')

# create two variables for the indexing
start = 0
next_one = 1
# create a new empty list
integer_pair = []
# create a for loop in order to check every pairs in the list
for start in range(len(list_integer)):
    # create a while loop to check every pairs with a certain first item
    while next_one < len(list_integer):
    # accept the pairs when the if statement met
        if int(list_integer[start]) + int(list_integer[next_one]) == first_integer:
            the_pair = [int(list_integer[start]),int(list_integer[next_one])]
            # do not accept duplicated pairs
            if the_pair not in integer_pair:
                integer_pair.append(the_pair)
                # the index of second item add up 1
            next_one +=1
        else:
            # the index of second item add up 1
            next_one +=1
    # when the index of second item greater than the length of the list, 
    # the index of first item add up 1 and the index of second item goes back to 1 bigger than the index of first item
    else:
        start +=1 
        next_one = start + 1
        
