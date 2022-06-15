rectangle = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 1, 0],
             [0, 1, 0, 1, 1, 0],
             [1, 1, 1, 1, 1, 1]]

def largestRec(rec):
    #initalize variables
    count = 0
    indexFrom = -1 #set to -1 until we find a filled square
    height = len(rec)
    listOfRecSizes = []

    #loop through entire array
    for j in range(len(rec)):
        for i in range(len(rec[0])):
            if indexFrom == -1: #check if we haven't come across a filled square yet
                if (rec[j][i] == 1): #check if it's a filled square
                    count += height - j #Add length of height to count since we know every square below this column must be filled
                                        #(height - j) because we are traversing down the 2d array instead of up
                    indexFrom = i #set index from to be current column
            else: #already have an index from, so check if there are more filled squares in this row
                if (rec[j][i] == 1): #check if this square is filled
                    count += height - j #if sqaure is filled, add height to count
                    if len(rec[j]) == i + 1: #check if we are at the end of the row
                        listOfRecSizes.append(count) #found rectangle, append to list
                        indexFrom = -1 #reset indexFrom
                        count = 0 #reset count
                else: #square is not filled, we can add the count to list of sizes and reset variables
                    listOfRecSizes.append(count) #found rectangle, append to list
                    indexFrom = -1 #reset indexFrom
                    count = 0 #reset count

    return max(listOfRecSizes) #return largest rectangle

print(largestRec(rectangle))
