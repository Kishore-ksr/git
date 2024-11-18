# This is a sample python file to learn working of git
# This program just prints even number and between 1 to 50 and display the count.

c_even = 0
c_odd = 0
for i in range(50):
	if i%2==0:
		print(i)
		c_even +=1
	else:
		c_odd +=1
print("The number of even numbers = ",c_even)
print("The number of odd numbers = ",c_odd)

