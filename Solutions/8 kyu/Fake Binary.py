def fake_bin(x):
# option 1
#     res=''
#     for c in x:
#         res+= '0' if int(c)<5 else '1'
#     return res
# option 2
#     return ''.join('0' if int(c)<5 else '1' for c in x)
# option 3
    x = list(x)
    for i, c in enumerate(x):
        x[i] = '0' if int(c)<5 else '1'
    return ''.join(x)
    
