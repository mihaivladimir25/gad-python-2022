print("Hello World!")


snow_case_var = 1

for i in range(2):
    print(f"Hello World! {i}")

def new_function(a, b):
    return a + b

print(type(2))

l = []
n = []
n = 'salut'
if not l:
    print('lista vida')

print(l is n)
print(l == n)

print("""
asdasfasd dasgfsdgasda]
    asdasdasd       -> asdasdasd
    asdasdasd       -> asdasdasd
qweqdasdasdqweasdasd
""")

print("coco \n"
      "dfsdf")

nume = 'Cojocaru'
prenume = 'Mihai'

body_text = f"""
Buna ziua!

Ma numesc {nume} {prenume}

Bine ati venit pe websiteul nostru!
"""

print(body_text)

l = [1, 2, 3]
print(l)
l[1] = 0
print(l)

name = 'Mihai'
print(name[1])

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
g = l[:]
l[0] = 'a'

print(l)
print(g)

print(l[-1])

d = {
    'Nume': 'Cojocaru',
    'Prenume': 'Mihai',
    'Varsta': 20
}

t = dict(d)

print(t)

# print(d['Varsta'])
print(d.get('Varsta'))

for key, value in d.items():
    print(f'{key} -> {value}')

s = {1, 2, 3}
c = {1, 2}
print(c.issubset(s))
print(c.intersection(s))