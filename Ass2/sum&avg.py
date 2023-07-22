numbers=[]
while((n:=int(input('Enter any number or 0 to exit: ')))!=0):
    numbers.append(n)
print('Numbers : ',numbers)
print('Sum',sum(numbers)) 
print('Average', sum(numbers)/len(numbers))