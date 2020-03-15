# Python3 code to calculate age in years 
# Source : https://www.geeksforgeeks.org/python-program-to-calculate-age-in-year/

from datetime import date 

def calculateAge(birthDate): 
	days_in_year = 365.2425	
	age = int((date.today() - birthDate).days / days_in_year) 
	return age 
		
# Driver code 
print(calculateAge(date(1997, 2, 3)), "years") 
print(date.today())
