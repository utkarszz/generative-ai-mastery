for i in range(1,11):
  print(i)

count = 1
while count <= 10:
  print(count)
  count += 1

for i in range(1,21):
  if i % 2 == 0:
    print(i)

for i in range(1,11):
  if i == 5:
    break
  print(i)

for i in range(1,11):
  if i == 5:
    continue
  print(i)  

for i in range(1,6):
    for j in range(1,5):
        print("*", end=" ")
    print()