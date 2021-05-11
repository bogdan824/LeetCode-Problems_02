a = "1010"
b = "1011"
max_len = max(len(a),len(b))
store = ""
a = a.zfill(max_len)
b = b.zfill(max_len)
carry = 0
for i in range (max_len-1,-1,-1):
    aa = int(a[i])
    bb = int(b[i])
    x = aa+bb+carry
    #print("calculam",aa,"+",bb)
    if x == 0:
        val1 = 0
        carry = 0
        store = str(val1) + store
    elif x == 1:
        val1 = 1
        carry = 0
        store = str(val1) + store
    elif x == 2:
        val1 = 0
        carry = 1
        store = str(val1) + store
    else:
        val1 = 1
        carry = 1
        store = str(val1) + store
if carry == 1:
    store=str(carry)+store

print(store)
