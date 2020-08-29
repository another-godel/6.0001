def cbrt(n,epsilon):
    """ approximate the cube root of n """
    low = min(-1,n)
    high = max(0,n) 
    approx = (low + high)/2
    times = 0
    while(abs(approx**3 - n) >= epsilon):
        times += 1
        print("low =", low, "high =", high, "approximate =", approx, "times:", times)
        if(approx**3 > n):
            high = approx
        else:
            low = approx
        approx = (low + high)/2
    return approx

cbrt(9,0.000000001)