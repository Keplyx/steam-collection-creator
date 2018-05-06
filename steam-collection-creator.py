
import sys
from collections import OrderedDict


class MapInfo:

    def __init__(self, workshop_link, normal_button_link, active_button_link):
        self.workshop_link = workshop_link
        self.normal_button_link = normal_button_link
        self.active_button_link = active_button_link


# Edit this with the workshop link, the clicked button link and the normal button link
# album for normal buttons : https://imgur.com/a/C0H3AuG
# album for clicked buttons : https://imgur.com/a/ki75sia

map_list = OrderedDict()
map_list["assault"] = MapInfo("https://steamcommunity.com/sharedfiles/filedetails/?id=750303494",
                              "https://imgur.com/PRN4Xdw.png", "https://imgur.com/mDcG4Zx.png")

map_list["cache"] = MapInfo("https://steamcommunity.com/sharedfiles/filedetails/?id=1104880439",
                            "https://imgur.com/K9xxQ1E.png", "https://imgur.com/Sr4kJeo.png")

map_list["inferno"] = MapInfo("https://steamcommunity.com/sharedfiles/filedetails/?id=715656653",
                              "https://imgur.com/RZWui6r.png", "https://imgur.com/cydNyRX.png")

map_list["italy"] = MapInfo("https://steamcommunity.com/sharedfiles/filedetails/?id=727993009",
                            "https://imgur.com/AvfGucM.png", "https://imgur.com/g15rb2T.png")

map_list["militia"] = MapInfo("https://steamcommunity.com/sharedfiles/filedetails/?id=966071743",
                              "https://imgur.com/27MKBeh.png", "https://imgur.com/UAmjZ39.png")

map_list["mirage"] = MapInfo("https://steamcommunity.com/sharedfiles/filedetails/?id=940310973",
                             "https://imgur.com/hNzrzHc.png", "https://imgur.com/pcZ40QC.png")

map_list["office"] = MapInfo("https://steamcommunity.com/sharedfiles/filedetails/?id=767501224",
                             "https://imgur.com/PxbDtd2.png", "https://imgur.com/YLDGr3l.png")

map_list["overpass"] = MapInfo("https://steamcommunity.com/sharedfiles/filedetails/?id=1362209446",
                               "https://imgur.com/Ignl5Za.png", "https://imgur.com/I6Fk6Fs.png")

map_list["vertigo"] = MapInfo("https://steamcommunity.com/sharedfiles/filedetails/?id=723224508",
                              "https://imgur.com/6UfOygs.png", "https://imgur.com/wGVslqJ.png")


# --------------------------------------------------------------------------------------------------------
# Do not modify the following code -----------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

def generate_button(info, active):
    if active:
        button = "[img]" + info.active_button_link + "[/img]"
    else:
        button = "[url=" + info.workshop_link + "][img]" + info.normal_button_link + "[/img][/url]"
    return button


def generate_description(selected_name):
    description = ""
    for map_name, map_info in map_list.items():
        description += generate_button(map_info, selected_name == map_name)
    return description


if len(sys.argv) <= 1:
    print("Generating code without active map:", end="\n\n")
    print(generate_description(-1))
else:
    map_name = sys.argv[1]
    if map_name in map_list:
        print("Generating description with map '" + map_name + "' active:", end="\n\n")
        print(generate_description(map_name))
    else:
        print("Map " + map_name + " invalid. Available maps:", end="\n\n")
        for item in map_list.keys():
            print(item)
