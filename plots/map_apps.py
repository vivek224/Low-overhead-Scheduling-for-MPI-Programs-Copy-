
new_names =  {
    "nbody"      :   "Barnes-Hut",
    "NASLU"      : "NASLU",
    "PlasComCM-StrnRt"  : "PlasComCM-StrnRt"
}


def map_apps(old_names):
    return [new_names[n] for n in old_names]
