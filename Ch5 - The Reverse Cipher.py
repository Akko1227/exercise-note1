#Reverse Cipher
#http://inventwithpython.com/hacking(BSD Licensed)
#反转加密法
message='I like for you to be still.'
a=''
i=len(message)-1
while(i!=-1):
    a=a+message[i]
    i=i-1
print(a)
