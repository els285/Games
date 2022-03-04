# generate perfect startegy dataframes

d = {}

for y in range(5,21):
    for x in range(2,11):
        if y >= 17:
            d[(y,x)] ="S"
        elif y >= 13 and x <= 6:
            d[(y,x)]="S"
        elif y >= 13 and x >= 7:
            d[(y,x)]="H"
        elif y==12:
            if x <=3:
                d[(y,x)] = "H"
            elif x >= 4 and x <=6:
                d[(y,x)] = "S"
            else:
                d[(y,x)] = "H"
        elif y==11:
            d[(y,x)] = "D"
        elif y==10:
            if x < 10: 
                d[(y,x)] =  "D"
            else:
                d[(y,x)] = "H"
        elif y==9:
            if x==2 or x>4:
                d[(y,x)] = "H"
            else:
                d[(y,x)] =  "D"
        elif y<=8:
            d[(y,x)] = "H"


import pandas as pd
# print(d)
# input()

standard_Strategy = d


# standard_Strategy = pd.DataFrame(
#     data={'Strategy': list(d.values())}, 
#     index=pd.MultiIndex.from_tuples(tuples=d.keys(), names=['Player Total', 'Dealer Total'])
# )



# df = standard_Strategy
# print(df.ix[df.index.get_level_values('Player Total') == 5 & df.index.get_level_values('Dealer Total') == 2])
# input()

