def islower(c):
    return ord('a') <= ord(c) <= ord('z')

def check_case(c):
    if ord('a') <= ord(c) <= ord('z'):
        print(f"{c} is lower")
    elif ord('A') <= ord(c) <= ord('Z'):
        print(f"{c} is upper")
    else:
        print(f"{c} is not a letter")

check_case('a')
check_case('H')
check_case('A')
check_case('3')
check_case('g')
