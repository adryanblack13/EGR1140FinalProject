# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:08:41 2017

@author: adrian
"""

import math as mt
import time
import os
import matplotlib.pyplot as plt
import numpy as np

GRAVITY = 9.789337  # Value of gravity in the DC area
HALF_GRAVITY = GRAVITY/2
PI = 3.14159  # (constant) value of pi
AIR_DENSITY = 1.22  # (constant) air density: kg/m^3

# Calculates person_object_velocity for cone shaped parachutes
def person_object_CONE():
   a = "Person"
   b = "Object"

   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")
   print("Is this parachute launch for an Object or Person?\n")
   print("a) Person")
   print("b) Object\n")


   Selected_choice = raw_input("Valid input should be 'a' or 'b' \n")

   while True:
       if Selected_choice == "a" or Selected_choice == "A":
           pweight = raw_input("\nWhat is the weight of the person(lb)?\n")
           P_Weight = float(pweight)
           P_slugAns = (P_Weight) / (GRAVITY)
           PersonMass = P_slugAns * 14.5939

           calc_person_cone(PersonMass)
           break
       elif Selected_choice == "b" or Selected_choice == "B":
           ooWeight = raw_input("What is the weight of the object (lb)? \n")
           Weight = float(ooWeight)
           slugAns = (Weight) / (GRAVITY)  # Pounds divided by accerlation(m/s**2) is a unit called slug
           ObjectMass = slugAns * 14.5939  # Converting slugs to mass

           calc_cone(ObjectMass)
           break

       else:

           time.sleep(2)
           print "\nError! ENTER A VALID CHOICE!\n"
           del Selected_choice
           print("Is this parachute launch for an Object or Person?\n")
           print("a) Person")
           print("b) Object\n")
           Selected_choice = raw_input("Valid input should be 'a' or 'b' \n")
           continue

#SENDING DOWN A PERSON WITH A CONE SHAPED PARACHUTE!
def calc_person_cone(Mass_Of_Person):
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")
   print(
   "\nYou've chosen to simulate a PERSON skydiving, with a CONE-shape parachute. This is more complicated than sending an object,")
   print("YOU WILL BE ASKED ALOT OF QUESTIONS!.\n")
   time.sleep(3)
   PERSON_MASS = Mass_Of_Person

   while True:
       PLANE_MOVEMENT = raw_input(
           "Does the plane that the jumper is jumping from have a initial velocity to consider for? (y/n) \nNOTE: This is a simulation so it's okay to say 'n' \n")
       if (PLANE_MOVEMENT == "y" or PLANE_MOVEMENT == "Y"):
           PLANE_SPEED = input("What is the velocity of the plane(Along Y-axis) (m/s)? \n")
           break
       elif (PLANE_MOVEMENT == "n" or PLANE_MOVEMENT == "N"):
           PLANE_SPEED = 0
           break
       else:
           print("NOT A VALID INPUT! ")
           print("\n")

   # Asking if there is any vertical velocity prior to jumping for example if the jumper has a running start jumping down
   while True:
       VERTICAL_VELOCITY_INITIAL_QUESTION = raw_input(
           "Does the jumper have an initial VERTICAL(Z-axis) velocity?(y/n) \n")

       if (VERTICAL_VELOCITY_INITIAL_QUESTION == "y" or VERTICAL_VELOCITY_INITIAL_QUESTION == "Y"):
           VERTICAL_VELOCITY_INITIAL = input("What is the initial VERTICAL(Z-axis) velocity of the jumper (m/s)? \n")
           break
       elif (VERTICAL_VELOCITY_INITIAL_QUESTION == "n" or VERTICAL_VELOCITY_INITIAL_QUESTION == "N"):
           VERTICAL_VELOCITY_INITIAL = 0
           break
       else:
           print("NOT A VALID ANSWER! \n")
           print("\n")

   # Asking if there is any horizontal velocity prior to jumping for example if the jumper has a running start
   while True:
       HORIZONTAL_VELOCITY_INITIAL_QUESTION = raw_input(
           "Does the jumper have an initial HORIZONTAL(X-axis) velocity?(y/n) \n")
       if (HORIZONTAL_VELOCITY_INITIAL_QUESTION == "y" or HORIZONTAL_VELOCITY_INITIAL_QUESTION == "Y"):
           HORIZONTAL_VELOCITY_INITIAL = input(
               "What is the initial HORIZONTAL(X-axis) velocity of the jumper (m/s)? \n")
           break
       elif (HORIZONTAL_VELOCITY_INITIAL_QUESTION == "n" or HORIZONTAL_VELOCITY_INITIAL_QUESTION == "N"):
           HORIZONTAL_VELOCITY_INITIAL = 0
           break
       else:
           print("NOT A VALID ANSWER! \n")
           print("\n")

   while True:
       try:
           JUMP_HEIGHT = float(raw_input(
               "\nWhat height does the jumper decide to jump from (meters)?\nNOTE: If you enter '0' then the default height is 4000m\n"))
           if (JUMP_HEIGHT == 0):
               JUMP_HEIGHT = 4000
               break
           elif (JUMP_HEIGHT < 0):
               print("The maximum height cannot be less than zero! \n")
               print("\n")
           elif (JUMP_HEIGHT > 0):
               break
           else:
               print("NOT A VALID ANSWER! \n")
       except ValueError:
           print("\nThat was not a number, Please enter a number! \n")

   TIME_OF_FLIGHT = mt.sqrt((JUMP_HEIGHT) / (HALF_GRAVITY))
   print(
   "Your flight lasts: %.2f" % TIME_OF_FLIGHT + " seconds\nNOTE: This flight time is if the jumper does not open the parachute! \n")
   # print("Please select the time your simulated jumper decides to open the parachute, your range is from: [0-%.2f] " %TIME_OF_FLIGHT)
   # print("\n")

   while True:
       try:
           OPENING_PARACHUTE = float(raw_input(
               "Please select the time (in seconds) your simulated jumper decides to open the parachute, your range is from: [0-%.2f] " % TIME_OF_FLIGHT))
           print("\n")
           if (OPENING_PARACHUTE < TIME_OF_FLIGHT and OPENING_PARACHUTE > 0):
               break
           else:
               print("ERROR, Number not in range! \n")
       except ValueError:
           print("\nThat was not a number, Please enter a number! \n")

   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   JUMPER_HORIZONTAL_DISPLACEMENT = HORIZONTAL_VELOCITY_INITIAL * OPENING_PARACHUTE  # X-coordinate point for position when the parachute dude deployed his/her parachute!
   print(
   "Your parachute dude's horizontal displacement position relative to the origin (plane): %.2f" % JUMPER_HORIZONTAL_DISPLACEMENT + "m \n")  # X-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_HORIZONTAL_VELOCITY = HORIZONTAL_VELOCITY_INITIAL  # X-coordinate point for velocity
   print(
   "Your parachute dude's horizontal velocity before the parachute is deployed is approximately: %.2f" % JUMPER_HORIZONTAL_VELOCITY + "m/s \n")  # X-coordinate point for velocity
   print("NOTE: This is because there is no acceleration in the x-axis \n")

   JUMPER_Y_AXIS_DISPLACEMENT = PLANE_SPEED * OPENING_PARACHUTE  # Y-coordinate point for position when the parachute dude deployed his/her parachute!
   print(
   "Your parachute dude's y-direction displacement is (due to plane's speed): %.2f" % JUMPER_Y_AXIS_DISPLACEMENT + "m\n")  # Y-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_Y_AXIS_VELOCITY = PLANE_SPEED  # Y-coordinate point for velocity
   print(
   "Your parachute dude's y-direction velocity is (due to plane's speed): %.2f" % JUMPER_Y_AXIS_VELOCITY + "m/s\n")  # Y-coordinate point for velocity

   JUMPER_VERTICAL_DISPLACEMENT = JUMP_HEIGHT + (VERTICAL_VELOCITY_INITIAL * OPENING_PARACHUTE) - (
   HALF_GRAVITY * OPENING_PARACHUTE ** 2)  # Z-coordinate point for position when the parachute dude deployed his/her parachute!
   print(
   "Your parachute dude's vertical displacement position relative to the initial position is: %.2f" % JUMPER_VERTICAL_DISPLACEMENT + "m \n")  # Z-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_VERTICAL_VELOCITY = VERTICAL_VELOCITY_INITIAL - (
   GRAVITY * OPENING_PARACHUTE)  # Z-coordinate point for velocity
   print(
   "Your parachute dude's vertical velocity before the parachute is deployed is approximately: %.2f" % JUMPER_VERTICAL_VELOCITY + "m/s \n")  # Z-coordinate point for velocity

   time.sleep(
       6)  # Making the python sleep for about 6 seconds, this is so that the user doesn't get bombarded with more incoming information, 4 seconds is enough to digest information before being thrown another screen

   for counter in range(0, 3,
                        1):  # THE COORDINATES ARE ALREADY CALCULATED BUT IT SLEEPS FOR UNTIL WHEN COUTNER HITS 3 SECONDS AND THEN PROCEEDS TO SHOW THE COORDINATES!
       print("CALCULATING THE COORDINATES. ")
       time.sleep(counter)
       print(". ")
       time.sleep(counter)
       print(". ")
       time.sleep(counter)

   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   print("Position Coordinate (m): <%.2f, %.2f, %.2f>" % (JUMPER_HORIZONTAL_DISPLACEMENT, JUMPER_Y_AXIS_DISPLACEMENT,
                                                        JUMPER_VERTICAL_DISPLACEMENT) + "\nNOTE: THIS COORDINATE IS WHEN THE DUDE DEPLOYS THE PARACHUTE! \n")
   print("Velocity Coordinate (m/s): <%.2f, %.2f, %.2f>" % (JUMPER_HORIZONTAL_VELOCITY, JUMPER_Y_AXIS_VELOCITY,
                                                          JUMPER_VERTICAL_VELOCITY) + "\nNOTE: THIS COORDINATE IS WHEN THE DUDE DEPLOYS THE PARACHUTE!\n")
   time.sleep(6)
   print(
   "NOTE: at this point the jumper has pulled the parachute and we will now consider that it takes the jumper 3 seconds to pull the chute and has fallen approximately 60 meters! \n")
   time.sleep(4)

   print("\n")
   OBJECT_HEIGHT = input("Please enter the height of the parachute in meters: \n")
   OBJECT_DIAMETER = input("Please enter the Diameter of the parachute in meters: \n")
   OBJECT_RADIUS = OBJECT_DIAMETER / 2
   print("\n")
   DRAG_CO = .75  # (Constant) drag coefficient of a cone shaped parachute (NO HOLES OR SLITS)
   VELOCITY = mt.sqrt((2 * PERSON_MASS * GRAVITY) / (
       AIR_DENSITY * DRAG_CO * ((PI * OBJECT_RADIUS) * (OBJECT_HEIGHT + OBJECT_RADIUS))))
   print "\n*This is the descent velocity. which means the object will land with and"
   print "is fallling down with this velocity! \n"
   print "*Parachute was opened as soon as the object was thrown out of the plane! \n"
   print "\nMass of the object is: %.2f" % PERSON_MASS, "kg\n"
   print "\nThe final velocity with the variables you entered is: %.2f" % VELOCITY, "m/s"

   time.sleep(3)

   TRIP_TIME_AFTER_PULLING_CHUTE = (JUMPER_VERTICAL_DISPLACEMENT - 60) / VELOCITY
   TOTAL_TRIP_TIME = TRIP_TIME_AFTER_PULLING_CHUTE + 3 + OPENING_PARACHUTE  # We are determining the total time it took to land. after the jumper pulled the chute, time it took to get the chute be fully deployed(3 seconds) and the time when he pulled
   # the chute
   print("The total time of skydive took approximately: %.2f" % TOTAL_TRIP_TIME + " seconds\n")
   time.sleep(4)


   paraPlot(TIME_OF_FLIGHT, JUMPER_VERTICAL_VELOCITY, JUMP_HEIGHT, JUMPER_VERTICAL_DISPLACEMENT, JUMPER_HORIZONTAL_VELOCITY, JUMPER_VERTICAL_VELOCITY, TOTAL_TRIP_TIME)



# Gets the input of the calculated mass of the object from above and solves for descent/terminal velocity for cone shaped parachute!
def calc_cone(Mass_of_Object):
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")
   print("You've chosen to send an OBJECT, with a CONE-shape parachute\n")
   # USER will define the object's mass

   # OBJECT_MASS = input("Please enter the mass of the object: ")
   OBJECT_MASS = Mass_of_Object
   print("\n")
   OBJECT_HEIGHT = input("Please enter the height of the parachute in meters: \n")
   OBJECT_DIAMETER = input("Please enter the Diameter of the parachute in meters: \n")
   OBJECT_RADIUS = OBJECT_DIAMETER / 2
   print("\n")
   DRAG_CO = .75  # (Constant) drag coefficient of a cone shaped parachute (NO HOLES OR SLITS)
   VELOCITY = mt.sqrt((2 * OBJECT_MASS * GRAVITY) / (
   AIR_DENSITY * DRAG_CO * ((PI * OBJECT_RADIUS) * (OBJECT_HEIGHT + OBJECT_RADIUS))))
   print "\n*This is the descent velocity. which means the object will land with and"
   print "is fallling down with this velocity! \n"
   print "*Parachute was opened as soon as the object was thrown out of the plane! \n"
   print "\nMass of the object is: %.2f" % OBJECT_MASS, "kg\n"
   print "\nThe final velocity with the variables you entered is: %.2f" % VELOCITY, "m/s"










def person_object_DOME():

   a = "Person"
   b = "Object"

   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   print("Is this parachute launch for an Object or Person?\n")
   print("a) Person")
   print("b) Object\n")

   Selected_choice = raw_input("Valid input should be 'a' or 'b' \n")

   while True:
       if Selected_choice == "a" or Selected_choice == "A":
           pweight = raw_input("\nWhat is the weight of the person(lb)?\n")
           P_Weight = float(pweight)
           P_slugAns = (P_Weight) / (GRAVITY)
           PersonMass = P_slugAns * 14.5939

           calc_person_dome(PersonMass)
           break
       elif Selected_choice == "b" or Selected_choice == "B":
           ooWeight = raw_input("What is the weight of the object (lb)? \n")
           Weight = float(ooWeight)
           slugAns = (Weight) / (GRAVITY)  # Pounds divided by accerlation(m/s**2) is a unit called slug
           ObjectMass = slugAns * 14.5939  # Converting slugs to mass

           calc_dome(ObjectMass)
           break

       else:

           time.sleep(2)
           print "\nError! ENTER A VALID CHOICE!\n"
           del Selected_choice
           print("Is this parachute launch for an Object or Person?\n")
           print("a) Person")
           print("b) Object\n")
           Selected_choice = raw_input("Valid input should be 'a' or 'b' \n")
           continue

#SENDING DOWN A PERSON WITH A DOME SHAPED PARACHUTE!
def calc_person_dome(Mass_Of_Person):
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   print("\nYou've chosen to simulate a PERSON skydiving, with a DOME-shape parachute. This is more complicated than sending an object,")
   print("YOU WILL BE ASKED ALOT OF QUESTIONS!.\n")
   time.sleep(3)
   PERSON_MASS = Mass_Of_Person

   while True:
       PLANE_MOVEMENT = raw_input("Does the plane that the jumper is jumping from have a initial velocity to consider for? (y/n) \nNOTE: This is a simulation so it's okay to say 'n' \n")
       if (PLANE_MOVEMENT == "y" or PLANE_MOVEMENT=="Y"):
           PLANE_SPEED = input("What is the velocity of the plane(Along Y-axis) (m/s)? \n")
           break
       elif(PLANE_MOVEMENT == "n" or PLANE_MOVEMENT == "N"):
           PLANE_SPEED = 0
           break
       else:
           print("NOT A VALID INPUT! ")
           print("\n")

   #Asking if there is any vertical velocity prior to jumping for example if the jumper has a running start jumping down
   while True:
       VERTICAL_VELOCITY_INITIAL_QUESTION = raw_input("Does the jumper have an initial VERTICAL(Z-axis) velocity?(y/n) \n")

       if(VERTICAL_VELOCITY_INITIAL_QUESTION == "y" or VERTICAL_VELOCITY_INITIAL_QUESTION == "Y"):
           VERTICAL_VELOCITY_INITIAL = input("What is the initial VERTICAL(Z-axis) velocity of the jumper (m/s)? \n")
           break
       elif(VERTICAL_VELOCITY_INITIAL_QUESTION == "n" or VERTICAL_VELOCITY_INITIAL_QUESTION == "N"):
           VERTICAL_VELOCITY_INITIAL = 0
           break
       else:
           print("NOT A VALID ANSWER! \n")
           print("\n")

   # Asking if there is any horizontal velocity prior to jumping for example if the jumper has a running start
   while True:
       HORIZONTAL_VELOCITY_INITIAL_QUESTION = raw_input("Does the jumper have an initial HORIZONTAL(X-axis) velocity?(y/n) \n")
       if (HORIZONTAL_VELOCITY_INITIAL_QUESTION == "y" or HORIZONTAL_VELOCITY_INITIAL_QUESTION == "Y"):
            HORIZONTAL_VELOCITY_INITIAL = input("What is the initial HORIZONTAL(X-axis) velocity of the jumper (m/s)? \n")
            break
       elif (HORIZONTAL_VELOCITY_INITIAL_QUESTION == "n" or HORIZONTAL_VELOCITY_INITIAL_QUESTION == "N"):
           HORIZONTAL_VELOCITY_INITIAL = 0
           break
       else:
           print("NOT A VALID ANSWER! \n")
           print("\n")

   while True:
      try:
           JUMP_HEIGHT= float(raw_input("\nWhat height does the jumper decide to jump from (meters)?\nNOTE: If you enter '0' then the default height is 4000m\n"))
           if (JUMP_HEIGHT == 0):
               JUMP_HEIGHT=4000
               break
           elif(JUMP_HEIGHT<0):
               print("The maximum height cannot be less than zero! \n")
               print("\n")
           elif(JUMP_HEIGHT>0):
               break
           else:
               print("NOT A VALID ANSWER! \n")
      except ValueError:
          print("\nThat was not a number, Please enter a number! \n")

   TIME_OF_FLIGHT=mt.sqrt((JUMP_HEIGHT)/(HALF_GRAVITY))
   print("Your flight lasts: %.2f" %TIME_OF_FLIGHT + " seconds\nNOTE: This flight time is if the jumper does not open the parachute! \n")
   #print("Please select the time your simulated jumper decides to open the parachute, your range is from: [0-%.2f] " %TIME_OF_FLIGHT)
   #print("\n")

   while True:
    try:
       OPENING_PARACHUTE = float(raw_input("Please select the time (in seconds) your simulated jumper decides to open the parachute, your range is from: [0-%.2f] " %TIME_OF_FLIGHT))
       print("\n")
       if (OPENING_PARACHUTE < TIME_OF_FLIGHT and OPENING_PARACHUTE > 0):
            break
       else:
           print("ERROR, Number not in range! \n")
    except ValueError:
       print("\nThat was not a number, Please enter a number! \n")

    try:
        os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
    except Exception:
        print("Unexpected Operating System!\n")


   JUMPER_HORIZONTAL_DISPLACEMENT = HORIZONTAL_VELOCITY_INITIAL * OPENING_PARACHUTE  # X-coordinate point for position when the parachute dude deployed his/her parachute!
   print("Your parachute dude's horizontal displacement position relative to the origin (plane): %.2f" % JUMPER_HORIZONTAL_DISPLACEMENT + "m \n")  # X-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_HORIZONTAL_VELOCITY = HORIZONTAL_VELOCITY_INITIAL  # X-coordinate point for velocity
   print("Your parachute dude's horizontal velocity before the parachute is deployed is approximately: %.2f" % JUMPER_HORIZONTAL_VELOCITY + "m/s \n")  # X-coordinate point for velocity
   print("NOTE: This is because there is no acceleration in the x-axis \n")

   JUMPER_Y_AXIS_DISPLACEMENT = PLANE_SPEED*OPENING_PARACHUTE # Y-coordinate point for position when the parachute dude deployed his/her parachute!
   print("Your parachute dude's y-direction displacement is (due to plane's speed): %.2f" %JUMPER_Y_AXIS_DISPLACEMENT + "m\n") # Y-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_Y_AXIS_VELOCITY = PLANE_SPEED # Y-coordinate point for velocity
   print( "Your parachute dude's y-direction velocity is (due to plane's speed): %.2f" % JUMPER_Y_AXIS_VELOCITY + "m/s\n") # Y-coordinate point for velocity


   JUMPER_VERTICAL_DISPLACEMENT =  JUMP_HEIGHT + (VERTICAL_VELOCITY_INITIAL*OPENING_PARACHUTE) - (HALF_GRAVITY*OPENING_PARACHUTE**2) # Z-coordinate point for position when the parachute dude deployed his/her parachute!
   print("Your parachute dude's vertical displacement position relative to the initial position is: %.2f" %JUMPER_VERTICAL_DISPLACEMENT + "m \n") # Z-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_VERTICAL_VELOCITY = VERTICAL_VELOCITY_INITIAL - (GRAVITY*OPENING_PARACHUTE) #Z-coordinate point for velocity
   print("Your parachute dude's vertical velocity before the parachute is deployed is approximately: %.2f" % JUMPER_VERTICAL_VELOCITY + "m/s \n") #Z-coordinate point for velocity

   time.sleep(6) #Making the python sleep for about 6 seconds, this is so that the user doesn't get bombarded with more incoming information, 4 seconds is enough to digest information before being thrown another screen

   for counter in range(0, 3, 1): #THE COORDINATES ARE ALREADY CALCULATED BUT IT SLEEPS FOR UNTIL WHEN COUTNER HITS 3 SECONDS AND THEN PROCEEDS TO SHOW THE COORDINATES!
       print("CALCULATING THE COORDINATES. ")
       time.sleep(counter)
       print(". ")
       time.sleep(counter)
       print(". ")
       time.sleep(counter)

   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   print("Position Coordinate (m): <%.2f, %.2f, %.2f>" %(JUMPER_HORIZONTAL_DISPLACEMENT,JUMPER_Y_AXIS_DISPLACEMENT,JUMPER_VERTICAL_DISPLACEMENT) + "\nNOTE: THIS COORDINATE IS WHEN THE DUDE DEPLOYS THE PARACHUTE! \n")
   print("Velocity Coordinate (m/s): <%.2f, %.2f, %.2f>" %(JUMPER_HORIZONTAL_VELOCITY, JUMPER_Y_AXIS_VELOCITY, JUMPER_VERTICAL_VELOCITY) + "\nNOTE: THIS COORDINATE IS WHEN THE DUDE DEPLOYS THE PARACHUTE!\n")
   time.sleep(6)
   print("NOTE: at this point the jumper has pulled the parachute and we will now consider that it takes the jumper 3 seconds to pull the chute and has fallen approximately 60 meters! \n")
   time.sleep(4)


   print("\n")
   OBJECT_DIAMETER = input("Please enter the diameter of the parachute: ")
   print("\n")
   # GRAVITY = 9.789337 #Value of gravity in the DC area
   # PI = 3.14159  #(constant) value of pi
   # AIR_DENSITY = 1.22 #(constant) air density: kg/m^3
   DRAG_CO = 1.5  # (Constant) drag coefficient of a true dome shaped parachute
   VELOCITY = mt.sqrt((8 * PERSON_MASS * GRAVITY) / (PI * AIR_DENSITY * DRAG_CO * (OBJECT_DIAMETER ** 2)))
   print "\n*This is the descent velocity. which means the jumper will land with and"
   print "is fallling down with this velocity after pulling the parachute! \n"
   print "\nMass of the jumper is: %.2f" % PERSON_MASS, "kg\n"
   print "The final velocity with the variables you entered is: %.2f" % VELOCITY, "m/s\n"
   print("\nNOTE: This is the maximum speed the jumper will reach after pulling the chute! \n")
   time.sleep(3)

   TRIP_TIME_AFTER_PULLING_CHUTE = (JUMPER_VERTICAL_DISPLACEMENT - 60) / VELOCITY
   TOTAL_TRIP_TIME = TRIP_TIME_AFTER_PULLING_CHUTE + 3 + OPENING_PARACHUTE  # We are determining the total time it took to land. after the jumper pulled the chute, time it took to get the chute be fully deployed(3 seconds) and the time when he pulled
   # the chute
   print("The total time of skydive took approximately: %.2f" % TOTAL_TRIP_TIME + " seconds\n")
   time.sleep(4)

   paraPlot(TIME_OF_FLIGHT, JUMPER_VERTICAL_VELOCITY, JUMP_HEIGHT, JUMPER_VERTICAL_DISPLACEMENT,
            JUMPER_HORIZONTAL_VELOCITY, JUMPER_VERTICAL_VELOCITY, TOTAL_TRIP_TIME)


# Gets the input of the calculated mass of the object from above and solves for descent/terminal velocity for dome shaped parachute!
def calc_dome(Mass_of_Object):
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")
   print("You've chosen to send an OBJECT, with a DOME-shape parachute, and NO holes.\n")
   # USER will define the object's mass

   # OBJECT_MASS = input("Please enter the mass of the object: ")
   OBJECT_MASS = Mass_of_Object
   print("\n")
   OBJECT_DIAMETER = input("Please enter the diameter of the parachute: ")
   print("\n")
   # GRAVITY = 9.789337 #Value of gravity in the DC area
   # PI = 3.14159  #(constant) value of pi
   # AIR_DENSITY = 1.22 #(constant) air density: kg/m^3
   DRAG_CO = 1.5  # (Constant) drag coefficient of a true dome shaped parachute
   VELOCITY = mt.sqrt((8 * OBJECT_MASS * GRAVITY) / (PI * AIR_DENSITY * DRAG_CO * (OBJECT_DIAMETER ** 2)))
   print "\n*This is the descent velocity. which means the object will land with and"
   print "is fallling down with this velocity! \n"
   print "*Parachute was opened as soon as the object was thrown out of the plane! \n"
   print "\nMass of the object is: %.2f" % OBJECT_MASS, "kg\n"
   print "The final velocity with the variables you entered is: %.2f" % VELOCITY, "m/s\n"


# Calculates person_object_velocity for rectangle shaped pararchutes
def person_object_RECTANGLE():
   a = "Person"
   b = "Object"

   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")
   print("Is this parachute launch for an Object or Person?\n")
   print("a) Person")
   print("b) Object\n")

   Selected_choice = raw_input("Valid input should be 'a' or 'b' \n")

   while True:
       if Selected_choice == "a" or Selected_choice == "A":
           pweight = raw_input("\nWhat is the weight of the person(lb)?\n")
           P_Weight = float(pweight)
           P_slugAns = (P_Weight) / (GRAVITY)
           PersonMass = P_slugAns * 14.5939

           calc_person_rectangle(PersonMass)
           break
       elif Selected_choice == "b" or Selected_choice == "B":
           ooWeight = raw_input("What is the weight of the object (lb)? \n")
           Weight = float(ooWeight)
           slugAns = (Weight) / (GRAVITY)  # Pounds divided by accerlation(m/s**2) is a unit called slug
           ObjectMass = slugAns * 14.5939  # Converting slugs to mass

           calc_rectangle(ObjectMass)
           break

       else:

           time.sleep(2)
           print "\nError! ENTER A VALID CHOICE!\n"
           del Selected_choice
           print("Is this parachute launch for an Object or Person?\n")
           print("a) Person")
           print("b) Object\n")
           Selected_choice = raw_input("Valid input should be 'a' or 'b' \n")
           continue

#SENDING DOWN A PERSON WITH A RECTANGLE SHAPED PARACHUTE!
def calc_person_rectangle(Mass_Of_Person):
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   print("\nYou've chosen to simulate a PERSON skydiving, with a RECTANGLE-shape parachute. This is more complicated than sending an object,")
   print("YOU WILL BE ASKED ALOT OF QUESTIONS!.\n")
   time.sleep(3)
   PERSON_MASS = Mass_Of_Person

   while True:
       PLANE_MOVEMENT = raw_input("Does the plane that the jumper is jumping from have a initial velocity to consider for? (y/n) \nNOTE: This is a simulation so it's okay to say 'n' \n")
       if (PLANE_MOVEMENT == "y" or PLANE_MOVEMENT=="Y"):
           PLANE_SPEED = input("What is the velocity of the plane(Along Y-axis) (m/s)? \n")
           break
       elif(PLANE_MOVEMENT == "n" or PLANE_MOVEMENT == "N"):
           PLANE_SPEED = 0
           break
       else:
           print("NOT A VALID INPUT! ")
           print("\n")

   #Asking if there is any vertical velocity prior to jumping for example if the jumper has a running start jumping down
   while True:
       VERTICAL_VELOCITY_INITIAL_QUESTION = raw_input("Does the jumper have an initial VERTICAL(Z-axis) velocity?(y/n) \n")

       if(VERTICAL_VELOCITY_INITIAL_QUESTION == "y" or VERTICAL_VELOCITY_INITIAL_QUESTION == "Y"):
           VERTICAL_VELOCITY_INITIAL = input("What is the initial VERTICAL(Z-axis) velocity of the jumper (m/s)? \n")
           break
       elif(VERTICAL_VELOCITY_INITIAL_QUESTION == "n" or VERTICAL_VELOCITY_INITIAL_QUESTION == "N"):
           VERTICAL_VELOCITY_INITIAL = 0
           break
       else:
           print("NOT A VALID ANSWER! \n")
           print("\n")

   # Asking if there is any horizontal velocity prior to jumping for example if the jumper has a running start
   while True:
       HORIZONTAL_VELOCITY_INITIAL_QUESTION = raw_input("Does the jumper have an initial HORIZONTAL(X-axis) velocity?(y/n) \n")
       if (HORIZONTAL_VELOCITY_INITIAL_QUESTION == "y" or HORIZONTAL_VELOCITY_INITIAL_QUESTION == "Y"):
            HORIZONTAL_VELOCITY_INITIAL = input("What is the initial HORIZONTAL(X-axis) velocity of the jumper (m/s)? \n")
            break
       elif (HORIZONTAL_VELOCITY_INITIAL_QUESTION == "n" or HORIZONTAL_VELOCITY_INITIAL_QUESTION == "N"):
           HORIZONTAL_VELOCITY_INITIAL = 0
           break
       else:
           print("NOT A VALID ANSWER! \n")
           print("\n")

   while True:
      try:
           JUMP_HEIGHT= float(raw_input("\nWhat height does the jumper decide to jump from (meters)?\nNOTE: If you enter '0' then the default height is 4000m\n"))
           if (JUMP_HEIGHT == 0):
               JUMP_HEIGHT=4000
               break
           elif(JUMP_HEIGHT<0):
               print("The maximum height cannot be less than zero! \n")
               print("\n")
           elif(JUMP_HEIGHT>0):
               break
           else:
               print("NOT A VALID ANSWER! \n")
      except ValueError:
          print("\nThat was not a number, Please enter a number! \n")

   TIME_OF_FLIGHT=mt.sqrt((JUMP_HEIGHT)/(HALF_GRAVITY))
   print("Your flight lasts: %.2f" %TIME_OF_FLIGHT + " seconds\nNOTE: This flight time is if the jumper does not open the parachute! \n")
   #print("Please select the time your simulated jumper decides to open the parachute, your range is from: [0-%.2f] " %TIME_OF_FLIGHT)
   #print("\n")

   while True:
    try:
       OPENING_PARACHUTE = float(raw_input("Please select the time (in seconds) your simulated jumper decides to open the parachute, your range is from: [0-%.2f] " %TIME_OF_FLIGHT))
       print("\n")
       if (OPENING_PARACHUTE < TIME_OF_FLIGHT and OPENING_PARACHUTE > 0):
            break
       else:
           print("ERROR, Number not in range! \n")
    except ValueError:
       print("\nThat was not a number, Please enter a number! \n")

   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   JUMPER_HORIZONTAL_DISPLACEMENT = HORIZONTAL_VELOCITY_INITIAL * OPENING_PARACHUTE  # X-coordinate point for position when the parachute dude deployed his/her parachute!
   print("Your parachute dude's horizontal displacement position relative to the origin (plane): %.2f" % JUMPER_HORIZONTAL_DISPLACEMENT + "m \n")  # X-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_HORIZONTAL_VELOCITY = HORIZONTAL_VELOCITY_INITIAL  # X-coordinate point for velocity
   print("Your parachute dude's horizontal velocity before the parachute is deployed is approximately: %.2f" % JUMPER_HORIZONTAL_VELOCITY + "m/s \n")  # X-coordinate point for velocity
   print("NOTE: This is because there is no acceleration in the x-axis \n")

   JUMPER_Y_AXIS_DISPLACEMENT = PLANE_SPEED*OPENING_PARACHUTE # Y-coordinate point for position when the parachute dude deployed his/her parachute!
   print("Your parachute dude's y-direction displacement is (due to plane's speed): %.2f" %JUMPER_Y_AXIS_DISPLACEMENT + "m\n") # Y-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_Y_AXIS_VELOCITY = PLANE_SPEED # Y-coordinate point for velocity
   print( "Your parachute dude's y-direction velocity is (due to plane's speed): %.2f" % JUMPER_Y_AXIS_VELOCITY + "m/s\n") # Y-coordinate point for velocity


   JUMPER_VERTICAL_DISPLACEMENT =  JUMP_HEIGHT + (VERTICAL_VELOCITY_INITIAL*OPENING_PARACHUTE) - (HALF_GRAVITY*OPENING_PARACHUTE**2) # Z-coordinate point for position when the parachute dude deployed his/her parachute!
   print("Your parachute dude's vertical displacement position relative to the initial position is: %.2f" %JUMPER_VERTICAL_DISPLACEMENT + "m \n") # Z-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_VERTICAL_VELOCITY = VERTICAL_VELOCITY_INITIAL - (GRAVITY*OPENING_PARACHUTE) #Z-coordinate point for velocity
   print("Your parachute dude's vertical velocity before the parachute is deployed is approximately: %.2f" % JUMPER_VERTICAL_VELOCITY + "m/s \n") #Z-coordinate point for velocity

   time.sleep(6) #Making the python sleep for about 6 seconds, this is so that the user doesn't get bombarded with more incoming information, 4 seconds is enough to digest information before being thrown another screen

   for counter in range(0, 3, 1): #THE COORDINATES ARE ALREADY CALCULATED BUT IT SLEEPS FOR UNTIL WHEN COUTNER HITS 3 SECONDS AND THEN PROCEEDS TO SHOW THE COORDINATES!
       print("CALCULATING THE COORDINATES. ")
       time.sleep(counter)
       print(". ")
       time.sleep(counter)
       print(". ")
       time.sleep(counter)

   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   print("Position Coordinate (m): <%.2f, %.2f, %.2f>" %(JUMPER_HORIZONTAL_DISPLACEMENT,JUMPER_Y_AXIS_DISPLACEMENT,JUMPER_VERTICAL_DISPLACEMENT) + "\nNOTE: THIS COORDINATE IS WHEN THE DUDE DEPLOYS THE PARACHUTE! \n")
   print("Velocity Coordinate (m/s): <%.2f, %.2f, %.2f>" %(JUMPER_HORIZONTAL_VELOCITY, JUMPER_Y_AXIS_VELOCITY, JUMPER_VERTICAL_VELOCITY) + "\nNOTE: THIS COORDINATE IS WHEN THE DUDE DEPLOYS THE PARACHUTE!\n")
   time.sleep(6)
   print("NOTE: at this point the jumper has pulled the parachute and we will now consider that it takes the jumper 3 seconds to pull the chute and has fallen approximately 60 meters! \n")
   time.sleep(4)

   print("\n")
   OBJECT_LENGTH = input("Please enter the length of the parachute in meters: \n")
   OBJECT_WIDTH = input("Please enter the width of the parachute in meters: \n")
   print("\n")
   DRAG_CO = .75  # (Constant) drag coefficient of a rectangle shaped parachute(NO HOLES OR SLITS)
   VELOCITY = mt.sqrt((2 * PERSON_MASS * GRAVITY) / (AIR_DENSITY * DRAG_CO * ((OBJECT_LENGTH) * (OBJECT_WIDTH))))
   print "\n*This is the descent velocity. which means the jumper will land with and"
   print "is fallling down with this velocity! \n"
   print "\nMass of the jumper is: %.2f" % PERSON_MASS, "kg\n"
   time.sleep(2)
   print "\nThe terminal velocity with the variables you entered is: %.2f" % VELOCITY, "m/s"
   print("\nNOTE: This is the maximum speed the jumper will reach after pulling the chute! \n")
   time.sleep(3)

   TRIP_TIME_AFTER_PULLING_CHUTE=(JUMPER_VERTICAL_DISPLACEMENT-60)/VELOCITY
   TOTAL_TRIP_TIME= TRIP_TIME_AFTER_PULLING_CHUTE + 3 + OPENING_PARACHUTE #We are determining the total time it took to land. after the jumper pulled the chute, time it took to get the chute be fully deployed(3 seconds) and the time when he pulled
   # the chute
   print("The total time of skydive took approximately: %.2f" %TOTAL_TRIP_TIME + " seconds\n")
   time.sleep(4)


   paraPlot(TIME_OF_FLIGHT,JUMPER_VERTICAL_VELOCITY,JUMP_HEIGHT, JUMPER_VERTICAL_DISPLACEMENT, JUMPER_HORIZONTAL_VELOCITY, JUMPER_VERTICAL_VELOCITY,TOTAL_TRIP_TIME)



# Gets the input of the calculated mass of the object from above and solves for descent/terminal velocity for rectangle shaped parachute!
def calc_rectangle(Mass_of_Object):
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")
   print("You've chosen to send an OBJECT, with a RECTANGLE-shape parachute\n")
   # USER will define the object's mass

   # OBJECT_MASS = input("Please enter the mass of the object: ")
   OBJECT_MASS = Mass_of_Object
   print("\n")
   OBJECT_LENGTH = input("Please enter the length of the parachute in meters: \n")
   OBJECT_WIDTH = input("Please enter the width of the parachute in meters: \n")
   print("\n")
   DRAG_CO = .75  # (Constant) drag coefficient of a rectangle shaped parachute(NO HOLES OR SLITS)
   VELOCITY = mt.sqrt((2 * OBJECT_MASS * GRAVITY) / (AIR_DENSITY * DRAG_CO * ((OBJECT_LENGTH) * (OBJECT_WIDTH))))
   print "\n*This is the descent velocity. which means the object will land with and"
   print "is fallling down with this velocity! \n"
   print "*Parachute was opened as soon as the object was thrown out of the plane! \n"
   print "\nMass of the object is: %.2f" % OBJECT_MASS, "kg\n"
   print "\nThe final velocity with the variables you entered is: %.2f" % VELOCITY, "m/s"




# Calculates person_object_velocity for cylinder shaped pararchutes
def person_object_CYLINDER():
   a = "Person"
   b = "Object"

   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   print("Is this parachute launch for an Object or Person?\n")
   print("a) Person")
   print("b) Object\n")

   Selected_choice = raw_input("Valid input should be 'a' or 'b' \n")

   while True:
       if Selected_choice == "a" or Selected_choice == "A":
           pweight = raw_input("\nWhat is the weight of the person(lb)?\n")
           P_Weight = float(pweight)
           P_slugAns = (P_Weight) / (GRAVITY)
           PersonMass = P_slugAns * 14.5939

           calc_person_cylinder(PersonMass)
           break
       elif Selected_choice == "b" or Selected_choice == "B":
           ooWeight = raw_input("What is the weight of the object (lb)? \n")
           Weight = float(ooWeight)
           slugAns = (Weight) / (GRAVITY)  # Pounds divided by accerlation(m/s**2) is a unit called slug
           ObjectMass = slugAns * 14.5939  # Converting slugs to mass

           calc_cylinder(ObjectMass)
           break

       else:

           time.sleep(2)
           print "\nError! ENTER A VALID CHOICE!\n"
           del Selected_choice
           print("Is this parachute launch for an Object or Person?\n")
           print("a) Person")
           print("b) Object\n")
           Selected_choice = raw_input("Valid input should be 'a' or 'b' \n")
           continue

#SENDING DOWN A PERSON WITH A CYLINDER SHAPED PARACHUTE!
def calc_person_cylinder(Mass_Of_Person):
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   print(
       "\nYou've chosen to simulate a PERSON skydiving, with a RECTANGLE-shape parachute. This is more complicated than sending an object,")
   print("YOU WILL BE ASKED ALOT OF QUESTIONS!.\n")
   time.sleep(3)
   PERSON_MASS = Mass_Of_Person

   while True:
       PLANE_MOVEMENT = raw_input(
           "Does the plane that the jumper is jumping from have a initial velocity to consider for? (y/n) \nNOTE: This is a simulation so it's okay to say 'n' \n")
       if (PLANE_MOVEMENT == "y" or PLANE_MOVEMENT == "Y"):
           PLANE_SPEED = input("What is the velocity of the plane(Along Y-axis) (m/s)? \n")
           break
       elif (PLANE_MOVEMENT == "n" or PLANE_MOVEMENT == "N"):
           PLANE_SPEED = 0
           break
       else:
           print("NOT A VALID INPUT! ")
           print("\n")

   # Asking if there is any vertical velocity prior to jumping for example if the jumper has a running start jumping down
   while True:
       VERTICAL_VELOCITY_INITIAL_QUESTION = raw_input(
           "Does the jumper have an initial VERTICAL(Z-axis) velocity?(y/n) \n")

       if (VERTICAL_VELOCITY_INITIAL_QUESTION == "y" or VERTICAL_VELOCITY_INITIAL_QUESTION == "Y"):
           VERTICAL_VELOCITY_INITIAL = input("What is the initial VERTICAL(Z-axis) velocity of the jumper (m/s)? \n")
           break
       elif (VERTICAL_VELOCITY_INITIAL_QUESTION == "n" or VERTICAL_VELOCITY_INITIAL_QUESTION == "N"):
           VERTICAL_VELOCITY_INITIAL = 0
           break
       else:
           print("NOT A VALID ANSWER! \n")
           print("\n")

   # Asking if there is any horizontal velocity prior to jumping for example if the jumper has a running start
   while True:
       HORIZONTAL_VELOCITY_INITIAL_QUESTION = raw_input(
           "Does the jumper have an initial HORIZONTAL(X-axis) velocity?(y/n) \n")
       if (HORIZONTAL_VELOCITY_INITIAL_QUESTION == "y" or HORIZONTAL_VELOCITY_INITIAL_QUESTION == "Y"):
           HORIZONTAL_VELOCITY_INITIAL = input(
               "What is the initial HORIZONTAL(X-axis) velocity of the jumper (m/s)? \n")
           break
       elif (HORIZONTAL_VELOCITY_INITIAL_QUESTION == "n" or HORIZONTAL_VELOCITY_INITIAL_QUESTION == "N"):
           HORIZONTAL_VELOCITY_INITIAL = 0
           break
       else:
           print("NOT A VALID ANSWER! \n")
           print("\n")

   while True:
       try:
           JUMP_HEIGHT = float(raw_input(
               "\nWhat height does the jumper decide to jump from (meters)?\nNOTE: If you enter '0' then the default height is 4000m\n"))
           if (JUMP_HEIGHT == 0):
               JUMP_HEIGHT = 4000
               break
           elif (JUMP_HEIGHT < 0):
               print("The maximum height cannot be less than zero! \n")
               print("\n")
           elif (JUMP_HEIGHT > 0):
               break
           else:
               print("NOT A VALID ANSWER! \n")
       except ValueError:
           print("\nThat was not a number, Please enter a number! \n")

   TIME_OF_FLIGHT = mt.sqrt((JUMP_HEIGHT) / (HALF_GRAVITY))
   print(
       "Your flight lasts: %.2f" % TIME_OF_FLIGHT + " seconds\nNOTE: This flight time is if the jumper does not open the parachute! \n")
   # print("Please select the time your simulated jumper decides to open the parachute, your range is from: [0-%.2f] " %TIME_OF_FLIGHT)
   # print("\n")

   while True:
       try:
           OPENING_PARACHUTE = float(raw_input(
               "Please select the time (in seconds) your simulated jumper decides to open the parachute, your range is from: [0-%.2f] " % TIME_OF_FLIGHT))
           print("\n")
           if (OPENING_PARACHUTE < TIME_OF_FLIGHT and OPENING_PARACHUTE > 0):
               break
           else:
               print("ERROR, Number not in range! \n")
       except ValueError:
           print("\nThat was not a number, Please enter a number! \n")

   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   JUMPER_HORIZONTAL_DISPLACEMENT = HORIZONTAL_VELOCITY_INITIAL * OPENING_PARACHUTE  # X-coordinate point for position when the parachute dude deployed his/her parachute!
   print(
       "Your parachute dude's horizontal displacement position relative to the origin (plane): %.2f" % JUMPER_HORIZONTAL_DISPLACEMENT + "m \n")  # X-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_HORIZONTAL_VELOCITY = HORIZONTAL_VELOCITY_INITIAL  # X-coordinate point for velocity
   print(
       "Your parachute dude's horizontal velocity before the parachute is deployed is approximately: %.2f" % JUMPER_HORIZONTAL_VELOCITY + "m/s \n")  # X-coordinate point for velocity
   print("NOTE: This is because there is no acceleration in the x-axis \n")

   JUMPER_Y_AXIS_DISPLACEMENT = PLANE_SPEED * OPENING_PARACHUTE  # Y-coordinate point for position when the parachute dude deployed his/her parachute!
   print(
       "Your parachute dude's y-direction displacement is (due to plane's speed): %.2f" % JUMPER_Y_AXIS_DISPLACEMENT + "m\n")  # Y-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_Y_AXIS_VELOCITY = PLANE_SPEED  # Y-coordinate point for velocity
   print(
       "Your parachute dude's y-direction velocity is (due to plane's speed): %.2f" % JUMPER_Y_AXIS_VELOCITY + "m/s\n")  # Y-coordinate point for velocity

   JUMPER_VERTICAL_DISPLACEMENT = JUMP_HEIGHT + (VERTICAL_VELOCITY_INITIAL * OPENING_PARACHUTE) - (
       HALF_GRAVITY * OPENING_PARACHUTE ** 2)  # Z-coordinate point for position when the parachute dude deployed his/her parachute!
   print(
       "Your parachute dude's vertical displacement position relative to the initial position is: %.2f" % JUMPER_VERTICAL_DISPLACEMENT + "m \n")  # Z-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_VERTICAL_VELOCITY = VERTICAL_VELOCITY_INITIAL - (
       GRAVITY * OPENING_PARACHUTE)  # Z-coordinate point for velocity
   print(
       "Your parachute dude's vertical velocity before the parachute is deployed is approximately: %.2f" % JUMPER_VERTICAL_VELOCITY + "m/s \n")  # Z-coordinate point for velocity

   time.sleep(
       6)  # Making the python sleep for about 6 seconds, this is so that the user doesn't get bombarded with more incoming information, 4 seconds is enough to digest information before being thrown another screen

   for counter in range(0, 3,
                        1):  # THE COORDINATES ARE ALREADY CALCULATED BUT IT SLEEPS FOR UNTIL WHEN COUTNER HITS 3 SECONDS AND THEN PROCEEDS TO SHOW THE COORDINATES!
       print("CALCULATING THE COORDINATES. ")
       time.sleep(counter)
       print(". ")
       time.sleep(counter)
       print(". ")
       time.sleep(counter)
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   print("Position Coordinate (m): <%.2f, %.2f, %.2f>" % (JUMPER_HORIZONTAL_DISPLACEMENT, JUMPER_Y_AXIS_DISPLACEMENT,
                                                        JUMPER_VERTICAL_DISPLACEMENT) + "\nNOTE: THIS COORDINATE IS WHEN THE DUDE DEPLOYS THE PARACHUTE! \n")
   print("Velocity Coordinate (m/s): <%.2f, %.2f, %.2f>" % (JUMPER_HORIZONTAL_VELOCITY, JUMPER_Y_AXIS_VELOCITY,
                                                          JUMPER_VERTICAL_VELOCITY) + "\nNOTE: THIS COORDINATE IS WHEN THE DUDE DEPLOYS THE PARACHUTE!\n")
   time.sleep(6)
   print(
       "NOTE: at this point the jumper has pulled the parachute and we will now consider that it takes the jumper 3 seconds to pull the chute and has fallen approximately 60 meters! \n")
   time.sleep(4)

   print("\n")
   OBJECT_HEIGHT = input("Please enter the height of the parachute in meters: \n")
   OBJECT_DIAMETER = input("Please enter the Diameter of the parachute in meters: \n")
   OBJECT_RADIUS = OBJECT_DIAMETER / 2
   print("\n")
   DRAG_CO = .75  # (Constant) drag coefficient of a cylinder shaped parachute (NO HOLES OR SLITS)
   VELOCITY = mt.sqrt(
       (PERSON_MASS * GRAVITY) / (AIR_DENSITY * DRAG_CO * ((PI * OBJECT_RADIUS) * (OBJECT_HEIGHT + OBJECT_RADIUS))))
   print "\n*This is the descent velocity. which means the jumper will land with and"
   print "is fallling down with this velocity! \n"
   print "\nMass of the jumper is: %.2f" % PERSON_MASS, "kg\n"
   print "\nThe final velocity with the variables you entered is: %.2f" % VELOCITY, "m/s"

   time.sleep(3)

   TRIP_TIME_AFTER_PULLING_CHUTE = (JUMPER_VERTICAL_DISPLACEMENT - 60) / VELOCITY
   TOTAL_TRIP_TIME = TRIP_TIME_AFTER_PULLING_CHUTE + 3 + OPENING_PARACHUTE  # We are determining the total time it took to land. after the jumper pulled the chute, time it took to get the chute be fully deployed(3 seconds) and the time when he pulled
   # the chute
   print("The total time of skydive took approximately: %.2f" % TOTAL_TRIP_TIME + " seconds\n")
   time.sleep(4)

   paraPlot(TIME_OF_FLIGHT, JUMPER_VERTICAL_VELOCITY, JUMP_HEIGHT, JUMPER_VERTICAL_DISPLACEMENT,
           JUMPER_HORIZONTAL_VELOCITY, JUMPER_VERTICAL_VELOCITY, TOTAL_TRIP_TIME)




# Gets the input of the calculated mass of the object from above and solves for descent/terminal velocity for cylinder shaped parachute!
def calc_cylinder(Mass_of_Object):
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")
   print("You've chosen to send an OBJECT, with a CYLINDER-shape parachute\n")
   # USER will define the object's mass

   # OBJECT_MASS = input("Please enter the mass of the object: ")
   OBJECT_MASS = Mass_of_Object
   print("\n")
   OBJECT_HEIGHT = input("Please enter the height of the parachute in meters: \n")
   OBJECT_DIAMETER = input("Please enter the Diameter of the parachute in meters: \n")
   OBJECT_RADIUS = OBJECT_DIAMETER / 2
   print("\n")
   DRAG_CO = .75  # (Constant) drag coefficient of a cylinder shaped parachute (NO HOLES OR SLITS)
   VELOCITY = mt.sqrt(
       (OBJECT_MASS * GRAVITY) / (AIR_DENSITY * DRAG_CO * ((PI * OBJECT_RADIUS) * (OBJECT_HEIGHT + OBJECT_RADIUS))))
   print "\n*This is the descent velocity. which means the object will land with and"
   print "is fallling down with this velocity! \n"
   print "*Parachute was opened as soon as the object was thrown out of the plane! \n"
   print "\nMass of the object is: %.2f" % OBJECT_MASS, "kg\n"
   print "\nThe final velocity with the variables you entered is: %.2f" % VELOCITY, "m/s"


# Calculates person_object_velocity for cuboid shaped pararchutes
def person_object_CUBOID():
   a = "Person"
   b = "Object"

   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   print("Is this parachute launch for an Object or Person?\n")
   print("a) Person")
   print("b) Object\n")

   Selected_choice = raw_input("Valid input should be 'a' or 'b' \n")

   while True:
       if Selected_choice == "a" or Selected_choice == "A":
           pweight = raw_input("\nWhat is the weight of the person(lb)?\n")
           P_Weight = float(pweight)
           P_slugAns = (P_Weight) / (GRAVITY)
           PersonMass = P_slugAns * 14.5939

           calc_person_cuboid(PersonMass)
           break
       elif Selected_choice == "b" or Selected_choice == "B":
           ooWeight = raw_input("What is the weight of the object (lb)? \n")
           Weight = float(ooWeight)
           slugAns = (Weight) / (GRAVITY)  # Pounds divided by accerlation(m/s**2) is a unit called slug
           ObjectMass = slugAns * 14.5939  # Converting slugs to mass

           calc_cuboid(ObjectMass)
           break

       else:

           time.sleep(2)
           print "\nError! ENTER A VALID CHOICE!\n"
           del Selected_choice
           print("Is this parachute launch for an Object or Person?\n")
           print("a) Person")
           print("b) Object\n")
           Selected_choice = raw_input("Valid input should be 'a' or 'b' \n")
           continue

#SENDING DOWN A PERSON WITH A CUBOID SHAPED PARACHUTE!
def calc_person_cuboid(Mass_Of_Person):
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   print(
       "\nYou've chosen to simulate a PERSON skydiving, with a RECTANGLE-shape parachute. This is more complicated than sending an object,")
   print("YOU WILL BE ASKED ALOT OF QUESTIONS!.\n")
   time.sleep(3)
   PERSON_MASS = Mass_Of_Person

   while True:
       PLANE_MOVEMENT = raw_input(
           "Does the plane that the jumper is jumping from have a initial velocity to consider for? (y/n) \nNOTE: This is a simulation so it's okay to say 'n' \n")
       if (PLANE_MOVEMENT == "y" or PLANE_MOVEMENT == "Y"):
           PLANE_SPEED = input("What is the velocity of the plane(Along Y-axis) (m/s)? \n")
           break
       elif (PLANE_MOVEMENT == "n" or PLANE_MOVEMENT == "N"):
           PLANE_SPEED = 0
           break
       else:
           print("NOT A VALID INPUT! ")
           print("\n")

   # Asking if there is any vertical velocity prior to jumping for example if the jumper has a running start jumping down
   while True:
       VERTICAL_VELOCITY_INITIAL_QUESTION = raw_input(
           "Does the jumper have an initial VERTICAL(Z-axis) velocity?(y/n) \n")

       if (VERTICAL_VELOCITY_INITIAL_QUESTION == "y" or VERTICAL_VELOCITY_INITIAL_QUESTION == "Y"):
           VERTICAL_VELOCITY_INITIAL = input("What is the initial VERTICAL(Z-axis) velocity of the jumper (m/s)? \n")
           break
       elif (VERTICAL_VELOCITY_INITIAL_QUESTION == "n" or VERTICAL_VELOCITY_INITIAL_QUESTION == "N"):
           VERTICAL_VELOCITY_INITIAL = 0
           break
       else:
           print("NOT A VALID ANSWER! \n")
           print("\n")

   # Asking if there is any horizontal velocity prior to jumping for example if the jumper has a running start
   while True:
       HORIZONTAL_VELOCITY_INITIAL_QUESTION = raw_input(
           "Does the jumper have an initial HORIZONTAL(X-axis) velocity?(y/n) \n")
       if (HORIZONTAL_VELOCITY_INITIAL_QUESTION == "y" or HORIZONTAL_VELOCITY_INITIAL_QUESTION == "Y"):
           HORIZONTAL_VELOCITY_INITIAL = input(
               "What is the initial HORIZONTAL(X-axis) velocity of the jumper (m/s)? \n")
           break
       elif (HORIZONTAL_VELOCITY_INITIAL_QUESTION == "n" or HORIZONTAL_VELOCITY_INITIAL_QUESTION == "N"):
           HORIZONTAL_VELOCITY_INITIAL = 0
           break
       else:
           print("NOT A VALID ANSWER! \n")
           print("\n")

   while True:
       try:
           JUMP_HEIGHT = float(raw_input(
               "\nWhat height does the jumper decide to jump from (meters)?\nNOTE: If you enter '0' then the default height is 4000m\n"))
           if (JUMP_HEIGHT == 0):
               JUMP_HEIGHT = 4000
               break
           elif (JUMP_HEIGHT < 0):
               print("The maximum height cannot be less than zero! \n")
               print("\n")
           elif (JUMP_HEIGHT > 0):
               break
           else:
               print("NOT A VALID ANSWER! \n")
       except ValueError:
           print("\nThat was not a number, Please enter a number! \n")

   TIME_OF_FLIGHT = mt.sqrt((JUMP_HEIGHT) / (HALF_GRAVITY))
   print(
       "Your flight lasts: %.2f" % TIME_OF_FLIGHT + " seconds\nNOTE: This flight time is if the jumper does not open the parachute! \n")
   # print("Please select the time your simulated jumper decides to open the parachute, your range is from: [0-%.2f] " %TIME_OF_FLIGHT)
   # print("\n")

   while True:
       try:
           OPENING_PARACHUTE = float(raw_input(
               "Please select the time (in seconds) your simulated jumper decides to open the parachute, your range is from: [0-%.2f] " % TIME_OF_FLIGHT))
           print("\n")
           if (OPENING_PARACHUTE < TIME_OF_FLIGHT and OPENING_PARACHUTE > 0):
               break
           else:
               print("ERROR, Number not in range! \n")
       except ValueError:
           print("\nThat was not a number, Please enter a number! \n")
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   JUMPER_HORIZONTAL_DISPLACEMENT = HORIZONTAL_VELOCITY_INITIAL * OPENING_PARACHUTE  # X-coordinate point for position when the parachute dude deployed his/her parachute!
   print(
       "Your parachute dude's horizontal displacement position relative to the origin (plane): %.2f" % JUMPER_HORIZONTAL_DISPLACEMENT + "m \n")  # X-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_HORIZONTAL_VELOCITY = HORIZONTAL_VELOCITY_INITIAL  # X-coordinate point for velocity
   print(
       "Your parachute dude's horizontal velocity before the parachute is deployed is approximately: %.2f" % JUMPER_HORIZONTAL_VELOCITY + "m/s \n")  # X-coordinate point for velocity
   print("NOTE: This is because there is no acceleration in the x-axis \n")

   JUMPER_Y_AXIS_DISPLACEMENT = PLANE_SPEED * OPENING_PARACHUTE  # Y-coordinate point for position when the parachute dude deployed his/her parachute!
   print(
       "Your parachute dude's y-direction displacement is (due to plane's speed): %.2f" % JUMPER_Y_AXIS_DISPLACEMENT + "m\n")  # Y-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_Y_AXIS_VELOCITY = PLANE_SPEED  # Y-coordinate point for velocity
   print(
       "Your parachute dude's y-direction velocity is (due to plane's speed): %.2f" % JUMPER_Y_AXIS_VELOCITY + "m/s\n")  # Y-coordinate point for velocity

   JUMPER_VERTICAL_DISPLACEMENT = JUMP_HEIGHT + (VERTICAL_VELOCITY_INITIAL * OPENING_PARACHUTE) - (
       HALF_GRAVITY * OPENING_PARACHUTE ** 2)  # Z-coordinate point for position when the parachute dude deployed his/her parachute!
   print(
       "Your parachute dude's vertical displacement position relative to the initial position is: %.2f" % JUMPER_VERTICAL_DISPLACEMENT + "m \n")  # Z-coordinate point for position when the parachute dude deployed his/her parachute!

   JUMPER_VERTICAL_VELOCITY = VERTICAL_VELOCITY_INITIAL - (
       GRAVITY * OPENING_PARACHUTE)  # Z-coordinate point for velocity
   print(
       "Your parachute dude's vertical velocity before the parachute is deployed is approximately: %.2f" % JUMPER_VERTICAL_VELOCITY + "m/s \n")  # Z-coordinate point for velocity

   time.sleep(
       6)  # Making the python sleep for about 6 seconds, this is so that the user doesn't get bombarded with more incoming information, 4 seconds is enough to digest information before being thrown another screen

   for counter in range(0, 3,
                        1):  # THE COORDINATES ARE ALREADY CALCULATED BUT IT SLEEPS FOR UNTIL WHEN COUTNER HITS 3 SECONDS AND THEN PROCEEDS TO SHOW THE COORDINATES!
       print("CALCULATING THE COORDINATES. ")
       time.sleep(counter)
       print(". ")
       time.sleep(counter)
       print(". ")
       time.sleep(counter)
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")

   print("Position Coordinate (m): <%.2f, %.2f, %.2f>" % (JUMPER_HORIZONTAL_DISPLACEMENT, JUMPER_Y_AXIS_DISPLACEMENT,
                                                        JUMPER_VERTICAL_DISPLACEMENT) + "\nNOTE: THIS COORDINATE IS WHEN THE DUDE DEPLOYS THE PARACHUTE! \n")
   print("Velocity Coordinate (m/s): <%.2f, %.2f, %.2f>" % (JUMPER_HORIZONTAL_VELOCITY, JUMPER_Y_AXIS_VELOCITY,
                                                          JUMPER_VERTICAL_VELOCITY) + "\nNOTE: THIS COORDINATE IS WHEN THE DUDE DEPLOYS THE PARACHUTE!\n")
   time.sleep(6)
   print(
       "NOTE: at this point the jumper has pulled the parachute and we will now consider that it takes the jumper 3 seconds to pull the chute and has fallen approximately 60 meters! \n")
   time.sleep(4)

   print("\n")
   OBJECT_HEIGHT = input("Please enter the height of the parachute in meters: \n")
   OBJECT_WIDTH = input("Please enter the width of the parachute in meters: \n")
   OBJECT_LENGTH = input("Please enter the length of the parachute in meters: \n")
   print("\n")
   DRAG_CO = .75  # (Constant) drag coefficient of a cuboid shaped parachute (NO HOLES OR SLITS)
   VELOCITY = mt.sqrt((PERSON_MASS * GRAVITY) / (AIR_DENSITY * DRAG_CO * (
       (OBJECT_WIDTH * OBJECT_LENGTH) + (OBJECT_HEIGHT * OBJECT_LENGTH) + (OBJECT_HEIGHT * OBJECT_WIDTH))))
   print "\n*This is the descent velocity. which means the jumper will land with and"
   print "is fallling down with this velocity! \n"
   print "\nMass of the jumper is: %.2f" % PERSON_MASS, "kg\n"
   print "\nThe final velocity with the variables you entered is: %.2f" % VELOCITY, "m/s"

   time.sleep(3)

   TRIP_TIME_AFTER_PULLING_CHUTE = (JUMPER_VERTICAL_DISPLACEMENT - 60) / VELOCITY
   TOTAL_TRIP_TIME = TRIP_TIME_AFTER_PULLING_CHUTE + 3 + OPENING_PARACHUTE  # We are determining the total time it took to land. after the jumper pulled the chute, time it took to get the chute be fully deployed(3 seconds) and the time when he pulled
   # the chute
   print("The total time of skydive took approximately: %.2f" % TOTAL_TRIP_TIME + " seconds\n")
   time.sleep(4)

   paraPlot(TIME_OF_FLIGHT, JUMPER_VERTICAL_VELOCITY, JUMP_HEIGHT, JUMPER_VERTICAL_DISPLACEMENT,
            JUMPER_HORIZONTAL_VELOCITY, JUMPER_VERTICAL_VELOCITY, TOTAL_TRIP_TIME)


# Gets the input of the calculated mass of the object from above and solves for descent/terminal velocity for cuboid shaped parachute!
def calc_cuboid(Mass_of_Object):
   try:
       os.system('cls' if os.name == 'nt' or 'NT' else 'clear')
   except Exception:
       print("Unexpected Operating System!\n")
   print("You've chosen to send an OBJECT, with a CUBOID-shape parachute\n")
   # USER will define the object's mass

   # OBJECT_MASS = input("Please enter the mass of the object: ")
   OBJECT_MASS = Mass_of_Object
   print("\n")
   OBJECT_HEIGHT = input("Please enter the height of the parachute in meters: \n")
   OBJECT_WIDTH = input("Please enter the width of the parachute in meters: \n")
   OBJECT_LENGTH = input("Please enter the length of the parachute in meters: \n")
   print("\n")
   DRAG_CO = .75  # (Constant) drag coefficient of a cuboid shaped parachute (NO HOLES OR SLITS)
   VELOCITY = mt.sqrt((OBJECT_MASS * GRAVITY) / (AIR_DENSITY * DRAG_CO * (
   (OBJECT_WIDTH * OBJECT_LENGTH) + (OBJECT_HEIGHT * OBJECT_LENGTH) + (OBJECT_HEIGHT * OBJECT_WIDTH))))
   print "\n*This is the descent velocity. which means the object will land with and"
   print "is fallling down with this velocity! \n"
   print "*Parachute was opened as soon as the object was thrown out of the plane! \n"
   print "\nMass of the object is: %.2f" % OBJECT_MASS, "kg\n"
   print "\nThe final velocity with the variables you entered is: %.2f" % VELOCITY, "m/s"

def paraPlot(TIME,VELOCITY,HEIGHT, RELEASE_HEIGHT, HORIZONTAL_DISPLACEMENT, RVELOCITY, RTIME):

   x1 = np.linspace(0, TIME, TIME,endpoint=True) # Position vs time
   y1 = ((-HALF_GRAVITY*x1**2)-(VELOCITY*x1) + HEIGHT)

   x2 = np.linspace(0, TIME, TIME, endpoint=True) # Velocity vs time
   y2 = ((-GRAVITY*x2)+ RVELOCITY)

   x3 = np.linspace(HORIZONTAL_DISPLACEMENT, RTIME, RTIME, endpoint=True)
   y3 = ((-HALF_GRAVITY*x3**2)+(RVELOCITY*x3) + RELEASE_HEIGHT)



   plt.xlabel("Time")
   plt.ylabel("Position")
   plt.title("Parachute Dude(Position vs Time)")
   plt.ylim([0, HEIGHT+1000])
   plt.xlim([-1, TIME+10])
   plt.plot(x1,y1,'o')
   plt.plot(x3,y3,'o')
   plt.plot(HORIZONTAL_DISPLACEMENT,RELEASE_HEIGHT,'*')
   plt.show()



a = "Cone"
b = "Dome-shape"
c = "Rectangle"
d = "Cylinder"
e = "Cuboid(square-box)"
shapes = [a, b, c, d, e]
print("\neq2.py version 1.2 last edited on: 4/15/2017")
#time.sleep(5)
print("MAKE CHANGES TO THE DATE TO KNOW WHAT CHANGES WERE MADE!\n")
#time.sleep(7)
print("DO NOT MAKE ANY CHANGES WITHOUT LETTING ME KNOW FIRST! \n")
#time.sleep(5)

print("\nWhat shape is your parachute?")  # First Question to pop up and the user answers
print("a)Cone")
print("b)Dome-Shape")
print("c)Rectangle")
print("d)Cylinder")
print("e)Cuboid(square-box)")


# TIME_OF_FLIGHT = 30.0
# JUMPER_VERTICAL_VELOCITY = 0.0
# JUMP_HEIGHT = 4000.00
# HEIGHT_OF_RELEASE = 3352.68
# HORIZONTAL_D = .56
# RVELOCITY = 112.58
# RTIME = 700
# paraPlot(TIME_OF_FLIGHT,JUMPER_VERTICAL_VELOCITY,JUMP_HEIGHT, HEIGHT_OF_RELEASE, HORIZONTAL_D, RVELOCITY, RTIME)





choice = raw_input("Please select a letter: \n")
while choice == a or b or c or d or e:
   x = choice
   if x == "a" or x == "A":
       print("\nYour parachute will be CONE-shaped\n")
             #hole_cone() UNCOMMENTING THIS WOULD CAUSE FATAL ERROR!
       person_object_CONE()

       break
   elif x == "b" or x == "B":
       print("\nYour parachute will be DOME-shaped\n")
       #     hole_dome() UNCOMMENTING THIS WOULD CAUSE FATAL ERROR!
       person_object_DOME()
       break
   elif x == "c" or x == "C":
       print "\nYour parachute will be RECTANGLE-shaped\n"
       #     hole_rectangle() UNCOMMENTING THIS WOULD CAUSE FATAL ERROR!
       person_object_RECTANGLE()
       break
   elif x == "d" or x == "D":
       print("\nYour parachute will be CYLINDER-shaped\n")
       person_object_CYLINDER()
       break
   elif x == "e" or x == "E":
       print("\nYour parachute will be a CUBOID-shaped\n")
       person_object_CUBOID()
       break
   else:
       time.sleep(2)
       print("Please choice a valid option provided above!")
       del choice
       choice = raw_input("")
       continue

