word_definitions = dict()

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""

word_definitions["Tennis"] = "a sport using a tennis racket and ball"
word_definitions["Basketball"] = "a sport using a bball and goal"
word_definitions["Futbol"] = "a sport using a ball"
word_definitions["Ping Pong"] = "a sport with a paddle and ping pong ball"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

# print(word_definitions["Tennis"])
# print(word_definitions["Basketball"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

words = word_definitions.items()
for word in words:
    print(f"The definition of {word[0]} is {word[1]}")








