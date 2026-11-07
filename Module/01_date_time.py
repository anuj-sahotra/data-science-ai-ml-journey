import datetime

x = datetime.datetime.now()
print(f"YEAR-MONTH-DATE : {x}")

print(f"Day : {x.strftime("%A")}")

print(f"Day : {x.strftime("%a")}")

print(f"Month : {x.strftime("%B")}")

print(f"Month No. : {x.strftime("%m")}")

print(f"Year : {x.strftime("%Y")}")
