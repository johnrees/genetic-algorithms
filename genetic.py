import random

def _mutate(parent, geneSet):
  index = random.randrange(0, len(parent))
  childGenes = list(parent)
  newGene, alternate = random.sample(geneSet, 2)
  childGenes[index] = alternate \
    if newGene == childGenes[index] \
    else newGene
  return ''.join(childGenes)

def _generate_parent(length, geneSet):
  genes = []
  while len(genes) < length:
    sampleSize = min(length - len(genes), len(geneSet))
    genes.extend(random.sample(geneSet, sampleSize))
  return ''.join(genes)

def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
  random.seed()
  # generate guess
  bestParent = _generate_parent(targetLen, geneSet)
  bestFitness = get_fitness(bestParent)
  display(bestParent)
  if bestFitness >= optimalFitness:
    return bestParent

  while True:
    child = _mutate(bestParent, geneSet)
    # request fitness
    childFitness = get_fitness(child)
    # compare fitness with previous best guess
    if bestFitness >= childFitness:
      # keep guess with better fitness
      continue
    display(child)
    if childFitness >= optimalFitness:
      return child
    bestFitness = childFitness
    bestParent = child
