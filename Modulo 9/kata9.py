# def gasoline(tank1, tank2, tank3):
#     gas_aver = (tank1+tank2+tank3)/3

#     return f"""The average fuell is {gas_aver} 
#     tank number 1 ={tank1} % 
#     tank number 2={tank2} % 
#     tank number 3={tank3} %"""

# print(gasoline(0,0,0))

def average(tanks):
    gas_total= sum(tanks)
    number_of_tanks = len(tanks)
    return gas_total/number_of_tanks

def gasoline(tank1, tank2, tank3):
     return f"""The average fuell is {average([tank1,tank2,tank3])} 
     tank number 1 ={tank1} % 
     tank number 2={tank2} % 
     tank number 3={tank3} %"""

print(gasoline(255,355,355))