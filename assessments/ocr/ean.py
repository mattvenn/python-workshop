def checksum(product_code):
    digit = 0
    checksum = 0
    for digit in range(0,12):
        num = product_code[digit]
        if digit % 2 != 0:
            checksum += int(num) * 3
        else:
            checksum += int(num)
    print("checksum: ", checksum)
    #round up to 10
    non_decade = checksum % 10
    check = 10 - non_decade
    print("check digit: ", check)
    return str(check)


#get a code from the user and check it
def test():
    product_code = input('13 digit ean')

    if len(product_code) != 13:
        print("bad length, must be 13")
        exit(1)

    print(product_code)

    if checksum(product_code) == product_code[12]:
        print("correct code")
    else:
        print("incorrect code")

#build a code
def make():
    #make one
    country = '978'
    business = '034'
    product = '099789'
    product_code = country + business + product

    print(product_code + checksum(product_code))

make()
test()
