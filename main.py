def power(base,pow,modulus):
    if pow==0:
        return 1
    if pow==1:
        return (base)%modulus
    halfPower=power(base,pow//2,modulus)
    if pow&1==0:
        return (halfPower*halfPower)%modulus
    return (halfPower*halfPower*base)%modulus

print(power(*map(int,input().split())))