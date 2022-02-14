# def report(prelaunch,fli_time, destiny, e_tank,i_tank):
#     return f""" Prelaunch will be at: {prelaunch}
#         Flight time: {fli_time} hours
#         Destiny: {destiny}
#         Extern Tank: {e_tank} Lt
#         Intern Tank: {i_tank} Lt
#     """
from numpy import mintypecode


def report(destiny, *minutes, **fuel_rerviors):
    return f"""Total Flight time: {sum(minutes)} minutes
        Destiny: {destiny}
        Total Fuel: {sum(fuel_rerviors.values())}
    """


# print(report('21:00',51, 'Moon',355000,355000))

print(report('Moon',15,59,66,tank1=350000,tank2=6500000,reserv_tank=89000))