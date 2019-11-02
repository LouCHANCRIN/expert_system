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

def evaluate(to_do, rule, facts, dictionnaire):
	if not rule:
		return facts, None
	if rule.value and rule.value.isalpha():
		if rule.value in facts:
			return facts, facts[rule.value]
		else:
			facts[rule.value] = moteur(to_do, rule.value, facts, dictionnaire)
			return facts, facts[rule.value]
	facts, left = evaluate(to_do, rule.left, facts, dictionnaire)
	fatcs, right = evaluate(to_do, rule.right, facts, dictionnaire)
	return facts, functions[rule.value](left, right)

def solve_querie(tree, querie, values):
	print(values)
	if True in values and False not in values and None not in values:
		return True
	return False

def moteur(to_do, querie, facts, dictionnaire):
	values = []
	for i in range(len(to_do)-1, 0, -1):
		print(i)
		if to_do[i] not in dictionnaire:
			print("Insolvable, il n'existe pas de règle pour déterminer la valeur de '" + to_do[i] + "'.")
			return False
		for rule in dictionnaire[to_do[i]]:
			facts, value = evaluate(to_do, rule.left, facts, dictionnaire)
			values.append(value)
	return solve_querie(rule.right, querie, values)

def get_facts(facts, queries):
	facts.remove("=")
	queries.remove("?")
	f = {}
	for fact in facts:
		f[fact] = True
	return f, queries

def check_rule(dictionnaire, rule, facts, to_do):
	if not rule:
		return to_do
	if rule.value and rule.value.isalpha():
		if rule.value not in facts and rule.value not in to_do:
			to_do.append(rule.value)
			to_do = select_letters(rule.value, dictionnaire, facts, to_do)
	elif rule.value:
		to_do = check_rule(dictionnaire, rule.left, facts, to_do)
		to_do = check_rule(dictionnaire, rule.right, facts, to_do)
	return to_do

def select_letters(querie, dictionnaire, facts, to_do):
	try:
		dictionnaire[querie]
	except:
		return to_do
	for rule in dictionnaire[querie]:
		if rule.value in ["=>", "<=>"]:
			to_do = check_rule(dictionnaire, rule.left, facts, to_do)
		else:
			to_do = check_rule(dictionnaire, rule, facts, to_do)
		if False in to_do:
			return to_do
	return to_do

def inference(rules, facts, queries, dictionnaire):
	facts, queries = get_facts(facts, queries)
	print(queries)
	print(facts)
	for querie in queries:
		tmp = copy.copy(facts)
		to_do = [querie]
		to_do = select_letters(querie, dictionnaire, facts, to_do)
		print("A faire :", to_do)
		result = moteur(to_do, querie, tmp, dictionnaire)
		print("Querie '" + querie + "' is", result)