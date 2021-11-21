temperatures = [30, 34, 32, 18, 10, 20, 8]
max = temperatures[0]
sum = 0
for t in temperatures:
    sum += t
    if t > max:
        max = t
average = sum/len(temperatures)
print("The average is " + str(average))
print("The maximum is " + str(max))
 
copy_list = temperatures.copy()
copy_list.sort()
top =3
top_list=[]
for t in range(top):
    top_list.append(copy_list[t])
print("The lowest three temperatures are: " +str(top_list) )