class Vwamp:
    def calculateVwamp(oMessage):
        sumSize     = 0.0
        sumPrice    = 0.0
        vwamp       = 0.0

        for value in oMessage:
            sumPrice += value.Price * value.Size
            sumSize += value.Size

        vwamp = sumPrice / sumSize

        return vwamp