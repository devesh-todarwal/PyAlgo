import math

get_bit = lambda num, bit: int(num/pow(10,bit-1))%10

def countingSort(arr, bit):

	out = [0]*len(arr) # output array
	ind = [0]*10 # count of digits

	for i in range(len(arr)): # store count of each digit
		ind[get_bit(arr[i], bit)] += 1

	for i in range(1,10): # add up counts (cumulative count)
		ind[i] += ind[i-1]

	for i in reversed(range(len(arr))): # fill the output array
		out[ ind[get_bit(arr[i], bit)] - 1] = arr[i]
		ind[get_bit(arr[i], bit)] -= 1

	return out

def radixSort(arr):
	for i in range(1,2+int(math.log10(max(arr)))):
		arr[:] = countingSort(arr,i)
		
nlist = [14,46,43,27,57,41,45,21,70]
radixSort(nlist)
print(nlist)
