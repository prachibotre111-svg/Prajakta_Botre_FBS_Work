# Write a program to enter P,T,R and calculate simple interest.
P=float(input("Enter the principle amount: "))
T=float(input("Enter the time period: "))
R=float(input("Enter the rate  of interest: "))

# calculating simple interest
SI=(P*T*R)/100

print("The simple interest is:", SI)
