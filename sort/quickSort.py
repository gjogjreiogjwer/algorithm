# -*- coding:utf-8 -*-
# 快速排序
# 每次排序把数据分隔成小于待比较的数和大于两部分

def quickSort(dataset, lo, hi):
	if lo<hi:
		# 确定position在排序数组中的位置
		position=partition(dataset, lo, hi)
		quickSort(dataset, lo, position-1)
		quickSort(dataset, position+1, hi)

def partition(dataset, lo, hi):
	p=dataset[lo]
	i=lo
	j=hi
	while i<j:
		while i<hi and dataset[i]<=p:
			i+=1
		while j>lo and dataset[j]>p:
			j-=1
		if i<j:
			dataset[i], dataset[j]=dataset[j], dataset[i]
	dataset[lo], dataset[j]=dataset[j], dataset[lo]
	return j

if __name__ == '__main__':
	dataset=[6,3,2,7,4,2,5,8]
	quickSort(dataset, 0, 7)
	print dataset