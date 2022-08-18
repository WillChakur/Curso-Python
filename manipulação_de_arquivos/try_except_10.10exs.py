filename = 'pride_and_prejudice.txt'

try:
    with open(filename) as f_object:
        contents = f_object.read()
except FileNotFoundError:
    pass
else:
    words = str(contents.lower()).split()
    print(f'O texto possuí {words.count("the")} "the"')