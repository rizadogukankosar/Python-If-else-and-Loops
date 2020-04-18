# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:45:52 2020

@author: doguk
"""  

#LOOPS

#FOR 1
numbers = [4,9,7,2,5]
sum = 0
for value in numbers:
    sum += value
    
print(sum)

#FOR 2
sum = 0
for value in range(0, 5):
    sum += value
    
print(sum) # 10 --> 0+1+2+3+4= 10
    

# WHILE
sum = 0
i =0
while i< 5:
    sum+=i
    i +=1
    
print(sum) # 10 --> 0+1+2+3+4= 10



