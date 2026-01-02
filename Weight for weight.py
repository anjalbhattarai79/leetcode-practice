def order_weight(strng=''):
    if not strng:
        return strng
    
    numbers = strng.split()
    
    weighted = []
    for number in numbers:
        weight = 0
        for digit in number:
            weight += int(digit)
        weighted.append((weight, number))
    
    weighted.sort(key=lambda x: (x[0], x[1])) # first sort on basis of x[0] ie. weight, if both eqyal than go x[1] ie. number (sent as strng, so lexicography used.)
    
    return " ".join(num for _, num in weighted)