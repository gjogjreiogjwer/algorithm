# -*- coding:utf-8 -*-
# 堆排序
# 每趟排序选出最大值，放在数组末尾
# 最后一个非叶子结点 n/2

def heapSort(dataset):
	if len(dataset) <= 1:
		return dataset
	n = len(dataset)
	# 创造初始堆
	for i in range(n//2-1, -1, -1):
		shift(dataset, i, n-1)
	for i in range(n-1, -1, -1):
		dataset[i], dataset[0] = dataset[0], dataset[i]
		shift(dataset, 0, i-1)

def shift(dataset, lo, hi):
	i = lo
	j = 2*i+1
	temp = dataset[i]
	while j <= hi:
		if j < hi and dataset[j+1] > dataset[j]:
			j += 1
		if temp < dataset[j]:
			dataset[i] = dataset[j]
			i = j
			j = 2*i+1
		else:
			break
	dataset[i]=temp

if __name__ == '__main__':
	dataset = [6,3,2,7,4,2,5,8]
	heapSort(dataset)
	print (dataset)