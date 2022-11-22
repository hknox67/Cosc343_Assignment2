__author__ = "<hayden knox>"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "<knoha805@student.otago.ac.nz>"

import random

import numpy as np

agentName = "my_agent"
perceptFieldOfVision = 5  # Choose either 3,5,7 or 9
perceptFrames = 1  # Choose either 1,2,3 or 4
trainingSchedule = [("random", 10), ("self", 20), ("random", 20)]


# This is the class for your snake/agent
class Snake:

    def __init__(self, nPercepts, actions):

        self.nPercepts = nPercepts
        self.actions = actions
        self.previous_action = 0
        self.rotation_count = 0
        # This statement populates the array with a range of randomised chromosome values to be
        # manipulated once the executions of the AgentFunction and newGeneration methods begin
        # their order of operations.
        self.chromosome = np.random.uniform(-1, 1, (self.nPercepts * 3))

    """
    range_finder function: This function is used by many other methods in this python script to return array data
    structures as iterable collections to be manipulated or accessed for the newGeneration function or the AgentFunction

    @param arrayInput: This is a variable specifying an input collection data structure.
    @return: This method returns an iterable data structure to be manipulated or examined by a method. 
    """

    def range_finder(self, arrayInput):
        return range(len(arrayInput))

    """
    AgentFunction function: This method is used to determine what actions each snake python instance object is to take
    given the randomised input of it chromosomes and percepts input variables. 

    @param percepts: This is the values which are apparant to the snake class instance via its class variable 
    perceptFieldOfVision. These are values to be modified by weight to gravitate the snake towards preferred behaviours.
    #return: a number which indicates to the snakes.py game engine which direction a snake is to move in the game grid
    """

    def AgentFunction(self, percepts):
        move = 0
        array_conversion = np.array(percepts).flatten()
        chromo_parition = np.array_split(self.chromosome, 3)
        for val in range(len(array_conversion)):
            if array_conversion[val] == 2.0:
                array_conversion[val] += 2.0
            if array_conversion[val] == 1.0:
                array_conversion[val] -= 1.0
            if array_conversion[val] == -1.0:
                array_conversion[val] -= 1.0


        action_v1_summary = 0.0
        action_v2_summary = 0.0
        action_v3_summary = 0.0
        DNA_action_v2 = np.array(chromo_parition[1])
        DNA_action_v1 = np.array(chromo_parition[0])
        DNA_action_v3 = np.array(chromo_parition[2])

        for val in range(self.nPercepts):
            action_v1_summary = array_conversion * DNA_action_v1
            action_v2_summary = array_conversion * DNA_action_v2
            action_v3_summary = array_conversion * DNA_action_v3
        action_1 = np.random.randint(-1.0, 1.0)
        action_2 = np.random.randint(-1.0, 1.0)
        action_3 = np.random.randint(-1.0, 1.0)
        action_1 += sum(action_v1_summary)
        action_2 += sum(action_v2_summary)
        action_3 += sum(action_v3_summary)

        # The values evaluated within this if else statement will elect to return a move which the snake will take
        # within the game grid: -1 is move left, 1 is move right, 0 is move straight ahead.
        if action_1 > (action_2 and action_3):
            move = -1
        if action_2 > (action_1 and action_3):
            move = 0
        if action_3 > (action_1 and action_2):
            move = 1

        return move

    """
    evalFitness function: This function iterates through the collection of the snake instance objects for the population
    is renewed by the newGeneration function. These fitness scores determine the players game scores and is used to 
    include the principal of elitism in the newGeneration function. 

    @param Population: This is the collection is snake class instances from the previous generation and game competition
    @return: This method return a numpy array of fitness scores corresponding to each individual snake python class 
    instance
    """


def evalFitness(population):
    N = len(population)

    fitness = np.zeros((N))
    for n, snake in enumerate(population):
        maxSize = np.max(snake.sizes)
        turnsAlive = np.sum(snake.sizes > 0)
        maxTurns = len(snake.sizes)

        # This is the formula used to determine the fitness of each snake instance
        fitness[n] = maxSize + turnsAlive / maxTurns

    return fitness


"""
newGeneration function: This function is responsible for implementing the principals of elitism within creating the new
generation of snake instances. Selecting parents from the population using roulette wheel selection base on the relative
normalised fitness values of each snake and performing this dynamically. Lastly after all the other aforementioned 
processes are complete. The mutation of snake chromosomes for the genetic algorithm are performed after the creation of 
child snakes. 

@param This is the collection of snake instances from the previous generation to be used to create new child 
snake instances

@return a new generation of snakes who's chromosomes are inherited and modified from the old generation of snakes.
"""


def newGeneration(old_population):
    N = len(old_population)
    nPercepts = old_population[0].nPercepts
    actions = old_population[0].actions
    fitness = evalFitness(old_population)

    # This block of code appends a varying number of elitism snakes to a list so that they may be added into the new
    # generation of competing snakes and be selected as potential snake parent instances.
    fitness_sum = np.sum(fitness)
    eleit_fitness_array_length = (round(fitness_sum / len(fitness))) // 2
    eliet_fitness_snakes = []
    max_fitness_values = np.empty(eleit_fitness_array_length)
    manipulate_fitness = np.copy(fitness)
    for entry in range(len(max_fitness_values)):
        max_fitness_value = np.max(manipulate_fitness)
        max_fitness_index = np.argmax(manipulate_fitness)
        eliet_fitness_snakes.append(old_population[max_fitness_index])
        manipulate_fitness = np.delete(manipulate_fitness, max_fitness_index)
        np.put(max_fitness_values, entry, max_fitness_value)

    # This for loop takes the individual snake fitness scores and produces them as a fraction to be normalised later
    # into a value ranging from 0 to 1.
    relative_fitness = []
    for fit in fitness:
        relative_fit = fit / fitness_sum
        relative_fitness.append(relative_fit)

    probability_ranges = []
    for i in range(len(relative_fitness)):
        probability_ranges.append(sum(relative_fitness[:i + 1]))

    # these two statements are used to randomly select from the old population an indexed snake instance which will be
    # selected in conjunction to its normalised probability.
    snake_selected_relativity1 = np.random.uniform(0, 1)
    snake_selected_relativity2 = np.random.uniform(0, 1)
    parent1 = []
    parent2 = []

    for prob in probability_ranges:
        if snake_selected_relativity1 < prob:
            parent1 = old_population[probability_ranges.index(prob)]
            break
    for prob in probability_ranges:
        if snake_selected_relativity2 < prob:
            parent2 = old_population[probability_ranges.index(prob)]
            break

    new_population = list()

    for n in range(N - eleit_fitness_array_length):
        new_snake = Snake(nPercepts, actions)

        mutate_probability = 0.05
        P1_snake_DNA = np.array(parent1.chromosome)

        P2_snake_DNA = np.array(parent2.chromosome)

        p1_marker1_end = int((len(P1_snake_DNA) / 2))
        parent1_chromosome_marker = random.randint(0, p1_marker1_end)
        parent2_chromosome_marker = random.randint(p1_marker1_end + 1, len(P1_snake_DNA))
        offspring = np.zeros(len(P2_snake_DNA))
        for chromo in range(len(P1_snake_DNA)):
            if chromo >= parent1_chromosome_marker and chromo <= parent2_chromosome_marker:
                offspring[chromo] = P2_snake_DNA[chromo]
            else:
                offspring[chromo] = P1_snake_DNA[chromo]

        # This part of the code is responsible for mutating individual new generation snake chromosomes. This is
        # done by iterating over the volume of each snakes chromosomes
        for chromo in range(len(offspring)):
            mutation_action = np.random.rand()
            if mutation_action < mutate_probability:
                offspring[chromo] = np.random.uniform(-1, 1)
        new_snake.chromosome = offspring
        new_population.append(new_snake)

    # Here is where the elitism snakes are appended to the new generation of child snakes.
    for snake in eliet_fitness_snakes:
        new_population.append(snake)
    avg_fitness = np.mean(fitness)

    return new_population, avg_fitness


