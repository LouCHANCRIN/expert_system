import copy

def ft_not(left, right):
	if left == True: return False
	return True

def ft_and(left, right):
	if left == True and right == True: return True
	return False

def ft_or(left, right):
	if left == True or right == True: return True
	return False

def ft_xor(left, right):
	if left == True and right == False: return True
	if left == False and right == True: return True
	return False

functions = {'!': ft_not, '+': ft_and, '|': ft_or, '^': ft_xor}

def evaluate(rule, facts, dictionnaire):
	if not rule:
		return facts, None
	if rule.value and rule.value.isalpha():
		if rule.value in facts:
			return facts, facts[rule.value]
		else:
			facts[rule.value] = moteur(rule.value, facts, dictionnaire)
			return facts, facts[rule.value]
	facts, left = evaluate(rule.left, facts, dictionnaire)
	fatcs, right = evaluate(rule.right, facts, dictionnaire)
	return facts, functions[rule.value](left, right)

def solve_querie(tree, querie, values):
	print(values)
	if True in values and False not in values and None not in values:
		return True
	return False

def moteur(querie, facts, dictionnaire):
	facts[querie] = None
	if querie not in dictionnaire:
		print("Insolvable, il n'existe pas de règle pour déterminer la valeur de '" + querie + "'.")
		return False
	values = []
	for rule in dictionnaire[querie]:
		facts, value = evaluate(rule.left, facts, dictionnaire)
		values.append(value)
	print(facts)
	print(values)
	return solve_querie(rule.right, querie, values)

def get_facts(facts, queries):
	facts.remove("=")
	queries.remove("?")
	f = {}
	for fact in facts:
		f[fact] = True
	return f, queries

def inference(rules, facts, queries, dictionnaire):
	facts, queries = get_facts(facts, queries)
	print(queries)
	print(facts)
	for querie in queries:
		tmp = copy.copy(facts)
		result = moteur(querie, tmp, dictionnaire)
		print("Querie '" + querie + "' is", result)