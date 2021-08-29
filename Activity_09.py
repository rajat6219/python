print("To find volume of tromboloid and radius of sphere,")
l = float(input("Enter the length of tromboloid: "))
b = float(input("Enter the breadth of tromboloid: "))
h = float(input("Enter the height of tromboloid: "))

k=(l**2)+(b**2)+(h**2)

volume_of_tromboloid = ((b**2)*(h**2))/(k**(1/2))
print(f"Volume of tromboloid is {volume_of_tromboloid:.3f}")

radius_of_sphere = (((3*volume_of_tromboloid)/(4*3.14159))**(1/3))
print(f"Radius of sphere is {radius_of_sphere:.3f}")
