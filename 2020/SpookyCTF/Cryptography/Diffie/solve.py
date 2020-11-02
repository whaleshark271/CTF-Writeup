for a in range(1000):
    if pow(7, a, 999331)==858076:
        print("a:" + str(a))
        break

for b in range(500):
    if pow(7, b, 999331)==346579:
        print("b:" + str(b))
        break
        
secret = pow(346579, a, 999331)
print("secret:" + str(secret))