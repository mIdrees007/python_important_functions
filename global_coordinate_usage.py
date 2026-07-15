from dis import dis

from global_coordinates import GlobalCoordinates

nsp =  GlobalCoordinates(latitude=(37, 46, 32, 6, "N"),
                         longitude=(122, 24, 39.4, "N"))

print(repr(nsp))

print(f"No Starch Press's offices are at {nsp}")

nostarch = GlobalCoordinates(latitude=(37, 36, 32, 6, "N"), 
                             longitude=(122, 24, 39, 4,"N"))