# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         print(self.time)

# boston_clock = Clock('5:30')
# paris_clock = boston_clock
# paris_clock.time = '10:30'
# boston_clock.print_time()


boston_clock = []
paris_clock = boston_clock
print(id(paris_clock))
print(id(boston_clock))
paris_clock.append(2)
print(id(paris_clock))
print(id(boston_clock))