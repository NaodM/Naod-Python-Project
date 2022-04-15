#Python Payroll Program with Input Validation 

hourlyRate=15
currency='$'

hellowhatisyourname=input('Enter your name')
dailyHours=input('Enter daily hours: ')
daysofTheWeek=input('How many days a week? ')

totalHoursPerWeek=float(dailyHours)* int(daysofTheWeek)
payDay=float(totalHoursPerWeek)*int(hourlyRate)

print()
print('Hours a day: ' , dailyHours)
print('Hours a week:' , totalHoursPerWeek)
print('Hourly Rate: ' ,hourlyRate)
print( currency+ ' ' ,payDay, ''+'Naod NET PAY A WEEK')