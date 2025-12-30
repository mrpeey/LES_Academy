
#Part 2: Practical Implementation (60%)
#Task 1: AI-Powered Code Completion

#Sorting a List of Dictionaries by a Specific Key

# AI-suggested implementation using sorted()
def sort_dicts_by_key(dicts, key):
	"""
	Sort a list of dictionaries by a specific key using Python's built-in sorted().
	"""
	return sorted(dicts, key=lambda d: d[key])

# Manual implementation using nested loops

def sort_dicts_by_key_manual(dicts, key):
	"""
	Sort a list of dictionaries by a specific key using a manual nested loop (selection sort).
	"""
	dicts = dicts.copy()
	n = len(dicts)
	for i in range(n):
		min_idx = i
		for j in range(i + 1, n):
			if dicts[j][key] < dicts[min_idx][key]:
				min_idx = j
		if min_idx != i:
			dicts[i], dicts[min_idx] = dicts[min_idx], dicts[i]
	return dicts

"""
Analysis:

The AI-suggested function uses Python's built-in sorted() with a lambda, leveraging Timsort (O(n log n)), which is highly efficient and stable. The manual implementation uses a selection sort (O(n^2)), which is much slower for large lists. The AI approach is more concise, readable, and less error-prone, making it preferable for production code. Built-in functions are optimized and tested, while manual sorting is more likely to introduce bugs and inefficiencies. Thus, the AI-suggested code is both more efficient and maintainable.
"""
