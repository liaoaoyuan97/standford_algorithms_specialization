def add(x, y):
    '''
    x:string
    y:string
    return:string
    '''
    nx = len(x);
    ny = len(y)
    n = max(nx, ny)
    if nx < ny:
        x = "0" * (ny - nx) + x
    elif ny < nx:
        y = "0" * (nx - ny) + y
    num = [0 for i in range(n + 1)]
    for i in range(n):
        tmp = int(x[n - i - 1]) + int(y[n - i - 1]) + num[i]
        num[i] = tmp % 10
        num[i + 1] = tmp / 10
    result = ""
    for i in range(n):
        result = str(num[i]) + result
    if num[n] != 0:
        result = str(num[n]) + result
    return result


def substract(x, y):
    '''
    x:string
    y:string
    return:string
    '''
    nx = len(x);
    ny = len(y)
    n = max(nx, ny)
    if nx < ny:
        x = "0" * (ny - nx) + x
    elif ny < nx:
        y = "0" * (nx - ny) + y
    num = [0 for i in range(n)]
    for i in range(n):
        tmp = num[i] + int(x[n - 1 - i]) - int(y[n - 1 - i])
        if tmp < 0:
            num[i + 1] -= 1
            tmp += 10
        num[i] = tmp

    result = ""
    zero_flag = False
    for i in range(n):
        if not zero_flag and num[n - 1 - i] != 0:
            zero_flag = True
        if zero_flag:
            result = result + str(num[n - 1 - i])
    if not zero_flag:
        return "0"
    return result


def KaratsubaMultiplication(x, y):
    '''
    x:string
    y:string
    return:string
    '''
    nx = len(x);
    ny = len(y);
    n = max(nx, ny)
    if nx < n:
        x = "0" * (n - nx) + x
    elif ny < n:
        y = "0" * (n - ny) + y
    if n == 1:
        return str(int(x[0]) * int(y[0]))
    if n % 2 == 0:
        n_div_2 = n / 2
    else:
        n_div_2 = (n + 1) / 2
        x = "0" + x
        y = "0" + y
    a = x[:n_div_2];
    b = x[n_div_2:]
    c = y[:n_div_2];
    d = y[n_div_2:]
    ac = KaratsubaMultiplication(a, c);
    bd = KaratsubaMultiplication(b, d)
    # bc = KaratsubaMultiplication(b, c);
    # ad = KaratsubaMultiplication(a, d)
    # mid = add(bc, ad)
    multipliers = KaratsubaMultiplication(add(a,b),add(c,d))
    mid=substract(substract(KaratsubaMultiplication(add(a,b),add(c,d)),ac),bd)
    tmp_result=add(add(ac + "0" * (n_div_2*2), mid + "0" * n_div_2), bd)
    flag_zero=False;result=""
    for i in range(len(tmp_result)):
        if tmp_result[i]!=0:
            flag_zero=True
        if flag_zero:
            result=result+tmp_result[i]

    return result




print KaratsubaMultiplication("3141592653589793238462643383279502884197169399375105820974944592","2718281828459045235360287471352662497757247093699959574966967627")