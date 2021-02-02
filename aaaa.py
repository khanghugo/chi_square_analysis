def l_manip(l):
	out__ = []
	def chunking(l):
		a = int(len(l) / 2)
		for i in range(0, len(l), a):
			yield l[i:i+a]

	chunks = [i for i in chunking(l)]
	chunk_1 = chunks[0]
	chunk_2 = chunks[1]
	# print(chunk_1)
	# print(chunk_2)
	# bbb = list(chunks)
	# print(bbb)
	# print(a1)
	# print(a2)
	for expected, observed in zip(chunk_1, chunk_2):
		# pass
		out__.append(expected)
		out__.append(observed)
	return out__


def calculate_now(list_a):

	if len(list_a) >= 2:
		expected = list_a.pop(0)
		observed = list_a.pop(0)
		return (expected - observed)**2 / (expected) + calculate_now(list_a)
	else:
		return 0

# l = [32.5, 26, 32.5, 35, 32.5, 29, 32.5, 40]
# a = calculate_now(l)
# print(a)

l = [97, 97, 97, 97, 110, 86, 90, 102]
l = l_manip(l)
# a = list(chunking(l))
print(l)
a = calculate_now(l)
print(a)
