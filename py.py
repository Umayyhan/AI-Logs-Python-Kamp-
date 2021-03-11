# NUMPY LIB giris 
import numpy as np

numbers_arr =np.array([1,2,"3",9,4,6],np.int)
#print(numbers_arr)
numbers_arr =numbers_arr.reshape(2,-1)
#sutunu kendi ayarliyor
numbers_arr.shape
#print(numbers_arr)
numbers_arr[0]=1 
#all first row is 1
print(numbers_arr)
numbers_arr[0]= [1,2,3] 
#first row is [1,2,3]
print(numbers_arr)
print(np.cos(numbers_arr))
print(np.sin(numbers_arr))
print(np.log(numbers_arr))
print(np.exp(numbers_arr))


print(np.max(numbers_arr))
print(np.argmax(numbers_arr))
print(np.min(numbers_arr))
print(np.sum(numbers_arr))
print(np.size(numbers_arr))
print(np.sum(numbers_arr)/ np.size(numbers_arr))
#instead of the above operation
print(np.mean(numbers_arr))

print(np.std(numbers_arr))

print(np.sum(numbers_arr, axis=1))
print(np.sum(numbers_arr, axis=0))
#axis hangi eksende toplama yapacagin =0 -> sutun topla =1 ->satit topla

print(np.zeros((4,4)))
#4e 4luk 0larlla dolu matris
print(np.ones((4,4)))
#0 in 1 li hali

eye = np.eye(3)
eye =eye+3 
#eye degerlerini 3 artirdik
print(eye)

np.diag(eye)

print(eye)

#print(np.random.randint(low value ,high value,(3,3))) integer 0-10 arasi random 3e 3luk matris urettik
print(np.random.randint(0,10,(3,3)))



































