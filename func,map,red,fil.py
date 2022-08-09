# a=["1","2","3","4","5"]
# for i in range(len(a)):
#     a[i]=int(a[i])
#     print(a[i])         #1 to 5 print vertically

# v=["10","20","30","40"]
# b=list(map(int,v))
# print(b)                 #[10, 20, 30, 40]

#his method print square of given number
# def sq(y):
#     return y*y
# n=[2,3,4,5,6]
# s=list(map(sq,n))
# g=list(map(lambda x:x*x,n))
# print(s)           # [4, 9, 16, 25, 36]
# print(g)           # [4, 9, 16, 25, 36]


##this print number of square and cube side by side from 1 to 5
# def square(s): return s*s           [1, 1]
# def cube(c): return c*c*c            [4, 8]
# f=[square,cube]                     [9, 27]
# for i in range(1,6):                [16, 64]
#     a=list(map(lambda x:x(i),f))     [25, 125]
#     print(a)      

# using this method we can print greater than OR less than number
# a=[1,2,3,4,5,6,7,8,9,10]
# def gr(n):
#     return n>5
# def ls(n):
#     return n<5
# v=list(filter(gr,a))
# b=list(filter(ls,a))
# print(v)                    #[6, 7, 8, 9, 10]
# print(b)                     #[1, 2, 3, 4]

# using this we can add number in given list
# from functools import reduce
# e=[5,10,15,20,25]
# n=reduce(lambda x,y: x+y,e)
# print(n)               #75