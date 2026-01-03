def dir_reduc(arr):
    if not arr:
        return arr
    
    opposite_direction = {'EAST' : 'WEST', 'NORTH':'SOUTH', 'WEST':'EAST', 'SOUTH':'NORTH'}
    result = []
    for direction in arr :
        if result and result[-1] == opposite_direction[direction]:
            result.pop()
        else: 
            result.append(direction)
    return result

print(dir_reduc(["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"]))
