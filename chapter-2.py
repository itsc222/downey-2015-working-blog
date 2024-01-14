message = 'And now for something completely different'
n = 17
pi = 3.1415926535897932

print(n)

#Calculate the number of kilometers in the marathon.
miles = 26.1
print(miles * 1.61)

5
x = 5
print(x + 1)

def vol_sphere (r):
    volume = (4/3) * pi * r ** 3
    return(print(volume))

vol_sphere(5)

def book_costs(n, cover):
    wholesale = (cover * 0.6) * n
    shipping = 3 + 0.75 * (n-1)
    return(wholesale + shipping)

print(book_costs(60, 24.95))

running_time = ((8*60 + 15) * 2 + 3 * (60 * 7 + 12)) / 60

print(running_time)

start_time_min = (60 * 6 + 52)
breakfast_time = (start_time_min + running_time) / 60

print(breakfast_time)