def fact(n):
    return fact_aux(n,1)

def fact_aux(n,result):
    if n==0:
        return result
    else:
        return fact_aux(n-1,n*result)
;
