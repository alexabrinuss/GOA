#შექმენით კოდი რომელიც შეაფასებს ბავშვს ასე:
#თუ ქულა 10-ია ან 9 დაპრიტნე A
#თუ ქულა 8-ის ან 7-ის ტოლია დაპრინტე B
#თუ ქულა 6-ის ან 5-ის ტოლია დაპრინტე  C
#თუ 5ზე დაბალია დაპრინტე - ვერ გადახვედი
score = int(input("enter your score:"))
if score ==10:
  print("A")
elif score ==9:
  print("A")
elif score ==8:
  print("B")
elif score ==7:
  print("B")
elif score ==6:
  print("C")
elif score ==5:
  print("C")
elif score <5:
  print("hold on")