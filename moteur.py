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

# def solve_querie(tree, querie, values, facts):
# 	check = False
# 	print(querie)
# 	print(values)
# 	print(facts)
# 	print("")
# 	for q in facts:
# 		if check == True:
# 			if facts[q] == None:
# 				return None
# 		if q == querie:
# 			check = True
# 	if True in values:
# 		return True
# 	return False

# def evaluate(rule, facts, dictionnaire):
# 	if not rule:
# 		return facts, None
# 	if rule.value and rule.value.isalpha():
# 		if rule.value in facts:
# 			return facts, facts[rule.value]
# 		else:
# 			facts[rule.value] = moteur(rule.value, facts, dictionnaire)
# 			return facts, facts[rule.value]
# 	facts, left = evaluate(rule.left, facts, dictionnaire)
# 	fatcs, right = evaluate(rule.right, facts, dictionnaire)
# 	return facts, functions[rule.value](left, right)

# def moteur(querie, facts, dictionnaire):
# 	facts[querie] = False
# 	if querie not in dictionnaire:
# 		return False
# 	values = []
# 	for rule in dictionnaire[querie]:
# 		facts, value = evaluate(rule.left, facts, dictionnaire)
# 		values.append(value)
# 	return solve_querie(rule.right, querie, values, facts)


def solve_querie(querie, values, facts):
	check = False
	#print(querie)
	#print(values)
	#print(facts)
	#print("")
	for q in facts:
		if check == True:
			if facts[q] == None:
				return None
		if q == querie:
			check = True
	if True in values:
		return True
	return False

def check_boucle(dictionnaire, querie):
	if querie in dictionnaire:
		for rule in dictionnaire[querie]:
			if rule["faite"] == True:
				return True
	return False

def evaluate(rule, facts, dictionnaire, cycle, initial_facts):
	if not rule:
		return facts, None, cycle
	if rule.value and rule.value.isalpha():
		if rule.value in facts:
			if cycle == False:
				cycle = check_boucle(dictionnaire, rule.value)
			return facts, facts[rule.value], cycle
		else:
			facts[rule.value], cycle = moteur(rule.value, facts, dictionnaire, cycle, initial_facts)
			return facts, facts[rule.value], cycle
	facts, left, cycle = evaluate(rule.left, facts, dictionnaire, cycle, initial_facts)
	fatcs, right, cycle = evaluate(rule.right, facts, dictionnaire, cycle, initial_facts)
	return facts, functions[rule.value](left, right), cycle

def moteur(querie, facts, dictionnaire, cycle, initial_facts):
	facts[querie] = False
	if querie not in dictionnaire:
		return False, cycle
	values = []
	for rule in dictionnaire[querie]:
		rule["faite"] = True
		facts, value, cycle = evaluate(rule["règle"].left, facts, dictionnaire, cycle, initial_facts)
		values.append(value)
	return solve_querie(querie, values, facts), cycle

def inference(rules, facts, queries, dictionnaire, initial_facts):
	for querie in queries:
		tmp_querie = copy.copy(facts)
		tmp_dictionnaire = copy.deepcopy(dictionnaire)
		if querie in facts:
			result = facts[querie]
		else:
			cycle = False
			result, cycle = moteur(querie, tmp_querie, tmp_dictionnaire, cycle, initial_facts)

			print("Boucle :", cycle)
		if result == None:
			print("Querie '" + querie + "' is Undefined")
		else:
			print("Querie '" + querie + "' is", result)
		print("\n\n\n")