from assignProjects import *

maxSolution = 10

instance = compile()
ace = solver(ACE)

cpt = 0
opti = 0
result = solve()
solution = values(p)
mini = sum(values(c))

while cpt < maxSolution and result in {SAT, OPTIMUM}:
    print(cpt)
    if result is OPTIMUM:
        solution = values(p)
        break

    tmp_mini = sum(values(c))
    if tmp_mini <= mini:
        mini = tmp_mini
        solution = values(p)

    print(values(p))
    #minimize( Sum(c) )
    cpt += 1
    result = solve()
    print(f"Solution : {cpt}")
    satisfy(p != values(p))

if result not in {SAT, OPTIMUM}:
    print("UNSAT")
    exit(0)

print("Score :", mini)
print(values(s))
print(value(x))
for i in range(nStudents):
    print(f"The student ({i}) {names[i]} {first_names[i].lower()} ({schools[i]}) will work on project ({solution[i]}) {projects[solution[i]]} ")

"""

elif result is OPTIMUM:
    for i in range(nPersons):
        print(f"The student ({i}) {names[i]} {first_names[i].lower()} will work on project ({value(p[i])}) \'{projects[value(p[i])]}\'")
    print("Bound : ", bound())
"""