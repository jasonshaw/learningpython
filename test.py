import timeit
# import random
# alist = random.sample(range(1,101),20) #random.sample()生成不相同的随机数
# print(alist)

# 常用排序算法练习
# 所有排序算法都仅考虑升序排列，降序仅需要反一下即可

# 选择排序算法：
# 一句话：从前往后，每个位置选出从此至结尾中最小的
# 默认升序排列一个列表，否则降序
# 思想在于从头开始，两两对比，通过小的占据当前位置，每次选出当前位置最小(升序）或者最大（降序）的值占位，后移一位，直至循环结尾完成排序
# 属于“从前往后”的排序，平均时间复杂度O(n²)

def selection_sort(alist, odrer="asc"):
	alist = list(alist)  # 将元组转化为一个新的list，避免后续多次排序影响源列表
	start = timeit.default_timer()
	# print(alist)
	times = 0
	alen = len(alist)
	for i in range(0,alen):
		for j in range(i+1,alen):
			temp = alist[i]
			if alist[j] < alist[i]:
				alist[i] = alist[j]
				alist[j] = temp
			times+=1
	print("Time used:",(timeit.default_timer() - start)*1000,"ms")
	print("选择排序迭代次数：",times)
	print(alist)


# 冒泡算法：
# 一句话：从后往前，每个位置选出从此至开头最大的
# 默认升序排列一个列表，否则降序
# 思想在于从首位开始，两两比较，将大的后移，将从首位到该轮末尾最大的移至末尾，下一轮末尾位置前移一位，逐轮循环，直至本轮末尾到达首位停止，完成排序
# 属于“从后往前”的排序，平均时间复杂度O(n²)

def bubble_sort(alist, odrer="asc"):
	start=timeit.default_timer()
	alist = list(alist) #将元组转化为一个新的list，避免后续多次排序影响源列表
	#print(alist)
	times = 0
	alen = len(alist)
	for i in range(0,alen-1):
		for j in range(0,alen-i-1):
			temp = alist[j]
			if alist[j] > alist[j+1]:
				alist[j] = alist[j+1]
				alist[j+1] = temp
			times+=1
	print("Time used:",(timeit.default_timer() - start)*1000,"ms")
	print("冒泡排序迭代次数：",times)
	print(alist)

# 插入排序算法：
# 一句话：从前往后，逐一向已排序好的序列中插入紧后元素（或者说：前两个元素先排序好，之后从第三个开始选择插入位置，依此后退，直至结尾）
# 默认升序排列一个列表，否则降序
# 思想在于从第二个元素（游标位置为1）开始，将当前元素逐步前移直至遇到更小的停止一轮插入，游标后移一位，重复下一轮，直至末尾元素完成插入，则排序完成
# 属于“从前往后”的排序，平均时间复杂度O(n²)，一般地要快过冒泡排序

def insertion_sort(alist, odrer="asc"):
	start=timeit.default_timer()
	alist = list(alist) #将元组转化为一个新的list，避免后续多次排序影响源列表
	#print(alist)
	times = 0
	alen = len(alist)
	for i in range(0,alen):
		position = i
		current_value = alist[position]
		while position > 0 and alist[position-1] > current_value:
			alist[position] = alist[position-1]
			alist[position-1] = current_value
			position-=1
			times+=1
	print("Time used:",(timeit.default_timer() - start)*1000,"ms")
	print("插入排序迭代次数：",times)
	print(alist)


# 希尔排序算法：直接插入排序算法的步长改进算法，又称缩小增量排序、递减增量排序。
# 默认升序排列一个列表，否则降序
# 思想在于，直接插入排序每次只能将数据移动一位，而步长从1改为gap(就是跳过等距的数)提高移动速度，
# 	相当于直接插入算法，步长从1改为gap，再加入限制条件gap > 0即可（巧记），
# 	步长使用的是Donald Shell的建议，每次缩为上次分组量的一半，将整租按插入排序实现插入，直至分组量为1
# 	**另外步长还可以使用Sedgewick提出的(1, 5, 19, 41, 109,…)
# 	**也可以使用斐波那契数列除去0和1将剩余的数以黄金分区比的两倍的幂进行运算得到的数列。
# 属于“从前往后”的排序，平均时间复杂度O(nlog2n)「n倍的log以2为底n」，一般地要快过直接插入排序

def shell_sort(alist, odrer="asc"):
	start=timeit.default_timer()
	alist = list(alist) #将元组转化为一个新的list，避免后续多次排序影响源列表
	# print(alist)
	times = 0
	alen = len(alist)
	# 初始步长
	gap = alen // 2
	while gap > 0:
		for i in range(gap,alen):
			 # 每个步长进行插入排序
			position = i
			current_value = alist[position]
			while position >= gap and alist[position-gap] > current_value:
				alist[position] = alist[position-gap]
				alist[position-gap] = current_value
				position-=gap
				times+=1
		gap = gap // 2
	print("Time used:",(timeit.default_timer() - start)*1000,"ms")
	print("希尔排序迭代次数：",times)
	print(alist)

# 快速排序算法：对冒泡排序的一种有效改进，但思想已经有了巨大的变化,戏称：挖坑填数+分治法。
# 默认升序排列一个列表，否则降序
# 思想在于，任选一个元素作为“基准”（pivot），通过交换，将大于它的放右边，小于它放左边，进而确定了这个值的位置，
# 	进而再次依赖该方法分别再次递归左侧和右侧，直至只有单侧只有一个位置，停止迭代
# 	具体的说：任选（选定首位）为基准，末尾序号倒退（递减），直至遇到一个小于等于基准的则将基准位填入该值，而后首位序号前进（递增），
# 		直到遇到一个大于基准的，则将倒退停下的位置填入该值，继续轮动，直至后退与前进相遇（序号相同），则将基准填入该位置，一次“分治”完成。
# 	每当后退位置元素小于基准，且前进位置元素大于基准，则交换（放入正确的位置），直至两者相遇，则一轮“分边”完成
# 	**也可以用迭代的方法，而非递归
# 属于“从前往后”的排序，平均时间复杂度O(nlog2n)「n倍的log以2为底n」，一般地要快过直接插入排序

def quick_sort(alist,lb = None,ub = None):  
# lb为列表alist中快排起点下标（lower bound），ub为列表alist快排终点下标（upper bound），默认空，则需快排列表全部
# 第一个参数为列表，则为引用传值，每次迭代都将影响源列表的值，故此并不需要提前返回值，如果为元组，则为值传递
	# start=timeit.default_timer()
	if not isinstance(alist,list) :
		return "第一参数不是list"
	alen = len(alist)
	if alen <=1:
		return alist
	if lb is None or ub is None :
		lb = 0
		ub = alen - 1
	elif lb < 0 or ub > alen -1 or lb > ub :
		return "Error：快排起止点越界或者顺序不合理！" 
	forwords = lb
	backwords = ub
	# alist = list(alist) #将元组转化为一个新的list，避免后续多次排序影响源列表
	# print(alist[lb:ub+1]) # 列表截取是前闭后开区间，为了保证最后一个下标不遗漏，所以要+1
	# 初始基准
	pivot = alist[lb]
	# 开始计数
	times = 0
	while forwords < backwords :
		# while alist[forwords] <= pivot:
		while alist[backwords] >= pivot and forwords < backwords : # 保障停止后退仅因为出现小于基准
			backwords -= 1
		if alist[backwords] < pivot and forwords < backwords : # 保障后退位值填入前进位坑，仅是因为找到一个小于基准的元素
			alist[forwords] = alist[backwords]
			forwords += 1
			times += 1
		while alist[forwords] <= pivot and forwords < backwords : # 保障停止后退仅因为出现小于基准
			forwords += 1
		if alist[forwords] > pivot and forwords < backwords : # 保障后退位值填入前进位坑，仅是因为找到一个小于基准的元素
			alist[backwords] = alist[forwords]
			backwords -= 1
			times += 1
	alist[forwords] = pivot
	quick_sort(alist,lb,forwords-1)
	quick_sort(alist,forwords+1,ub)
	return alist
	# print("Time used:",(timeit.default_timer() - start)*1000,"ms")
	# print("希尔排序迭代次数：",times)
	# print(alist)



# 函数传递参数为可变对象（列表、字典）时，结果是引用传递，而非普通变量的值传递
# l1=(8,13,2,1,9,7,4,6)
l1=(82, 11, 99, 8, 59, 83, 48, 12, 39, 63, 44, 73, 41, 86, 79, 35, 13, 98, 10, 42)
# selection_sort(l1)
# bubble_sort(l1)
# insertion_sort(l1)
shell_sort(l1)
# l3=[82, 11, 99, 8, 59, 83, 48, 12, 39, 63, 44, 73, 41, 86, 79, 35, 13, 98, 10, 42]
# start=timeit.default_timer()
# print(quick_sort(l3))
# print("Time used:",(timeit.default_timer() - start)*1000,"ms")
# # a = b = 1
# # print(a,b)
# aaa = [3*x for x in l1]
# print(aaa)

# 阶乘
def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)
# print(fact(120))