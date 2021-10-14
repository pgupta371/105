import csv
import math

with open("datastd.csv") as f:
    reader=csv.reader(f)
    file_data=list(reader)

#sort data to get the list
data=file_data[0]

def mean(data):
    n=len(data)
    t=0
    
    for x in data:
        t +=int(x)

    mean=t/n
    return mean


squared_list=[]
for number in data:
    a= int(number)-mean(data)
    a=a**2
    squared_list.append(a)

## sum of all
sum=0
for i in squared_list:
    sum +=i 

#divide the sum by total values
result=sum/(len(data)-1)

#get the standard deviation by taking square root of the result
std_dev=math.sqrt(result)
print(std_dev)

