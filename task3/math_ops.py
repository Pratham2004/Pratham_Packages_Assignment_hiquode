from statistics import mean, median, mode, StatisticsError

def get_mean(data):
    return mean(data)

def get_median(data):
    return median(data)

def get_mode(data):
    try:
        return mode(data)
    except StatisticsError:        
        return None