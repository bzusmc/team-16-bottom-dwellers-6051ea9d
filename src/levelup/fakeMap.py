class FakeMap:
    theLowerBoundForTheXAxis = 0
    theUpperBoundForTheXAxis = 1
    theLowerBoundForTheYAxis = 0
    theUpperBoundForTheYAxis = 1

    def __init__(self, ):
        self.name = character_name

    theRangeOfTheXAxis = range(theLowerBoundForTheXAxis, theUpperBoundForTheXAxis)
    theRangeOfTheYAxis = range(theLowerBoundForTheYAxis, theUpperBoundForTheYAxis)

    def isWithinBounds(endingXPostion, endingYPosition):
        thePositionIsValid = False
        if endingXPostion in theRangeOfTheXAxis and endingYPosition in theRangeOfTheYAxis:
            thePositionIsValid = True
        return thePositionIsValid
        