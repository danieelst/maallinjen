# Parse scoreline string, e.g. '3-1' -> (3,1)
def goals(result):
  return *(int(goals) for goals in result.split('-')),

# Compute points gained for a guessed scoreline
#  * 1 point for right outcome
#  * 3 additional points for correct result
def points(guessed, result):
  p = 0
  g1,g2 = goals(guessed)
  r1,r2 = goals(result)
  p += 3 * (g1 == r1 and g2 == r2)
  p += (g1 > g2 and r1 > r2) or (g1 == g2 and r1 == r2) or (g1 < g2 and r1 < r2)
  return p

# Number of goals the guessed scoreline differed with
def difference(guessed, result):
  g1,g2 = goals(guessed)
  r1,r2 = goals(result)
  return abs(g1 - r1) + abs(g2 - r2)

# Simple probability distribution
def distribution(guessed, result):
  return 1 / (1 + abs(result - guessed))

# Compute accuracy of a scoreline in accordance with the distribution
def accuracy(guessed, result):
  g1,g2 = goals(guessed)
  r1,r2 = goals(result)
  return distribution(g1,r1) * distribution(g2,r2)

# Check if the result would have been correct, if the result differed with n goals
def n_diff(n, guessed, result):
  return difference(guessed, result) <= n
