# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# This is the first kata in series:

# Find the unique number (this kata)
# Find the unique string
# Find The Unique

def find_uniq(arr): #Don't handle all edge-cases eg: [0, 1, 1, 1]
    first_num = arr[0]
    
    for num in arr:
        if first_num != num:
            return num
    
       # n: unique number in the array
       
print(find_uniq([1, 2, 1, 1, 1]))

def find_uniq(arr): #Handles all edge-cases
    a , b ,c = arr[0] , arr[1], arr[2]
    
    if a== b or a==c :
        common = a
    else:
        common = b
           
    for num in arr:
        if num != common:
            return num
        
        