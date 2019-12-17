'''Power Of A Number

Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
Input format :
Two integers x and n (separated by space)
Output Format :
x^n (i.e. x raise to the power n)
Sample Input 1 :
 3 4
Sample Output 1 :
81
Sample Input 2 :
 2 5
Sample Output 2 :
32'''

def power(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        return x*power(x,n-1)

x,n=[int(i) for i in input().split()]
print(power(x,n))
