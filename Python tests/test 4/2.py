def temperature(celsius):
    fahrenheit=(celsius*(9/5))+32
    return f"{fahrenheit:.2f}"
celsius=int(input())
print(temperature(celsius))
