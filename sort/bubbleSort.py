# -*- coding:utf-8 -*-
# 冒泡算法
# (n-1)趟排序，每次排序通过两两交换把最大值移到最右边（升序）

def bubbleSort(dataset):
	if len(dataset) < 1:
		return dataset
	n = len(dataset)
	for i in range(n-1):
		# 如果j遍历一边没有两两交换顺序，说明已是有序排列
		exchange = True
		for j in range(n-1):
			if dataset[j] > dataset[j+1]:
				dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
				exchange = False
		if exchange:
			break
	return dataset

if __name__ == '__main__':
	dataset = [6,3,2,7,4,2,5,8]
	print (bubbleSort(dataset))
