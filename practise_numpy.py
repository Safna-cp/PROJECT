import numpy as np
# a= np.array([1, 2, 3, 4, 5, 6,])
# print(a)


# print(np.zeros((2,3)))
# print(np.ones((2,2)))

# a=np.arange(0,10,2)  # arrange array from 0 to 10 
# print(a)

# reshape(it changes the shape of the numpy array without changing its data)
# b=a.reshape((2, 3))
# print("reshaped array is :",b)

# print(np.mean(a))
# print(np.median(a))
# print(np.std(a))

# a=np.random.rand()
# print(a)
# b=np.random.rand(5)
# print(b)
# c=np.random.rand(2,3)
# print(c)

# x=np.random.randint(1,10)
# print(x)
# y=np.random.randint(0,100, size=5)
# print(y)
# z=np.random.randint(10,21, size=(3,3))
# print(z)



# Generate a random 6-digit number between 100000 and 999999
otp = np.random.randint(100000, 1000000)
print(otp)
