
import csv, math, random

#----------------------------------------------------------------------------------------------#

# Functions

def writeData(filename, tup):
    """ Takes in a string filename, a tuple of 3 FLOAT elements and
        a string. Appends all of the elements to the file on a new
        line in CSV format.
    """
    
    try:
        assert len(tup) == 4
    except:
        print("\nCheck your inputted tuple!")
        return
        
    file = open(filename, 'a')
    for element in tup[0:3]:
        try:
            assert element == float(element)
        except:
            print("\nCheck your inputted tuple!")
            return
        else:        
            file.write(str(element) + ',')
    file.write(str(tup[3]))
    file.write('\n')
    file.close()
    
#------------------------------------------------------------------------------#

def readData(filename, printContents):
    """ Takes in a string filename and a Boolean. If the Boolean is
        True, then the function prints the contents of the file. 
        Returns the contents in an array of tuples.
    """
    
    file = open(filename, 'r')
    lines = file.readlines()
    array = []
    
    if printContents:
        print("\nThe contents of", filename, "are:\n")
        count = 1
        for line in lines:
            print(str(count) + ".)", line.strip())
            count += 1
            temp_tup = ()
            for data in line.strip().split(','):
                temp_tup += (data,)
            array.append(temp_tup)
    file.close()
    
    return array
    
#------------------------------------------------------------------------------#
    
def removeData(filename):
    """ Takes in a string filename and prints its contents.
        Then, it takes in an entry from the file to remove.
        Removes all given entries from the file matching it.
    """
    
    readData(filename, True)
    lines = open(filename, 'r').readlines()
    
    line_num = input("Enter the line of data to remove:\n\n")
    file = open(filename, 'w')
    for line in lines:
        if line.strip() != lines[int(line_num) - 1].strip():
            file.write(line.strip())
            file.write('\n')
    file.close()
    
#------------------------------------------------------------------------------#

def normalizeData(lines):
    """ Takes in an array of tuples of CSV data separated by new lines.
        Normalizes the data and returns this new data as an array of tuples
        along with stats needed to normalize the test data.
    """
    
    first = []  
    second = []   
    third = []
    
    for line in lines:
        first.append(float(line[0]))
        second.append(float(line[1]))
        third.append(float(line[2]))

    #----------------------------------------------#
    
    # Map all values into the interval [0, 1]
    first_max, first_min = max(first), min(first)
    first_range = first_max - first_min
    new_first = []
    for num in first:
        try:
            new_first.append((num - first_min) / first_range)
        except:
            continue
        
    second_max, second_min = max(second), min(second)
    second_range = second_max - second_min
    new_second = []
    for num in second:
        try:
            new_second.append((num - second_min) / second_range)
        except:
            continue
        
    third_max, third_min = max(third), min(third)
    third_range = third_max - third_min
    new_third = []
    for num in third:
        try:
            new_third.append((num - third_min) / third_range)
        except:
            continue
        
    stats = [first_min, first_range, second_min, 
             second_range, third_min, third_range]
    
    #----------------------------------------------#

    final_tuples = []
    for num in range(len(first)):
        try:
            yes_no = []
            # 88/175 chance of yes and 87/175 chance of no
            for value in [new_first[num], new_second[num], new_third[num]]:
                if value <= .3:
                    for a in range(4):
                        yes_no.append("No")
                    yes_no.append("Yes")
                elif value > .3 and value < .6:
                    for a in range(2):
                        yes_no.append("No")
                    yes_no.append("Yes")
                else:
                    yes_no.append("No")
                    for a in range(6):
                        yes_no.append("Yes")
            label = random.choice(yes_no)
            final_tuples.append((new_first[num], new_second[num], 
                                 new_third[num], label))
        except:
            continue
        
    return final_tuples, stats

#------------------------------------------------------------------------------#

def getDistance(t1, t2):
    """ Calculates and returns the Euclidean distance
        between two tuples
    """
    
    sum_sq = 0

    if len(t1) == len(t2):
        for num in range(len(t1)):
            sum_sq += (t2[num] - t1[num]) ** 2
        return math.sqrt(sum_sq)  
    
    elif len(t1) > len(t2):
        diff = len(t1) - len(t2)
        t2 += (0,) * diff  
        for num in range(len(t1)):
            sum_sq += (t2[num] - t1[num]) ** 2
        return math.sqrt(sum_sq)
    
    else:
        return getDistance(t2, t1)
    



