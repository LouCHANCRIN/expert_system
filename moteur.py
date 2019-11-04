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
	if right == True and left == False: return True
	return False

functions = {'!': ft_not, '+': ft_and, '|': ft_or, '^': ft_xor}

def solve_querie(tree, querie, values, facts):
	check = False
	for q in facts:
		if check == True:
			if facts[q] == None:
				return None
		if q == querie:
			check = True
	if True in values and False not in values and None not in values:
		return True
	if True in values and (False in values or None in values):
		return None
	return False

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

def moteur(querie, facts, dictionnaire):
	facts[querie] = None
	if querie not in dictionnaire:
		return False
	values = []
	for rule in dictionnaire[querie]:
		facts, value = evaluate(rule.left, facts, dictionnaire)
		values.append(value)
	return solve_querie(rule.right, querie, values, facts)

def inference(rules, facts, queries, dictionnaire):
	for querie in queries:
		tmp = copy.copy(facts)
		result = moteur(querie, tmp, dictionnaire)
		if result == None:
			print("Querie '" + querie + "' is Undefined")
		else:
			print("Querie '" + querie + "' is", result)