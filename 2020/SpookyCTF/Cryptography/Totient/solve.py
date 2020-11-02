import gmpy2
from Crypto.Util.number import inverse

gmpy2.get_context().precision=4096

n = 3332188378295875783869064122703412230143264268626208625352231809707004626253693498892823264566220909462343272078555847886616528581762042090546179170482236487869003184706780657600698382325015809116744248893806650852223735783470295773006852652525553466007962717720284304724619241395637108961365171979649
e = 65537
ct = 3316983025788692017396821771835311006322014015027406970602003270080890623639030751135640062117695237676733971772109533247669892340663705733239749827632105244781062716356677792105791119992377197378659424691710778109509477222535640626877439474417447571477422236539760920897186204634495349674479974912987
p = int(gmpy2.sqrt(n))
phi = n-p
d = inverse(e, phi)


pt = pow(ct, d, n)
hex_pt = hex(pt)
flag = bytes.fromhex(hex_pt[2:])
print(flag)