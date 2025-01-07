maximum = 3
v = [1, 2, 3]
w = [4, 5, 6]
total = len(v)

memory = [0]*(maximum+1)

def knapsack(values, weights, max_weight, total_items, last_weight):
	global memory
	
	# base_case: no items to use or max_weight is 0,
	if total_items == 0 or max_weight == 0:
		return 0

	# for current item, need to check if have max_weight to use this item
	current_item_index = total_items - 1
	
	if weights[current_item_index] > max_weight:
		return knapsack (values, weights, max_weight, total_items - 1, last_weight)
	
	if memory[max_weight] > last_weight:
		return memory[current_item_index]
		
	'''
	1. use the current item
		- gain the value
		- lose the max_weight, determine the subproblem by reducing the max_weight
	2. not use the current item
		- don't gain the value
		- determine the same subproblem with the same max_weight
	'''
	with_item = values[current_item_index] + knapsack(values, weights, max_weight - weights[current_item_index], total_items - 1, last_weight+values[current_item_index])
	without_item = knapsack(values, weights, max_weight, total_items - 1, last_weight)

	return max(with_item, without_item)

print(knapsack(v, w, maximum, total, 0))
