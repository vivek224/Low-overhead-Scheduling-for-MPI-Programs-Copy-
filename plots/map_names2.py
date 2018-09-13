
new_names =  {
    "Nodes"         : "Nodes",
    "Static"         : "OMP-Static",
    "OMP-sta"       : "OMP_Static",
    "static"         : "OMP-Static",
    "Dynamic"        : "OMP-Dynamic",
    "dynamic"        : "OMP-Dynamic",
    "OMP-dyn"        : "OMP-Dynamic",
    "dyn"        : "OMP-Dyn",

    "uSchedExp"         : "uSched",
    "uSched"         : "uSched",
    "Static-Hybrid"  : "Static-Hybrid",
    "genColl"        : "Adpt-Naive",
    "Naive"          : "Adpt-Naive",
    "SlackConscious" : "Adpt-Collective",
    "Collective" : "Adpt-Collective",
    "callsite"       : "Adpt-Callpath Base",
    "callsite_dq"    : "Adpt-Callpath DQ",
    "callsite_fd"    : "slackSched",
    "Callpath"    : "Adpt-Callpath",
    "bestfs_t"    : "Best_fs",
    "vSched"      : "vSched",
    "full"        : "comboSched",

    "guided"       : "OMP-Guided",
    "Guided"       : "OMP-Guided",
    "OMP-gui"      : "OMP-Guided",

    "dotprod"      : "dp",
    "AMG"          : "amg",
    "NASLU"        : "naslu",
    "NASSP"        : "nassp",
    "NASBT"        : "nasbt",
    "NASLU-MZ"     : "naslu",
    "NASSP-MZ"     : "nassp",
    "NASBT-MZ"     : "nasbt",
    "PF3D"         : "pf3d",
    "amg2"        : "amg",
    "NASSP-MZ"    : "nassp",
    "NASBT-MZ"    : "nasbt",
    "NASLU-MZ"    : "naslu",
    "NASSPMZ"    : "nassp",
    "NASBTMZ"    : "nasbt",
    "NASLUMZ"    : "naslu",

# names of metrics - TODO: put this in another file , and organize it even more neatly if time
    "icores"    : "Across-Core-LdImb",
    "inodes"    : "Across-Node-LdImb",

    "fs"    : "Static Fraction",
    "fspct"    : "Percent Static",

    "time"    : "Wall Clock Time (seconds)",
}


def map_names2(old_names):
    return [new_names[n] for n in old_names]
