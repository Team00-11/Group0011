import time

red = "red"
yellow = "yellow"
green = "green"

greenMessage = "You can move for the next"
yellowMessage = "Slow down. Be prepared to stop in the next"
redMessage = "Wait for the next"

messages = [greenMessage, yellowMessage, redMessage]

trafficSignal = {green: 6, yellow: 2, red: 5}
trafficSignalIndex = 0

while (True):
    currentLight = list(trafficSignal)[trafficSignalIndex]
    currentDelay = trafficSignal.get(currentLight)
    currentMessage = messages[trafficSignalIndex]

    print(f"The traffic light is currently {currentLight}.")
    print( f"{currentMessage} {currentDelay} seconds")
    print()

    time.sleep(currentDelay)

    if trafficSignalIndex < 2:
        trafficSignalIndex += 1
    else:
        trafficSignalIndex = 0
print(trafficSignalIndex)
print('Exiting program')





