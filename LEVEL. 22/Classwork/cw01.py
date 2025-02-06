#შექმენით for loop რომელიც სამჯერ შეეკითხება მომხმარებელს პაროლს, თუ მომხმარებელმა პაროლი სწორად შეიყვანა დაიბეჭდება "correct" თუ სამ ცდას გადააჭარგბა 
# და პაროლი ვერ გამოიცნო კოდი გამოირთვება და დაიბეჭდება "out of trys"
password = "35619452`945`296465`237645`97635436543235496184618037468016412640923757926576"
user = input ("enter your password:")
for i in range (3):
 print(user)
if user ==password:
 print("correct")
else:
 print("out of trys")