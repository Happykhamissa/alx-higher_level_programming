#!/usr/bin/python3
a = 10
b = 5

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)

    print("{a} + {b} = {result_add}".format(a=a, b=b, result_add=result_add))
    print("{a} - {b} = {result_sub}".format(a=a, b=b, result_sub=result_sub))
    print("{a} * {b} = {result_mul}".format(a=a, b=b, result_mul=result_mul))
    print("{a} / {b} = {result_div}".format(a=a, b=b, result_div=result_div))
