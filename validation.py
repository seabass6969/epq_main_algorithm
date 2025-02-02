import numpy
def isOutlier(numbers: list[int], value: int):
    # https://en.wikipedia.org/wiki/Interquartile_range
    # finding outlier by getting iqr and see if iqr*1.5 <= value
    q1 = numpy.percentile(numbers, 25)
    q3 = numpy.percentile(numbers, 75)
    iqr = (q3 - q1)
    if (iqr * 1.5) <= value and iqr != 0:
        return True
    else:
        return False
