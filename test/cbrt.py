def cbrt(n,epsilon):
    """ approximate the cube root of n """
    low = min(-1,n)
    high = max(1,n) 
    approx = (low + high)/2
    times = 0
    while(abs(approx**3 - n) >= epsilon):
        print("low =", low, "high =", high, "approximate =", approx, "times:", times)
        if(approx**3 < n):
            low = approx
        else:
            high = approx
        approx = (low + high)/2
        times += 1
        if(times > 1000):
            break
    return approx

cbrt(-8,0.000000001)