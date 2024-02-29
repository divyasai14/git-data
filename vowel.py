'''
str=input()
vowel="aeiouAEIOU"
for i in str:
    if i in vowel:
        print(i,end=" " )
'''

s="aaaabbbccdd
"
for i in s:
    print(chr(ord(i)-32),end="")
