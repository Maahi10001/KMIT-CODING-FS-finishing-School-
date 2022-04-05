'''
Sunder is given a number(num).
He will apply the following rules only 2 times 

Pick a digit x (9 >= x >=0) .
Pick another digit y (9 >= y >= 0) . The digit y can be equal to x .
Replace all the occurrences of x in the decimal representation of num by y .
The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.
Return the max difference between a and b .

Example 1:
Input = 555
Output = 888

Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888


Example 2:
Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8

Input = 123456
Output = 820000

Explanation:
The first time pick x=1 and y=9 and store the new integer in a(a=923456)
The second time pick x=2 and y=0 and store the new integer in b (b=103456)
Now a-b becomes 820000


Input = 10000
Output = 80000
Explanation:
The first time pick x=1 and y=9 and store the new integer in a(a=90000)
The second time pick x=9 and y=1 and store the new integer in b (b=10000)
Now a-b becomes 80000


'''
#solution
def getmax(s):
    mx_str=" "
    mx_list=[]
    for i in range(len(s)):
        if s[i]!='9':
            mx_str=s[i]
            break
    for i in range(len(s)):
        if s[i]==mx_str:
            mx_list.append('9')
        else:
            mx_list.append(s[i])
    #print(str("".join(mx_list)))   
    return str("".join(mx_list))
def getmin(s):
    mi_str=" "
    temp=" "
    a=[]
    if s[0]=='1':
        for i in range(1,len(s)):
            if s[i]!='0':
                if s[i]=='1':
                    continue
                else:
                    temp=s[i]
                    mi_str='0'
                    break
    else:
        temp=s[0]
        mi_str='1'
    for i in range(len(s)):
        if s[i]==temp:
            a.append(mi_str)
        else:
            a.append(s[i])
    #print(str("".join(a)))
    return str("".join(a))
def getdiffer(n):
    s=str(n)
    mx=int(getmax(s))
    mi=int(getmin(s))
    #print(mx,mi)
    return mx-mi
if __name__=="__main__":
    n=int(input())
    print(getdiffer(n))
    
