# -*- coding:utf-8 -*-
# 直接插入排序
# n-1趟排序，每次把待排序的数据插入到已排序数组的合适位置

def insertSort(dataset):
	if len(dataset) < 1:
		return dataset
	n = len(dataset)
	for i in range(1, n-1):
		j = i-1
		temp = dataset[i]
		while j >= 0 and dataset[j] > temp:
			dataset[j+1] = dataset[j]
			j -= 1
		dataset[j+1] = temp
	return dataset

#优化：二分查找插入位置
def binaryInsertSort(dataset):
	if len(dataset) < 1:
		return dataset
	n = len(dataset)
	for i in range(1, n-1):
		j = i-1
		temp = dataset[i]
		index = binarySearch(dataset, i, temp)
		if index != -1:
			while j>= index:
				dataset[j+1] = dataset[j]
				j -= 1
			dataset[j+1] = temp
	return dataset

def binarySearch(dataset,key,value):
	left = 0
	right = key-1
	while left <= right:
		mid = left+(right-left)//2
		if dataset[mid] > value:
			right = mid-1
		else:
			left = mid+1
	if left < key:
		return left
	# 插入的数比有序数组都大
	else:
		return -1

if __name__ == '__main__':
	dataset = [6,3,2,7,4,2,5,8]
	print (binaryInsertSort(dataset))

