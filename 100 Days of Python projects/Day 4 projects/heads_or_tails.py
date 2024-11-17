import random
#always use the import random librry

#The mistake I made was that I didn't assign integers abd then used cmbination of if/else: statenebts
random_side = random.randint(0, 1)
if random_side == 1:
  print('Heads')
else:
  print('Tails')