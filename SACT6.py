def assignValues ():
    temperature = float(input("What is the temperature outside? (Celsius)\n"))
    distance = float(input("What is the distance to your destination? (Kilometers)\n"))
    time = float(input("How much time do you have available? (minutes) \n"))
    return temperature, distance, time

temperature, distance, time = assignValues()
extend = True

while extend:
    if distance >= 5:
        print("\nSAFETY RECOMMENDATIONS: If you use a bike then follow the bike lane. If you hop on a bus check your belongings")
        print("TRANSPORTATION RECOMMENDATIONS: Ride on a bike or hope on the bus")
        print("EXTRA RECOMMENDATIONS: Make sure your bike tyres has enough air in them. Check the ticket prices for the bus")

    if temperature > 30 and time < 15:
        print("\nSAFETY RECOMMENDATIONS: Bring light clothing and use sunscreen")
        print("TRANSPORTATION RECOMMENDATIONS: Use a car or public transport")
        print("EXTRA RECOMMENDATIONS: Hurry up but make sure you have everything with you. Check the gas in your car")

    if distance <= 4 or time > 45:
        print("\nSAFETY RECOMMENDATIONS: While walking beware of your surroundings. Make sure you are in well enough condition to ride a bike")
        print("TRANSPORTATION RECOMMENDATIONS: Walk to your location or ride a bike")
        print("EXTRA RECOMMENDATIONS: Bring comfortable clothes. Make sure you bring your wallet in case you need to catch a ride on the way back")

    if input("Do you wish to reassign some values?\n").lower() == "yes":
        temperature, distance, time = assignValues()
    else:
        extend = False