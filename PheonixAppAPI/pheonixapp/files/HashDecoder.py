#    _____              .___       __________            _____   __           .__          ___.   .__
#   /     \ _____     __| _/____   \______   \___.__.   /  _  \ |  | __  _____|  |__   ____\_ |__ |  |__ ___.__._____
#  /  \ /  \\__  \   / __ |/ __ \   |    |  _<   |  |  /  /_\  \|  |/ / /  ___/  |  \ /  _ \| __ \|  |  <   |  |\__  \
# /    Y    \/ __ \_/ /_/ \  ___/   |    |   \\___  | /    |    \    <  \___ \|   Y  (  <_> ) \_\ \   Y  \___  | / __ \_
# \____|__  (____  /\____ |\___  >  |______  // ____| \____|__  /__|_ \/____  >___|  /\____/|___  /___|  / ____|(____  /
#         \/     \/      \/    \/          \/ \/              \/     \/     \/     \/           \/     \/\/          \/
#     ___ ___________                      .___             ___
#    /  / \_   _____/___  __ __  ____    __| _/___________  \  \
#   /  /   |    __)/  _ \|  |  \/    \  / __ |/ __ \_  __ \  \  \
#  (  (    |     \(  <_> )  |  /   |  \/ /_/ \  ___/|  | \/   )  )
#   \  \   \___  / \____/|____/|___|  /\____ |\___  >__|     /  /
#    \__\      \/                   \/      \/    \/        /__/






# __________.__                        .__           _________ __            .___.__
# \______   \  |__   ____  ____   ____ |__|__  ___  /   _____//  |_ __ __  __| _/|__| ____  ______
#  |     ___/  |  \_/ __ \/  _ \ /    \|  \  \/  /  \_____  \\   __\  |  \/ __ | |  |/  _ \/  ___/
#  |    |   |   Y  \  ___(  <_> )   |  \  |>    <   /        \|  | |  |  / /_/ | |  (  <_> )___ \
#  |____|   |___|  /\___  >____/|___|  /__/__/\_ \ /_______  /|__| |____/\____ | |__|\____/____  >
#                \/     \/           \/         \/         \/                 \/               \/

import os
mainDir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

from HashDecoderT import *
import LIB
from Mapper import map

#Avail formats are -> [PSntx_H1]

op = input("Operation (Encode/Decode/Map): ")
if op.lower() == "encode":
    msg = input("Message: ")
    type = input("Type: ")
    if type.lower() in LIB.PSH.types_Lower:
        ComponentType = input("Component Type (Community, Enterprise, Pheonix Studios): ")
        if ComponentType.lower() in ["community", "enterprise", "pheonix studios", "pheonixstudios"]:
            print("\n\n\n\nEncoded Message: "+"\n"+Encode(msg, type, ComponentType).run())
        else:
            raise Exception("Only [Community, Enterprise, Pheonix Studios] are allowed as [Component Type]")
    else:
        map_ = map.Map(type).get_map()
        ComponentType = input("Component Type (Community, Enterprise, Pheonix Studios): ")
        if ComponentType.lower() in ["community", "enterprise", "pheonix studios", "pheonixstudios"]:
            print("\n\n\n\nEncoded Message: "+"\n"+Encode(msg, "map", ComponentType).run(map_))
        else:
            raise Exception("Only [Community, Enterprise, Pheonix Studios] are allowed as [Component Type]")

elif op.lower() == "decode":
    msg = input("Message: ")
    type = input("Type (Leave if don't have only for default): ")
    map_ = {}
    if not type.lower() in LIB.PSH.types_Lower:
        map_ = map.Map(type).get_map()
    print("\n\n\n\nDecoded Message: "+"\n"+Decode(msg, "map").run(map_))

elif op.lower() == "map":
    op_ = input("Get Map/Create Map/Remove Map/Remove Maps/Remove All Maps(GM, CM, RM, RMS, RAM): ")
    name = ""
    if op_ == "ram":
        pass
    else:
        name = input("Name of the map/list of maps separated by commas [,] and no spaces: ")

    if op_.lower() == "cm":
        map_ = input("Map (Leave for generating a random map): ")
        if map_.lower() == "":
            map_ = map.Map("").create_map()

        map.Map(name, map_).push_map()
        print("Map successfully created!")
    elif op_.lower() == "gm":
        print(map.Map(name).get_map())
    elif op_.lower() == "rm":
        map.Map(name).remove_maps("one", [name])
        print("Map Successfully removed!")
    elif op_.lower() == "rms":
        map.Map(name.split(",")[0]).remove_maps("list", name.split(","))
        print("Maps successfully removed!")
    elif op_.lower() == "ram":
        map.Map("").remove_maps("all")
        print("All Maps successfully removed!")
    else:
        raise ValueError(f"Unknown operation type -> [{op_}]. Available are -> [GM, CM, RM, RMS, RAM]")
else:
        raise ValueError(f"Unknown operation type -> [{op}]. Available are -> [Map, Decode, Encode]")