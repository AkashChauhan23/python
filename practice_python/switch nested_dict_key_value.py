i_d = {"a":{"b":{}},"c":{"d":{}},"e":{"f":{}}} 

o_d={"b":{"a":{}},"d":{"c":{}},"f":{"e":{}}}

d = {}
for k, v in i_d.items():
    for k1, v1 in v.items():
        d[k1] = {k: v1}

print(d)