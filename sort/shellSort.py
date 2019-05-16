# -*- coding:utf-8 -*-
# 希尔排序
# 以n/2为步长，一直取半直到gap为1

def shellSort(dataset):
	if len(dataset)<=1:
		return dataset
	n=len(dataset)
	gap=n/2
	while gap>0:
		for i in range(gap, n):
			temp=dataset[i]
			j=i-gap
			while j>=0 and dataset[j]>temp:
				dataset[j+gap]=dataset[j]
				j-=gap
			dataset[j+gap]=temp
		gap/=2
	return dataset

if __name__ == '__main__':
	dataset=[6,3,2,7,4,2,5,8]
	print shellSort(dataset)
