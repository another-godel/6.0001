def sqrt(n,epsilon):
    """ approximate the square root of n """
    low = 0
    high = (n+1)/2 #sqrt(n) =< (n+1)/2  
    approx = (low + high)/2
    times = 0
    while(abs(approx**2 - n) >= epsilon):
        times += 1
        print("low =", low, "high =", high, "approximate =", approx, "times:", times)
        if(approx**2 > n):
            high = approx
        else:
            low = approx
        approx = (low + high)/2
    return approx

sqrt(25,0.01)