"""•连续输入字符串，请按长度为8拆分每个输入字符串并进行输出；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
（注：本题有多组输入）
"""

while True:
    try:
        s=input("请输入一串字符串:")
        if len(s)<8:
            s_new = s+"0"*(8-len(s))
            print(s_new)
        else:
            n=len(s)%8
            if n !=0:
              s= s +"0"*(8-n)
            n1 = int(len(s) / 8)
            for i in range(0,n1):
                 s_new = s[i*8:i*8+8]
                 print(s_new)
    except:
        break