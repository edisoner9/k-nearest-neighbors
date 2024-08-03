
def random_kNN(filename, sample_size, k):
    """ Runs the k-nearest neighbors algorithm on a given 4-column
        CSV file where:
            -the first 3 columns are labels, 
            -the 4th column is the classifier
            -all non-label data is generated randomly
        The input filename represents the name of the CSV file to create
        and hold raw sample data.
        The variable sample_size must be a natural number greater 
        than k representing the number of random sample rows 
        to create.
    """
    
    if sample_size < k:
        print("Sample size must be greater than k!")
        return
    
    # Create and store sample data
    for num in range(sample_size):
        f1 = random.uniform(-10, 10)
        f2 = random.uniform(1, 100)
        f3 = random.uniform(0, 2 * math.pi)
        label = ""
        data = (f1,) + (f2,) + (f3,) + (label,)
        functions.writeData(filename, data)
    
    # Display, normalize, and store sample data
    norm_filename = "normalized_" + filename
    lines = functions.readData(filename, True)
    norm_data, stats = functions.normalizeData(lines)
    for tup in norm_data:
        for elem in tup:
            file = open(norm_filename, 'a')
            file.write(str(elem) + ',')
        file.write("\n")
    
    #----------------------------------------------#
    
    # Create and normalize the data to classify using kNN
    f1 = random.uniform(-10, 10)
    f2 = random.uniform(1, 100)
    f3 = random.uniform(0, 2 * math.pi)
    
    print("\n", "-" * 100)
    print("\nData to classify:", (f1, f2, f3), "\n")
    print("-" * 100)
    
    # stats = 1st min, 1st range, 2nd min, 2nd range, 3rd min, 3rd range
    new = ((f1 - stats[0]) / stats[1], (f2 - stats[2]) / stats[3], 
           (f3 - stats[4]) / stats[5])
    
    print("\nNormalized data to classify:", new, "\n")
    print("-" * 100)
    
    #----------------------------------------------#
     
    # Compute distance from new data to normalized 
    # all normalized tuples and choose the majority 
    # label of the top k closest tuples.
    # We construct a dictionary to map each tuple
    # to its distance from the new data.
    distance_dict = {}
    distances = []
    
    for tup in norm_data:
        tup_dist = functions.getDistance(tup[0:3], new)
        distances.append(tup_dist)
        distance_dict[tup] = tup_dist
    
    sorted_dist = sorted(distances)
    labels = []
    for tup in distance_dict:
        if distance_dict[tup] in sorted_dist[-k:]:
            labels.append(tup[3])
            
    
    print(labels)
    print("\nFinal classification: ", statistics.mode(labels))

#----------------------------------------------------------------------------------------------#

random_kNN("data.csv", 200, 30)



    
