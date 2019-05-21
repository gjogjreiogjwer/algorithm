# -*- coding:utf-8 -*-
# 归并排序
# 分治法，分而治之

def mergeSort(dataset):
	if len(dataset) <= 1:
		return dataset
	mid = len(dataset)//2
	left = mergeSort(dataset[:mid])
	right = mergeSort(dataset[mid:])
	return merge(left, right)

def merge(left, right):
	res = []
	i = 0
	j = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			res.append(left[i])
			i += 1
		else:
			res.append(right[j])
			j += 1
	if i == len(left):
		res.extend(right[j:])
	else:
		res.extend(left[i:])
	return res

if __name__ == '__main__':
	dataset = [6,3,2,7,4,2,5,8]
	print (mergeSort(dataset))