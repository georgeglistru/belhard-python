import contextlib, io
import string

zen = io.StringIO()
with contextlib.redirect_stdout(zen):
    import this
zen = zen.getvalue()
print(zen)

lines = zen.splitlines()
print(f"Number of lines is {len(lines)}")

# remove all punctuation marks
zen_without_punctuation = zen.translate(str.maketrans('', '', string.punctuation))
# list with separate words
words = zen_without_punctuation.split()
# convert all words to lower case
words = [x.lower() for x in words]
from collections import Counter
c = Counter(words)
print(c)
print(f"is frequency - {c['is']}")
print(f"and frequency - {c['and']}")
print(f"or frequency - {c['or']}")
changed_zen = zen.replace("is", "is not")
print("=================")
print("Changed Zen:")
print("=================")
print(changed_zen)


