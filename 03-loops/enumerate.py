menu = ["Green", "Lemon", "Spiced", "Mint"]
elist = list(enumerate(menu))
print(elist)
for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")