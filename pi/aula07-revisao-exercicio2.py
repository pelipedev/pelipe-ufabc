def media_celsius_fahrenheit(celsius_array):
    total = 0
    for i in celsius_array:
        total += i
    total = total/len(celsius_array)
    return(celsius_fahrenheit(total))
def celsius_fahrenheit(celsius):
    american_temp = (celsius*1.8)+32
    return(american_temp)