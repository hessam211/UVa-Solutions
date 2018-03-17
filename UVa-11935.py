km_passed = 0
leak_level = 0
gas_consumed = float(0)
consumption = float(0)
highest_gas = float(0)
while True:
    inp = [str(q) for q in input().split()]
    if inp[1] == "Fuel":
        gas_consumed += (int(inp[0]) - km_passed)*(consumption + leak_level)
        consumption = float(inp[3])/100
        km_passed = int(inp[0])
        if inp[3] == "0":
            break
        continue
    if inp[1] == "Leak":
        gas_consumed += (int(inp[0]) - km_passed) * (consumption + leak_level)
        leak_level += 1
        km_passed = int(inp[0])
        continue
    if inp[1] == "Mechanic":
        gas_consumed += (int(inp[0]) - km_passed) * (consumption + leak_level)
        km_passed = int(inp[0])
        leak_level = 0
        continue
    if inp[1] == "Gas":
        gas_consumed += (int(inp[0]) - km_passed) * (consumption + leak_level)
        km_passed = int(inp[0])
        if gas_consumed > highest_gas:
            highest_gas = gas_consumed
        gas_consumed = 0
    if inp[1] == "Goal":
        gas_consumed += (int(inp[0]) - km_passed) * (consumption + leak_level)
        if gas_consumed > highest_gas:
            print("%.3f"%gas_consumed)
        else:
            print("%.3f"%highest_gas)
        km_passed = 0
        leak_level = 0
        gas_consumed = 0
        consumption = 0
        highest_gas = 0
