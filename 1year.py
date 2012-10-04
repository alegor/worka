#!/usr/bin/env python

year = raw_input('enter year ')
while str(year).isdigit() == False:
year = raw_input('enter year ')
if(int(year)%4 == 0 and int(year)%100!=0) or int(year)%400 == 0:
print '%s is leap' %year
else:
print '%s is not leap' %year