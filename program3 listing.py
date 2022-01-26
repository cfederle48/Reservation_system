# Chrissi Federle
# CS115-19Z2
# Spring 2021
# Programming Assignment #3
#
# Program Description
#
# This program will accept, from the user, a day of the week for a reservation,
# the hour in military time for a possible reservation, and the minute portion
# of time of a possible reservation all subject to certain restrictions. Then it
# will display the civilian time of the hopeful reservation. If the restaurant
# is open, then the corresponding special and a greeting will be displayed. If
# the restaurant is closed on this day at this time, a negative message will be
# displayed and the next available time, day, and corresponding special will be
# displayed.
#
# Program Preconditions
#
# 1. The user will enter the day of the week, to be called
#    user_day_of_reservation, which must be a string called Monday, Tuesday,
#    Wednesday, Thursday, Friday, Saturday, or Sunday.
#
# 2. The user will enter the hour portion of time, to be called
#    user_hour_of_reservation, which must be a whole number between 0 and 23.
#
# 3. The user will enter the minutes portion of time, to be called
#    user_minutes_of_reservation, which must be a whole number between 0 and 59.
#
# 4. The program will check the range of each input value and adjust it if
#    necessary. It will also check the day of week input and continue to ask
#    until a proper day of the week is entered.
#
# Program Postconditions
#
# 1. The program will display the hopeful reservation time of the user including
#    the day of the week, to be called user_day_of_reservation, the hour to be
#    called civilian_hour_reservation_time, and the minutes to be called
#    user_minutes_of_reservation with am/pm respectively. This time will be the
#    civilian time and day of week that the user wants to come into the
#    restaurant to eat.
#
# 2. The program will display either a positive or negative message based on if
#    the restaurant is closed or open at the requested time. If the restaurant
#    is open it will then display the corresponding special for that meal and
#    day of the week to be called special. If the restaurant is closed it will
#    then display the next day and time they will be open and the corresponding
#    special.


# Variable Dictionary
#
#
# user_day_of_reservation            the day of the reservation, as given by the
#                                    user
#
# user_hour_of_reservation           the hour of the reservation, as given by
#                                    the user
#
# user_minutes_of_reservation        the minute of the reservation, as given by
#                                    the user
#
# open_lunch_military                opening time for Monday-Saturday lunch in
#                                    military time that could easily be changed
#                                    later if the hours of the restaurant were
#                                    to change.
#
# open_lunch_civilian                opening time for Monday-Saturday lunch in
#                                    civilian time that could be changed.
#
# close_lunch_military               closing time for Monday-Saturday lunch in
#                                    military time that could easily be changed
#                                    later if the hours of the restaurant were
#                                    to change.
#
# close_lunch_civilian               opening time for Monday-Saturday lunch in
#                                    civilian time that could be changed.
#
# open_dinner_sat_military           opening time for Saturday dinner in
#                                    military time that could easily be changed
#                                    later if the hours of the restaurant were
#                                    to change.
#
# open_dinner_sat_civilian           opening time for Saturday dinner in
#                                    civilian time that could be changed.
#
# close_dinner_sat_military          closing time for Saturday dinner in military
#                                    time that could easily be changed later if
#                                    the hours of the restaurant were to change.
#
# close_dinner_sat_civilian          closing time for Saturday dinner in
#                                    civilian time that could be changed.
#
# open_brunch_sun_military           opening time for Sunday brunch in military
#                                    time that could easily be changed later if
#                                    the hours of the restaurant were to change.
#
# open_brunch_sun_civilian           opening time for Sunday brunch in
#                                    civilian time that could be changed.
#
# close_brunch_sun_military          closing time for Sunday brunch in military
#                                    time that could easily be changed later if
#                                    the hours of the restaurant were to change
#
# close_brunch_sun_civilian          closing time for Sunday brunch in
#                                    civilian time that could be changed.
#
# mon_special                        the Monday lunch special.
#
# tue_special                        the Tuesday lunch special.
#
# wed_special                        the Wednesday lunch special.
#
# thu_special                        the Thursday lunch special.
#
# fri_special                        the Friday lunch special.
#
# sat_lunch_special                  the Saturday lunch special.
#
# sat_dinner_special                 the Saturday dinner special.
#
# sun_special                        the Sunday brunch special.
#
# civilian_hour_reservation_time     the reservation time in civilian time
#                                    calculated from the user input in military
#                                    time
#
# reservation_in_minutes             the total number of minutes converted from
#                                    the user input of hours and minutes
#
# open_lunch_minutes                 the opening time in minutes of the
#                                    restaurant for lunch Monday-Saturday
#
# close_lunch_minutes                the closing time in minutes of the
#                                    restaurant for lunch Monday-Saturday
#
# open_sat_dinner_minutes            the opening time in minutes of the
#                                    restaurant for dinner on Saturday
#
# close_sat_dinner_minutes           the closing time in minutes of the
#                                    restaurant for dinner on Saturday
#
# open_sun_brunch_minutes            the opening time in minutes of the
#                                    restaurant for brunch on Sunday
#
# close_sun_brunch_minutes           the closing time in minutes of the
#                                    restaurant for brunch on Sunday
#
# open_lunch_range                   the open time range defined for Monday
#                                    through Saturday lunch.
#
# open_brunch_range                  the open time range defined for Sunday
#                                    brunch.
#
# open_dinner_range                  the open time range defined for Saturday
#                                    dinner.
#
# special                            the special assigned to print out based on
#                                    the day of week and time of day.



#################
# Input section #
#################

# Give the initial prompt for the input statements for the reservation that the
# user wants
print('For your desired reservation, please:')

# ask for and get the day of the reservation from the user
user_day_of_reservation = input('Enter the day: ')

# validifies the day of the week entered as a day
while (user_day_of_reservation != 'Monday') and (user_day_of_reservation != \
'Tuesday') and (user_day_of_reservation != 'Wednesday') and \
(user_day_of_reservation != 'Thursday') and (user_day_of_reservation != 'Friday')\
and (user_day_of_reservation != 'Saturday') and (user_day_of_reservation != \
'Sunday'):
    print('ERROR: The day must be Monday, Tuesday, Wednesday, Thursday,',\
    'Friday, Saturday, or Sunday.')
    user_day_of_reservation = input('Enter a correct day: ')

# ask for and get the hour of the reservation from the user
user_hour_of_reservation = int(input('Enter the hours portion of time: '))

# make sure the hour is between 0 and 23
while (user_hour_of_reservation < 0 or user_hour_of_reservation > 23):
    print('ERROR: The hour must be between 0 and 23.')
    user_hour_of_reservation = int(input('Enter the correct hours: '))

# ask for and get the minute of the reservation from the user
user_minutes_of_reservation = int(input('Enter the minutes portion of time: '))

# make sure the minute is between 0 and 59
while (user_minutes_of_reservation < 0 or user_minutes_of_reservation > 59):
    print('ERROR: The minutes must be between 0 and 59.')
    user_minutes_of_reservation = int(input('Enter the correct minutes: '))


###################
# Process section #
###################

# the opening time on Monday through Saturday for lunch in military time
open_lunch_military = 11

# the opening time on Monday through Saturday for lunch in civilian time
open_lunch_civilian = '11 am'

# the closing time on Monday through Saturday for lunch in military time
close_lunch_military = 15

# the closing time on Monday through Saturday for lunch in civilian time
close_lunch_civilian = '3 pm'

# the opening time on Saturday for dinner in military time
open_dinner_sat_military = 17

# the opening time on Saturday for dinner in civilian time
open_dinner_sat_civilian = '5 pm'

# the closing time on Saturday for dinner in military time
close_dinner_sat_military = 23

# the closing time on Saturday for dinner in civilian time
close_dinner_sat_civilian = '11 pm'

# the opening time on Sunday for brunch in military time
open_brunch_sun_military = 9

# the opening time on Sunday for brunch in civilian time
open_brunch_sun_civilian = '9 am'

# the closing time on Sunday for brunch in military time
close_brunch_sun_military = 14

# the closing time on Sunday for brunch in civilian time
close_brunch_sun_civilian = '2 pm'

# assign the specials for every meal of the week
mon_special        = 'Hummus with Pita Bread'
tue_special        = 'Moussaka with Zucchini'
wed_special        = 'Falafel with Tahini Sauce'
thu_special        = 'Calamari with Tomatoes'
fri_special        = 'Souvlaki with Tzatziki Sauce'
sat_lunch_special  = 'Gyros with Onions'
sat_dinner_special = 'Spanakopita with Feta Cheese'
sun_special        = 'Grape Leaves with Vegetables'

# calculate the time of day in civilian time from the user input for hours
# between 13 and 23
if user_hour_of_reservation > 12 and user_hour_of_reservation <= 23:
    civilian_hour_reservation_time = user_hour_of_reservation - 12

# calculate the time of day from the user input of 0, meaning midnight
elif user_hour_of_reservation == 0:
    civilian_hour_reservation_time = 12

# assign the time of day to the correct variable if it is between 1 and 12
else:
    civilian_hour_reservation_time = user_hour_of_reservation

# convert all hours and minutes from user entry to just minutes
reservation_in_minutes = user_hour_of_reservation * 60 + \
user_minutes_of_reservation

# opening time on Monday through Saturday for lunch converted to minutes
open_lunch_minutes = open_lunch_military * 60

# closing time on Monday through Saturday for lunch converted to minutes
close_lunch_minutes = close_lunch_military * 60

# opening time on Saturday for dinner converted to minutes
open_sat_dinner_minutes = open_dinner_sat_military * 60

# closing time on Saturday for dinner converted to minutes
close_sat_dinner_minutes = close_dinner_sat_military * 60

# opening time on Sunday for brunch converted to minutes
open_sun_brunch_minutes = open_brunch_sun_military * 60

# closing time on Sunday for brunch converted to minutes
close_sun_brunch_minutes = close_brunch_sun_military * 60


##################
# Output section #
##################

# display the user's reservation time request if it is pm and less than ten
# minutes
if user_hour_of_reservation >= 12 and user_hour_of_reservation <= 23 and \
user_minutes_of_reservation < 10:
    print('\nYou have requested a reservation for',user_day_of_reservation, \
    'at', str(civilian_hour_reservation_time) + ':0' + \
    str(user_minutes_of_reservation) + ' pm.')

# display the user's reservation time request if it is pm and more than or equal
# to ten minutes
if user_hour_of_reservation >= 12 and user_hour_of_reservation <= 23 and \
user_minutes_of_reservation >= 10:
    print('\nYou have requested a reservation for',user_day_of_reservation, \
    'at', str(civilian_hour_reservation_time) + ':' + \
    str(user_minutes_of_reservation) + ' pm.')

# display the user's reservation time request if it is am and less than ten
# minutes
if user_hour_of_reservation >= 0 and user_hour_of_reservation < 12 and \
user_minutes_of_reservation < 10:
    print('\nYou have requested a reservation for',user_day_of_reservation, \
    'at', str(civilian_hour_reservation_time) + ':0' + \
    str(user_minutes_of_reservation) + ' am.')

# display the user's reservation time request if it is am and more than or equal
# to ten minutes
if user_hour_of_reservation >= 0 and user_hour_of_reservation < 12 and \
user_minutes_of_reservation >= 10:
    print('\nYou have requested a reservation for',user_day_of_reservation, \
    'at', str(civilian_hour_reservation_time) + ':' + \
    str(user_minutes_of_reservation) + ' am.')

# assign a time period to open for Monday through Saturday lunch
if (reservation_in_minutes >= open_lunch_minutes and \
reservation_in_minutes <= close_lunch_minutes):
    open_lunch_range  = True
    open_dinner_range = False
    open_brunch_range = False

# assign a time period to open for Saturday dinner
elif (user_day_of_reservation == 'Saturday' and reservation_in_minutes >= \
open_sat_dinner_minutes and reservation_in_minutes <= close_sat_dinner_minutes):
    open_dinner_range = True
    open_lunch_range  = False
    open_brunch_range = False

# assign a time period to open for Sunday brunch
elif (user_day_of_reservation == 'Sunday' and reservation_in_minutes >= \
open_sun_brunch_minutes and reservation_in_minutes <= close_sun_brunch_minutes):
    open_brunch_range = True
    open_lunch_range  = False
    open_dinner_range = False

# assign all statements to false if the restaurant is closed
else:
    open_brunch_range = False
    open_lunch_range  = False
    open_dinner_range = False

# assign a special to Monday lunch
if user_day_of_reservation == 'Monday' and open_lunch_range == True:
    special = mon_special

# display the Monday lunch special
    print("\nAll right! We’ll be open for lunch then! \nOur special will be", \
    special + '.')

# assign a special to Tuesday lunch
elif user_day_of_reservation == 'Tuesday' and open_lunch_range == True:
    special = tue_special

#display the Tuesday lunch special
    print("\nAll right! We’ll be open for lunch then! \nOur special will be", \
    special + '.')

# assign a special to Wednesday lunch
elif user_day_of_reservation == 'Wednesday' and open_lunch_range == True:
    special = wed_special

# display the Wednesday lunch special
    print("\nAll right! We’ll be open for lunch then! \nOur special will be", \
    special + '.')

# assign a special to Thursday lunch
elif user_day_of_reservation == 'Thursday' and open_lunch_range == True:
    special = thu_special

# display the Thursday lunch special
    print("\nAll right! We’ll be open for lunch then! \nOur special will be", \
    special + '.')

# assign a special to Friday lunch
elif user_day_of_reservation == 'Friday' and open_lunch_range == True:
    special = fri_special

# display the Friday lunch special
    print("\nAll right! We’ll be open for lunch then! \nOur special will be", \
    special + '.')

# assign specials to Saturday
elif user_day_of_reservation == 'Saturday':

# assign a special to Saturday lunch
    if open_lunch_range == True:
        special = sat_lunch_special

# display the Saturday lunch special
        print("\nAll right! We’ll be open for lunch then! \nOur special will be",\
        special + '.')

# assign a special to Saturday dinner
    elif open_dinner_range == True:
        special = sat_dinner_special

# display the Saturday dinner special
        print("\nGood news! We’ll be open for dinner then!\nOur special will be",\
        special + '.')

# display the negative message for neither opening time on Saturday
    else:
        print('\nSorry! We won’t be open then.')

# assign a special to Sunday brunch
elif user_day_of_reservation == 'Sunday' and open_brunch_range == True:
    special = sun_special

# display the Sunday brunch special
    print("\nCongratulations! We’ll be open for brunch then! \nOur special will",\
    "be",special + '.')

# display an apology for not being open at the requested time
else:
        print('\nSorry! We won’t be open then.')

# display the next opening time being Monday morning with the special. This
# assumes a user input time of after brunch on Sunday or before lunch Monday.
if (open_lunch_range == False) and ((user_day_of_reservation == 'Monday' and \
reservation_in_minutes < open_lunch_minutes) or \
(user_day_of_reservation == 'Sunday' and reservation_in_minutes > \
close_sun_brunch_minutes)):
    print('However, please join us when we next open at', \
    open_lunch_civilian, 'on Monday. \nAt that time, our',
    'special will be', mon_special)

# display the next opening time being Tuesday monring with the special. This
# assumes a user input time of after lunch on Monday or before lunch Tuesday.
elif (open_lunch_range == False) and ((user_day_of_reservation == 'Tuesday' and \
reservation_in_minutes < open_lunch_minutes) or \
(user_day_of_reservation == 'Monday' and reservation_in_minutes > \
close_lunch_minutes)):
    print('However, please join us when we next open at', \
    open_lunch_civilian, 'on Tuesday. \nAt that time, our',
    'special will be', tue_special)

# display the next opening time being Wednesday morning with the special. This
# assumes a user input time of after lunch on Tuesday or before lunch Wednesday.
elif (open_lunch_range == False) and ((user_day_of_reservation == 'Wednesday' \
and reservation_in_minutes < open_lunch_minutes) or \
(user_day_of_reservation == 'Tuesday' and reservation_in_minutes > \
close_lunch_minutes)):
    print('However, please join us when we next open at',
    open_lunch_civilian, 'on Wednesday. \nAt that time, our', \
    'special will be', wed_special)

# display the next opening time being Thursday morning with the special. This
# assumes a user input time of after lunch on Wednesday or before lunch Thursday.
elif (open_lunch_range == False) and ((user_day_of_reservation == 'Thursday' and \
reservation_in_minutes < open_lunch_minutes) or \
(user_day_of_reservation == 'Wednesday' and reservation_in_minutes > \
close_lunch_minutes)):
    print('However, please join us when we next open at', \
    open_lunch_civilian, 'on Thursday. \nAt that time, our',
    'special will be', thu_special)

# display the next opening time being Friday morning with the special. This
# assumes a user input time of after lunch on Thursday or before lunch Friday.
elif (open_lunch_range == False) and ((user_day_of_reservation == 'Friday' and \
reservation_in_minutes < open_lunch_minutes) or \
(user_day_of_reservation == 'Thursday' and reservation_in_minutes > \
close_lunch_minutes)):
    print('However, please join us when we next open at', \
    open_lunch_civilian, 'on Friday. \nAt that time, our',
    'special will be', fri_special)

# display the next opening time being Saturday morning with the special. This
# assumes a user input time of after lunch on Friday or before lunch Saturday.
elif (open_lunch_range == False) and ((user_day_of_reservation == 'Saturday' and \
reservation_in_minutes < open_lunch_minutes) or \
(user_day_of_reservation == 'Friday' and reservation_in_minutes > \
close_lunch_minutes)):
    print('However, please join us when we next open at', \
    open_lunch_civilian, 'on Saturday. \nAt that time, our',
    'special will be', sat_lunch_special)

# display the next opening time being Saturday night with the special. This
# assumes a user input time of after lunch on Saturday or before dinner Saturday.
elif (open_lunch_range == False and open_dinner_range == False) and \
(user_day_of_reservation == 'Saturday') and (reservation_in_minutes < \
open_sat_dinner_minutes and reservation_in_minutes > \
close_lunch_minutes):
    print('However, please join us when we next open at', \
    open_dinner_sat_civilian, 'on Saturday. \nAt that time, our',
    'special will be', sat_dinner_special)

# display the next opening time being Sunday for brunch with the special. This
# assumes a user input time of after dinner on Saturday or before Sunday brunch.
elif (open_dinner_range == False and open_lunch_range == False) and \
(user_day_of_reservation == 'Sunday') and (reservation_in_minutes < \
open_sun_brunch_minutes or reservation_in_minutes > close_sat_dinner_minutes):
    print('However, please join us when we next open at', \
    open_brunch_sun_civilian, 'on Sunday. \nAt that time, our',
    'special will be', sun_special)
