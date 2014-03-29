import random

class Robot:
	"""Individual used to solve genetic algorithm problems"""

	def __init__(self, dna, random_constant, bound, fitness_func):
		#initial dna
		self.dna = dna
		#assumed a value between 0 & 1
		self.r_constant = random_constant
		#assumed a tuple
		self.bound = bound 
		#the fitness function to evaluate the robot by
		self.fitness_func = fitness_func

		#evaluate fitness
		self.fitness = 0
		self.evaluate()

	def evaluate(self):
		self.fitness = self.fitness_func(self.dna)
		
	def breed(self, robot):
		sub = self.random_ind()
		return self.dna[:sub] + robot.dna[sub:]
		"""
		for i in range(len(self.dna)):
			rand_double = random.random()
			if(rand_double > .5):
				self.dna[i] = robot.dna[i]
			elif(rand_double < self.r_constant):
				self.dna[i] = self.random_value()"""

	def mutate(self):
		self.dna[self.random_ind()] = self.random_value()

	def random_value(self):
		return random.randrange(self.bound[0], self.bound[1])

	def random_ind(self):
		return random.randrange(0, len(self.dna))

	def __lt__(self, x):
		if(self.fitness < x.fitness):
			return True
		return False

	def __str__(self):
		return "DNA: " + str(self.dna)

	def __repr__(self):
		return "FIT: " + str(self.fitness)

##Large picture GA stuff##
def myfitness(dna):
	numb = 1
	for n in dna:
		numb *= n

	return abs(numb - 150)

def createRandomDna(size, bound):
	l = []
	for i in range(size):
		l.append(random.randrange(bound[0], bound[1]))

	return l

def runGA():
	pop_size = 250
	bound = (1, 20)
	mutation_c = .06
	list_size = 6

	population = []
	for i in range(pop_size):
		population.append(Robot(createRandomDna(list_size, bound), mutation_c, bound, myfitness))

	epoch = 0
	answered = False
	while (not answered):
		new_pop = []
		for i in range(pop_size):
			x = random_selection(population)
			y = random_selection(population)
			new_dna = x.breed(y)
			new_pop.append(Robot(new_dna, mutation_c, bound, myfitness))

		population = new_pop
		sorted_pop = sorted(population)
		if(epoch % 50 == 0):
			print sorted_pop[:5]
			for robo in sorted_pop[:3]:
				print "+", robo

		for robo in population:
			robo.evaluate()
			if robo.fitness == 0:
				answered = True
				print "ANSWER FOUND:", robo

		epoch += 1


def random_selection(population):
	sorted_pop = sorted(population)
	rand_double = random.random()

	if(rand_double < .80):
		return sorted_pop[random.randrange(0, len(sorted_pop)/2)]

	return sorted_pop[random.randrange(0, len(sorted_pop))]


if __name__ == '__main__':
	runGA()