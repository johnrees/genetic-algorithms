import random
import datetime

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello World!"

def generate_parent(length):
  genes = []
  while len(genes) < length:
    sampleSize = min(length - len(genes), len(geneSet))
    genes.extend(random.sample(geneSet, sampleSize))
  return ''.join(genes)

def get_fitness(guess):
  return sum(1 for expected, actual in zip(target, guess) if expected == actual)

def mutate(parent):
  index = random.randrange(0, len(parent))
  childGenes = list(parent)
  newGene, alternate = random.sample(geneSet, 2)
  childGenes[index] = alternate \
    if newGene == childGenes[index] \
    else newGene
  return ''.join(childGenes)

def display(guess):
  timeDiff = datetime.datetime.now() - startTime
  fitness = get_fitness(guess)
  print("{}\t{}\t{}".format(guess, fitness, timeDiff))

random.seed(1)
startTime = datetime.datetime.now()
# generate guess
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)

while True:
  child = mutate(bestParent)
  # request fitness
  childFitness = get_fitness(child)
  # compare fitness with previous best guess
  if bestFitness >= childFitness:
    # keep guess with better fitness
    continue
  display(child)
  if childFitness >= len(bestParent):
    break
  bestFitness = childFitness
  bestParent = child
