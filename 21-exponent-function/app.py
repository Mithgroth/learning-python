from math import floor

# equal to pow(2,3)
print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(floor(pow_num)):
        result = result * base_num
    
    return result

print(raise_to_power(3, 2))
print(raise_to_power(3.8, 2.4))