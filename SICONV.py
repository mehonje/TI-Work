unit_values={"K":3,"H":2,"D":1,"u":0,"d":-1,"c":-2,"m":-3}
unit_values_string="KHDudcm"

print("From")
from_value=float(input("Value? "))
print(unit_values_string)
from_unit=input("Unit? ")
print("\nTo")
print(unit_values_string)
to_unit=input("Unit? ")
to_value=from_value*(10**(unit_values[from_unit]-unit_values[to_unit]))
print("\n"+str(to_value)+" "+to_unit)
