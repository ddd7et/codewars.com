#https://www.codewars.com/kata/58941fec8afa3618c9000184/solutions/python/me/best_practice
#Task

#Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters due to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want to know when the height of the plant will reach a certain level.
#Example

#For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be 10.

def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    i = 0
    print(upSpeed, downSpeed, desiredHeight)
    while True:
        i += 1
        height += upSpeed
        if height >= desiredHeight:
            return i
        height -= downSpeed