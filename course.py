from collections import Counter
a = ["ab", "ac", "ac", "ab", "bd"]
my_counter = Counter(a)
print(my_counter.most_common(1))
