# This is a Project 1 for Python Deep Dive course Part 2 by Serge Ivanko

import polygons as pl

pl1 = pl.RSCPolygon(7, 12)
pl2 = pl.RSCPolygon(5, 15.8)
pl3 = pl.RSCPolygon(7, 12)



print(f'{pl1=}, {pl2=}, {pl3=}')
print(f'{pl1=} :')
print(f'{pl1.interior_angle=};  {pl1.apothem=};  {pl1.edge_length=};  {pl1.area=};  {pl1.perimeter=}')

print(f'{pl1==pl2=};  {pl1==pl3=};  {pl1>pl2=};  {pl1>pl3=};  {pl1<pl2=}')

# Exceptions
# pl_Err1 = pl.RSCPolygon(7.3, 12)
# pl_Err1 = pl.RSCPolygon('7', 12)
# pl_Err1 = pl.RSCPolygon(7, '12')
# pl_Err1 = pl.RSCPolygon(7, -12)
# pl_Err1 = pl.RSCPolygon(2, 12)
#plErr = pl.RSCPolygon(5, -12)

###########
pls = pl.RSCPolygons(20, 1)
print(pls)

# print(pls._pls)
print(f'{pls[2]=}')
print(f'{pls[2:4]=}')
print(f'{len(pls)=}')
print(f'{pls.max_eff_polygon=}')
print('============================')
for plg in pls:
    print(f'{plg=}, {plg.area=}, {plg.perimeter=}, {plg.area / plg.perimeter=}')


####### try something
#a = int(2+3j)


