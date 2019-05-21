# -*- coding:utf-8 -*-
# 选择排序
# 每趟排序选择最小插入到已排序数组后面

def selectSort(dataset):
	if len(dataset) <= 1:
		return dataset
	n = len(dataset)
	for i in range(n-1):
		min = i
		for j in range(i+1, n):
			if dataset[j] < dataset[min]:
				min = j
		dataset[i], dataset[min] = dataset[min], dataset[i]
	return dataset

if __name__ == '__main__':
	dataset = [6,3,2,7,4,2,5,8]
	print (selectSort(dataset))