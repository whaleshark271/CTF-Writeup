from Crypto.Util.number import inverse

p = 698485749536180936399303063789
q = 1187691164211371725536146312471
phi = (p-1)*(q-1)
e = 3
n = p * q
d = inverse(e, phi)
ct = 723480078313583262942069801141894355731968051669034152256286

pt = pow(ct, d, n)
hex_pt = hex(pt)
flag = bytes.fromhex(hex_pt[2:])
print(flag)