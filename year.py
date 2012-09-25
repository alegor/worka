#!/usr/bin/env python 
year = input('enter year ')
if(year%4 == 0 and year%100!=0) or year%400 == 0:
print '%s is leap' %year
else:
print '%s is not leap' %year