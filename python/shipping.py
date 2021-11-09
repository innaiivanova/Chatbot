# Codecademy Sal's Shipping
# Inna I. Ivanova

weight = 1.5

# Ground Shipping
if (weight<2):
  cost_ground = weight*1.5+20
elif (2 < weight < 6):
  cost_ground = weight*3+20
elif (6 < weight < 10):
  cost_ground = weight*4+20
elif (weight>10):
  cost_ground = weight*4.75+20
else:
  print("Error")

print("Ground shipping: $", cost_ground)

# Premium Shipping
cost_premium = 125.00

print("Premium Shipping: $", cost_premium)

# Drone Shipping
if (weight<2):
  cost_drone = weight*4.5
elif (2 < weight < 6):
  cost_drone = weight*9
elif (6 < weight < 10):
  cost_drone = weight*12
elif (weight>10):
  cost_drone = weight*14.25
else:
  print("Error")

print("Drone Shipping: $", cost_drone)

