def print_tree(tree, current="current"):
    print(current, tree.value)
    if tree.left is not None:
        print_tree(tree.left, "left")
    if tree.right is not None:
        print_tree(tree.right, "right")

def fill_dict(tree, values):
	if tree.value.isupper():
		values.append(tree.value)
		return values
	if tree.left and tree.left.value in ['+', '|', '^', '!']:
		values = fill_dict(tree.left, values)
	elif tree.left:
		values.append(tree.left.value)
	if tree.right and tree.right.value in ['+', '|', '^', '!']:
		values = fill_dict(tree.right, values)
	elif tree.right:
		values.append(tree.right.value)
	return values

def get_dict(rules):
	dictionnaire = {}
	for rule in rules:
		values = []
		values = fill_dict(rule.right, values)
		for value in values:
			try:
				dictionnaire[value].append(rule)
			except:
				dictionnaire[value] = []
				dictionnaire[value].append(rule)
	return dictionnaire