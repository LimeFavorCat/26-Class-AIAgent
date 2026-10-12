import random
DICE_SIDES = [1,2,3,4,5,6]
DEFALT_WEIGHT = [100,100,100,100,100,100]
SUCCESS_THRESHOLD = 4
luck = -50
weight = [x - luck for x in DEFALT_WEIGHT[:SUCCESS_THRESHOLD-1]] + [x + luck for x in DEFALT_WEIGHT[:SUCCESS_THRESHOLD-1]]
DiceResult = random.choices(DICE_SIDES, weights=weight, k=6)
print(DiceResult)