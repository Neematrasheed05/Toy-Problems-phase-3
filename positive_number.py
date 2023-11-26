def positive_number(a,b,c):
        # Checks if any numbers are positive
    if (a > 0 or b > 0) or (b > 0 and c > 0):
        return True
    else:
        return False
    
print(positive_number(4, -6, 9))
    