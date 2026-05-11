#=======================================================================================================================
# TASK 1 SUPERNACCI
#
#=======================================================================================================================

def supernacci(n):
    s = [1]
    # Loop from 2 since 1 = 1
    for i in range(2, n+1):
        num_terms = (i - 1) % 3
        if num_terms == 0:
            # If 0 get the last element
            temp = s[- 1]
        else:
            # sum the last num_term elements, using slice
            temp = sum(s[-num_terms:])
        s.append(temp)
    return s[n-1]

# Desired element we wish to append
result = supernacci(5)

print(supernacci(result))