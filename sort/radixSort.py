# -*- coding:utf-8 -*-
# 基数排序
# 对个位、十位、百位...依次排序

def radixSort(dataset):
	maxValue = max(dataset)
	n = 1
	# 找到最大位数
	while maxValue > 10**n:
		n += 1
	i = 0
	while i < n:
		count = {}
		for k in range(10):
			count[k] = count.get(k, [])
		for d in dataset:
			index = (d//10**i)%10
			count[index].append(d)
		j = 0
		for k in range(10):
			if count[k]:
				for m in count[k]:
					dataset[j] = m
					j += 1
		i += 1
	return dataset

if __name__ == '__main__':
	dataset = [123, 5, 475, 543, 24, 1111, 4793]
	print (radixSort(dataset))