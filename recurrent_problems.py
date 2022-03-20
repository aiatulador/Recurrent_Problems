from collections import deque

print("\t\t\tRecurrent Problems\n\n")
print("\t\t\tTower of Hanoi")
print("\t\t\tLines in the plane")
print("\t\t\tJosephus Problem")

def tower_of_hanoi():
  disk = int(input("Enter Number of Disks: "))
  move = pow(2,disk) - 1
  print(move)
  

def lines_in_the_plane():
  n = int(input("Enter the numbers of line: "))
  r = (pow(n,2)+ n + 2)/2 
  print(r)

def josephus_problem():
  
  josh = int(input("Number of people: "))

  #josh = 10

  range_start = 1
  range_target = josh

  if (range_start == range_target):
    print(createList(range_start,range_target))
  else:
    our_list = []
    temp = 1
    while (temp < range_target + 1):  
      our_list.append(temp)
      temp += 1
   
  #print(our_list)
  x = deque(our_list)

  while len(x)>1:
    x.rotate(-3)
    x.pop()

  print('Survived Person:' , x.pop())


tower_of_hanoi()
lines_in_the_plane()
josephus_problem()


