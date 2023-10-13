#leep year

"""
year % 4 == 0
year % 100 != 0 /
year % 400 == 0

"""
def isleapyear(year):
    if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
      return True
    else:
      return False
      
year = 2012

if isleapyear(year):
  print('{} is a leep year.'.format(year))
else:
  print('{} is a not leap year.'.format(year))

# Write your code here
# Not sure where to start?
# Check out README.md under "Files"
