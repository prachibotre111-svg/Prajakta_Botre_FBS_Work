# Write a program to convert days into years, months, and days.
total_days=int(input('Enter the total number of days: '))
years=total_days//365

remaining_days = total_days- 365*years

months = remaining_days//30

days=remaining_days-30*months

print(f"{total_days} days is equal to {years} years, {months} months, and {days} days.")