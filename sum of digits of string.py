def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit += z
    return sum_digit
print(sum_digits_string("123abc45"))
