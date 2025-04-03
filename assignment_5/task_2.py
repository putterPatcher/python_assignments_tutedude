a = [i for i in range(1, 11)]
print("Original list: {}".format(a))
e = a[:5]
print("Extracted first five elements: {}".format(e))
e = [e[i] for i in range(len(e)-1, -1, -1)]
print("Reversed extracted elements: {}".format(e))
