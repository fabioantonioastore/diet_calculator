from pulp import LpProblem, LpVariable, value


problem = LpProblem("metas", 1)
xA = LpVariable("Boiled Egg", lowBound=0)
xB = LpVariable("Carioca Beans", lowBound=600)
xC = LpVariable("White Rice", lowBound=0)
xD = LpVariable("Bread", lowBound=450, upBound=450)
problem += 0.126*xA + 0.027*xC + 0.048*xB + 0.055*xD >= 176
problem += 0.007*xA + 0.286*xC + 0.136*xB + 0.25*xD == 480
problem += 0.095*xA + 0.003*xC + 0.009*xB + 0.021*xD >= 80
problem += 1.43*xA + 1.3*xC + 0.76*xB + 1.415*xD == 3400
problem.solve()

if problem.status == 1:
    print(f"Boiled Egg: {value(xA)}, Carioca Beans: {value(xB)}, White Rice: {value(xC)}, Bread: {value(xD)}")
    print(f"Protein: {(value(xA) * 0.126) + (value(xB) * 0.048) + (value(xC) * 0.027) + (value(xD) * 0.055)}")
    print(f"Carbohydrate: {(value(xA) * 0.007) + (value(xC) * 0.286) + (value(xB) * 0.136) + (value(xD) * 0.25)}")
    print(f"Fat: {(value(xA) * 0.095) + (value(xB) * 0.009) + (value(xC) * 0.003) + (value(xD) * 0.021)}")
    print(f"Calories: {(value(xA) * 1.43) + (value(xB) * 0.76) + (value(xC) * 1.3) + (value(xD) * 1.415)}")
