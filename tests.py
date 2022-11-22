import random

import numpy as np
import statistics

# generation 0
old_population = 10
perceptFieldOfVision = 3

chromosome = np.random.uniform(-1, 1, size = (perceptFieldOfVision * perceptFieldOfVision * 3))
# chromosome = np.random.random((perceptFieldOfVision, perceptFieldOfVision * 3))
#chromosome = chromosome.round(decimals=4, out=None)
percepts = np.random.randint(-1, 3, size=(perceptFieldOfVision, perceptFieldOfVision))
#matrix_combination = chromosome * percepts
#summary = np.sum(matrix_combination)
dimensions = np.shape(chromosome)
percepts_sum = np.sum(percepts)
matrix = []
# for i in range(len(chromosome)):
#    sum = 0
#    for j in range():
#        sum = sum + matrix[i][j]
#    print('====================== Matrix Row Sums ======================')
#    print('Sum of row',i+1,':',sum)

print('====================== chromsomes ======================')
print(chromosome)
print('')
print('====================== percepts ======================')
print(percepts)
print('')
print('====================== Chromosome Shape ===================')
print(dimensions)
print('====================== Sub Arrays ===========================')
print(np.split(chromosome, perceptFieldOfVision))
print('')
print('====================== Sub Array Row Summary ======================')
arr = np.array(np.split(chromosome, perceptFieldOfVision))
print(arr)
print('====================== Percetps Sum ========================')
print(percepts_sum)
print('')
print('====================== Matrix Per and chromo multiply ========================')
print(percepts_sum)
print('')

arr1 = [[2,4,1], [3,2,1], [2,3,1]]
arr2 = [[1,2,3], [3,2,1], [2,3,1]]

combo = np.multiply(arr1, arr2)
print(combo)


threshold_list = []

for i in range(perceptFieldOfVision * 20):
    counter = 0
    if(counter == 5):
        print("")
    chromosome = np.random.uniform(-1, 1, size=(perceptFieldOfVision, perceptFieldOfVision))
    chromosome = chromosome.round(decimals=4, out=None)
    percepts = np.random.randint(-1, 3, size=(perceptFieldOfVision, perceptFieldOfVision))
    matrix_combination = chromosome * percepts
    summary = np.sum(matrix_combination)
    threshold_list.append(summary)
    counter += 1

# threshold_list = [2.0843, 1.18509, 0.22109, 5.9866, 4.031, 1.2999, 1.7171, 1.6624, 3.109700, 0.2765, 1.18234, 0.77175, 1.1612, 0.927]
#threshold_list.sort()

print('====================== Threshold Calculation ========================')
print(threshold_list)
print('highest value in the threshold_list = ', max(threshold_list))
print('lowest value in the threshold_list = ', min(threshold_list))
print('Sum of the list = ', sum(threshold_list))
print('Length of the threshold list = ', len(threshold_list))
print('Average value in the threshold list = ', sum(threshold_list) / len(threshold_list))

# The threshold value should be something between 0 and the sum pf the percepts value?
rounded_list = [round(num, 0) for num in threshold_list]
print(rounded_list)
absolute_list  = [ -abs(x) for x in rounded_list]
print(absolute_list)
# because the mode ranges from 0-3 most often consider changing the threshold value to something closer to this
print('ArrayList mode =', statistics.mode(absolute_list))
print('threshold value =', random.triangular(0, (perceptFieldOfVision + (perceptFieldOfVision * np.random.uniform(0,2))), np.random.randint(0,3))) # was 0 ,2)
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')






# test sorting fitness Sam's code

fitness = [100, 200, 202, 102, 301, 345, 210, 250, 110, 134]
print('====================== Fitness Values ========================')
print(fitness)
# old ordering of code
#order = sorted(range(len(fitness)), key = lambda i: fitness[i])
print('====================== My Fitness Order ========================')
fitness = np.flip(np.sort(fitness))
print(fitness)
sorted_indexes = []
print('====================== My Fitness Order Indexes ========================')
for val in range(len(fitness)):
    sorted_indexes.append(val)
print(sorted_indexes)
print('====================== Source Fitness Values ========================')
fitness = [100, 200, 202, 102, 301, 345, 210, 250, 110, 134]
order = sorted(range(len(fitness)), key=lambda i: fitness[i])
print(fitness)
print(order)
# new_sorted = [old_population[i] for i in order]
#print(fitness)
#print(new_sorted)
#print(np.matrix(fitness))

#this works # maybe remove one percept field of vision value

# bias value
test_decimal = np.random.uniform(0, 1)
print(test_decimal)