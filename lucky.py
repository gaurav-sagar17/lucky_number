
def lucky(num,k) :
    even_sum = 0 
    odd_sum = 0 
    digits = 0 
    copy = num
    flag = 1
    while(copy > 0) :
        if(flag == 1) :
            odd_sum += copy%10 
            flag = 0

        else :
            even_sum += copy%10 
            flag =1 
        digits += 1
        copy = copy // 10 

    if(digits%2 == 0) :
        temp = even_sum 
        even_sum = odd_sum 
        odd_sum = temp 

    # print(even_sum ) 
    # print(odd_sum ) 
    copy = num 
    if(odd_sum <= even_sum) :
        return num 
    ## uusing divide and conquer
    # dividing 
    full_rev = 0 
    while(copy > 0) :
        d= copy%10 
        full_rev = full_rev*10 + d 
        copy = copy // 10

    track = 0 
    last_k = full_rev%(10**k) 
    rest = 0 
    while(full_rev > 0) :
        if(track < k) :
            # d = full_rev%10 
            # k_rev = k_rev*10 + d
            full_rev = full_rev//10 
            track += 1 
        else :
            d = full_rev%10 
            rest = rest*10 + d
            full_rev = full_rev//10 

    # print(full_rev) 
    # print(last_k) 
    # print(rest)
    

    # print(rest) 

    ## conquer 

    
    for i in range(k) :
        d = last_k%10 
        rest = rest*10 + d
        last_k = last_k//10
     
    lucky_num = rest
    return lucky_num 




lucky(123456789,3)







    

