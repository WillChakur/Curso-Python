#Break
for x in range(1, 11):
    if x == 5:
        break
    print(x)
#O break é utilizado para quebrar um laço de repetição caso algo ocorra
print('\n')
#Continue
for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)
#O continue não quebra o laço de repetição porém ele para a execução da respectiva repetição