# Write the program to enter P,T,R and calculate Compound Interest.
P=float(input("Enter the principle amount: "))
T=float(input("Enter the time period: "))
R=float(input("Enter the rate  of interest: "))

# Calculating compound interest

CI=P*(1+R/100)**T-P

print("The Compound interest is: ",CI)