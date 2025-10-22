import math

def menu_config():
    velocity = float(input("enter air velocity:"))
    object_area = float(input("enter object area:"))
    dragCF = float(input("enter drag coefficient:"))
    ad = float(input("enter air density:"))
    return velocity, ad, dragCF, object_area

def dragforce(v, ad, dCF, oa):
    dragforce = (v*v)*ad*dCF*oa
    print("df =", round(dragforce, 2))
    return dragforce

v, ad, dCF, oa = menu_config()
drag = dragforce(v, ad, dCF, oa)

