import random



flips = 10
HT = random.randint(0,1)


x = random.choices(['T', 'H'], cum_weights= [.7, 1.0], k=flips).count('H')
percentage = str(x/flips*100)
print("Head was", percentage + "% up! The program performed", flips, "flips.")

