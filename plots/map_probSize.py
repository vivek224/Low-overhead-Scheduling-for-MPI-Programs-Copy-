
new_names =  {

    "1000"         : "1000 bodies", 
    "10000"        :  "10000 bodies",
    "100000"        :  "100000 bodies",

    "1024"          : "1024 mesh points",
    "8192"          : "8192 mesh points",
    "65536"      : "65536 mesh points"
}


def map_probSize(old_names):
    return [new_names[n] for n in old_names]
