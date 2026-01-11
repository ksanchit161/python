def adjust_crew_pay(data):
    updated_data = {}
    high_earners = {}

    for member, (base,bonus) in data.items():
        final_pay = base + (base * bonus) / 100

        if final_pay < 20000:
            continue


        if final_pay > 50000:
            high_earners[member] = final_pay
        else:
            updated_data[member] = final_pay

    return updated_data , high_earners

data={'Pilot':[40000,25],'Crew1':[18000,10],'Crew2':[25000,15]}
print(adjust_crew_pay(data))