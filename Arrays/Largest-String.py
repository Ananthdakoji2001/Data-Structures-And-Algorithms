### Takes O(n)


s="fun&|| find"
c=0
m=0
for i in range(len(s)):
    if s[i].isalpha():
        c+=1
        if c>m:
            m=c
    else:
        c=0
print(m)






