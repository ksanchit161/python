def analyze_icecore_thermal(thermal_data: list) -> tuple:
    result=[]
    try:
        if not isinstance(thermal_data,list):
            raise TypeError
        if len(thermal_data)==0:
            raise ValueError
        for i in thermal_data:
            sum=0
            count=0
            for j in i:
                if isinstance(j,(int,float)):
                    sum+=j
                    count+=1
            average=sum/count
            if average>120:
                result.append(round(average))
        return tuple(result)
    except TypeError:
        return "Invalid Data Type"
    except ValueError:
        return ("No Thermal Data Found")

data=[(100, "bad", 110), (118.5, 119.5), (200, 201)]
print(analyze_icecore_thermal(data))





