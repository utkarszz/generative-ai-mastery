def calculate_result(a,b,c):
  return a+b+c,(a+b+c)/3


a=int(input("Enter marks in subject 1: "))
b=int(input("Enter marks in subject 2: "))
c=int(input("Enter marks in subject 3: "))

total, average = calculate_result(a, b, c)
print(f"Total marks: {total}")
print(f"Average marks: {average}")