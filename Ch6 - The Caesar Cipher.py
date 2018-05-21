#The Caesar Cipher
#凯撒加密法
#key是偏移量，需要key为正整数且0<n<=25
#a是原文，输出的是加密后的密文
key=13
a='This is my secret message.'.upper()
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
if letters.find(a[0])!=-1:
    a=letters[letters.find(a[0])+key]+a[1:]
else:
    a=a
i=1
while(i<=len(a)-1):
    if letters.find(a[i])!=-1:
      a=a[:i]+letters[letters.find(a[i])+key]+a[i+1:]
    else:
      a=a
    i=i+1
print(a)
