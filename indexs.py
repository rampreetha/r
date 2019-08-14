def main():
    print("*** Find the index of an element in 1D Numpy Array ***")
 
    # Create a numpy array from a list of numbers
    arr = np.array([11, 12, 13, 14, 15, 16, 17, 15, 11, 12, 14, 15, 16, 17])
 
    # Get the index of elements with value 15
    result = np.where(arr == 15)
 
    print('Tuple of arrays returned : ', result)
    print("Elements with value 15 exists at following indices", result[0], sep='\n')
    print('First Index of element with value 15 is : ', result[0][0])
 
    # If given element doesn't exist in the array then it will return an empty array
    result = np.where(arr == 111)
    print('Empty Array returned : ', result)
    print("value 111 exists at following indices", result[0], sep='\n')
 
    print("*** Find the index of an element in 2D Numpy Array ***")
 
    # Create a 2D Numpy array from list of lists
    arr = np.array([[11, 12, 13],
                    [14, 15, 16],
                    [17, 15, 11],
                    [12, 14, 15]])
 
    print('Contents of 2D Numpy Array', arr, sep='\n')
 
    # Get the index of elements with value 17
    result = np.where(arr == 15)
 
    print('Tuple of arrays returned : ', result)
 
    print('List of coordinates where element with value 15 exists in given 2D array : ')
    # zip the 2 arrays to get the exact coordinates
    listOfCoordinates = list(zip(result[0], result[1]))
    # iterate over the list of coordinates
    for cord in listOfCoordinates:
        print(cord)
 
    print("*** Get the index of an element based on multiple conditions Numpy Array ***")
 
    # Create a numpy array from a list of numbers
    arr = np.array([11, 12, 13, 14, 15, 16, 17, 15, 11, 12, 14, 15, 16, 17])
 
    # Get the index of elements with value less than 16 and greater than 12
    result = np.where((arr > 12) & (arr < 16))
    print("Elements with value less than 16 and greater than 12 exists at following indices", result, sep='\n')
 
    print("*** Get the first index of an element in Numpy Array ***")
 
    result = np.where(arr == 15)
    if len(result) > 0 and len(result[0]) > 0:
        print('First Index of element with value 15 is ', result[0][0])
 
