
'''

TINY_GSHCGP.py: An Implementation of Geometric Semantic ***Hill Climber*** Genetic Programming Using Higher-Order Functions and Memoization

Author: Alberto Moraglio (albmor@gmail.com)

Features:

- Same as TINY_GSGP.py, substituting the evolutionary algorithm with a hill-climber.

- The fitness landscape seen by Geometric Semantic operators is always unimodal. A hill climber can reach the optimum.

- Offspring functions call parent functions rather than embed their definitions (no grwoth, implicit ancestry trace).

- Even if offspring functions embedded parent function definition, the growth is linear in the number of generation (not exponential as with crossover). 

- Memoization of individuals turns time complexity of fitness evalutation from linear to constant (not exponential to constant as with crossover).

- Implicit ancestry trace and memoization not strictly necessary with hill-climber for efficent implementation.

- The final solution is a compiled function. It can be extracted using the ancestry trace to reconstruct its 'source code'. 

This implementation is to evolve Boolean expressions. It can be easily adapted to evolve arithmetic expressions or classifiers.

'''

import random
import itertools

#### PARAMETERS ####

NUMVARS = 5 # number of input variables
DEPTH = 4 # maximum depth of expressions in the initial population
GENERATIONS = 400 # number of generations

####################

vars = ['x'+str(i) for i in range(NUMVARS)] # variable names

def memoize(f):
    'Add a cache memory to the input function.'
    f.cache = {}
    def decorated_function(*args):
        if args in f.cache:
            return f.cache[args]
        else:
            f.cache[args] = f(*args)
            return f.cache[args]
    return decorated_function

def randexpr(dep):
    'Create a random Boolean expression.'
    if dep==1 or random.random()<1.0/(2**dep-1):
        return random.choice(vars)
    if random.random()<1.0/3:
        return 'not' + ' ' + randexpr(dep-1) 
    else:
        return '(' + randexpr(dep-1) + ' ' + random.choice(['and','or']) + ' ' + randexpr(dep-1) + ')'

def randfunct():
    'Create a random Boolean function. Individuals are represented _directly_ as Python functions.'
    re = randexpr(DEPTH)
    rf = eval('lambda ' + ', '.join(vars) + ': ' + re) # create function of n input variables
    rf = memoize(rf) # add cache to the function
    rf.geno = lambda: re # store genotype
    return rf

def targetfunct(*args):
    'Parity function of any number of input variables'
    return args.count(True) % 2 == 1

def fitness(individual):
    'Determine the fitness (error) of an individual. Lower is better.'
    fit = 0
    somelists = [[True,False] for i in range(NUMVARS)]
    for element in itertools.product(*somelists): # generate all input combinations for n variables
        if individual(*element) != targetfunct(*element):
            fit = fit + 1
    return fit

def mutation(p):
    'The mutation operator is a higher order function. The parent function is called by the offspring function.'
    mintermexpr = ' and '.join([random.choice([x,'not ' + x]) for x in vars]) # random minterm expression of n variables
    minterm = eval('lambda ' + ', '.join(vars) + ': ' + mintermexpr) # turn minterm into a function
    if random.random()<0.5:
        offspring = lambda *x: p(*x) or minterm(*x)
        offspring = memoize(offspring) # add cache
        offspring.geno = lambda: '(' + p.geno() + ' or ' + mintermexpr + ')' # to reconstruct genotype
    else:
        offspring = lambda *x: p(*x) and not minterm(*x)
        offspring = memoize(offspring) # add cache
        offspring.geno = lambda: '(' + p.geno() + ' and not ' + mintermexpr + ')' # to reconstruct genotype
    return offspring
    
def climb():
    'Main function. As the landscape is always unimodal the climber can find the optimum.'
    curr = randfunct() # initial individual
    curr.fit = fitness(curr) # evaluate fitness

    for gen in xrange(GENERATIONS+1):
        off = mutation(curr) # create offspring
        off.fit = fitness(off) # fitness offspring
        if off.fit < curr.fit: curr = off # offspring replaces parent if better
        if gen % 10 == 0: print 'gen: ', gen , ' fit: ', curr.fit # print stats

    print 'Best individual: '
    print curr.geno() # reconstruct genotype of final solution (LINEAR SIZE IN NUMBER OF GENERATIONS)
    print 'Query best individual with all True inputs:'
    print curr(*([True] * NUMVARS)) # query final solution

climb()
