#simple physics calculator

#function calculate velocity
def velocity(x, y, z):
    return (x - y) / z

#function calculate acceleration
def acceleration(x, y, z):
    return (x - y) / z

#function calculate Force
def force(x, y):
    return x * y

#function calculate density
def density(x, y):
    return x / y

#function calculate centripetal force
def centripetal_force(x, y, z):
    return x * (y**2) / z

#users possible choices
print("Types of operations: ")
print("1. Velocity")
print("2. Acceleration")
print("3. Force")
print("4. Density")
print("5. Centripetal Force")

#rx users input and save in a variable
selection = input("Enter the number for which calculation you wish to complete: ")

if selection == "1":
    final_position = float(input("Enter the final position in meters: "))
    initial_position = float(input("Enter the initial position meters: "))
    time = float(input("Enter the time seconds: "))
    print("The velocity is:", velocity(final_position, initial_position, time), "m/s")

elif selection == "2":
    final_velocity = float(input("Enter the final velocity in m/s: "))
    initial_velocity = float(input("Enter the initial velocity in m/s: "))
    time = float(input("Enter the time in seconds: "))
    print("The acceleration is:", acceleration(final_velocity, initial_velocity, time), "m/s^2")

elif selection == "3":
    mass = float(input("Enter the mass in kgs: "))
    acceleration = float(input("Enter the acceleration in m/s^2: "))
    print("The force is:", force(mass, acceleration), "N")

elif selection == "4":
    mass = float(input("Enter the mass in kg or g: "))
    volume = float(input("Enter the volume in m^3 or cm^3: "))
    print("The density is:", density(mass, volume), "(kg/m^3) or (g/cm^3)")

elif selection == "5":
    mass = float(input("Enter the mass in kgs: "))
    velocity = float(input("Enter the velocity in m/s^2: "))
    radius = float(input("Enter the raduis in meters: "))
    print("The centripetal force is:", centripetal_force(mass, velocity, radius), "Newtons")

else:
    print("Sorry, invalid input")
