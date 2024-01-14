# print(1 + 1)

print('Hello, World!')

def calculator (input):
    return(print(input))
    
calculator(40 + 2)
calculator(43 - 1)
calculator(6*7)
calculator(84/2)
calculator(6**2 + 6)

#bitwise operators

def type_print(input):
    return(print(type(input)))


type_print(2)
type_print(42.0)
type_print("42.0")
type_print("Hello, World!")

#Exercise 1.2
calculator(42*60 + 42)
calculator(10/1.61)

race_time = (42*60 + 42)
min_per_kilometer = (race_time / 10 / 60)
min_per_mile = (min_per_kilometer * 1.61)
print(min_per_mile)

miles = (10 / 1.61)
hours = (race_time / 3600)
miles_per_hour = miles/hours

print(miles_per_hour)


