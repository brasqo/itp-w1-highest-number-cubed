"""This is the entry point of the program."""


# My attempt...Failed miserably.
# def highest_number_cubed(limit):
    
# #testresult = 12000
    
#     test2 = int(limit**(1./3.))
    
#     if test2**3 == limit:
#         print ('ok ' + str(test2) + '.')
#     else:
#         if test2**3 == limit:
#           return 'nope'

# # print(highest_number_cubed(22))

#Jason while solution

def highest_number_cubed(limit):
    
    number = 0
    
    while True:
        number += 1
        if number ** 3 > limit:
            return number - 1

print(highest_number_cubed(12000))


# 1 ^ 3 = 1 <30? True...keep going 
# 2 ^ 3 = 8 <30? True...Keep going
# 3 ^ 3 = 27 <30? True...keep going
# 4 ^ 3 = 64 <30? False...Flag, refer to previous value