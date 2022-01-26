# Reservation_system
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
