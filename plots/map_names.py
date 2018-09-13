
new_names =  {
    "Nodes"         : "Nodes",
    "it"         : "iters",
   
    "Static"         : "OMP-Static",
    "OMP-sta"       : "OMP_Static",
    "static"         : "OMP-Static",
    "oGPU"         : "1GPU",
    "oGPUmx"         : "1GPU_max",
    "oGPUav"         : "1GPU_avg",
    "Dynamic"        : "OMP-Dynamic",
    "dynamic"        : "OMP-Dynamic",
    "OMP-dyn"        : "OMP-Dynamic",
    "dyn"        : "OMP-Dynamic",
   
    "uSchedExp"         : "uSched",
    "uSched"         : "Static-Hybrid",
    "Static-Hybrid"         : "Static-Hybrid",
    "genColl"        : "Adpt-Naive",
    "Naive"        : "Adpt-Naive",
    "SlackConscious" : "Adpt-Collective",
    "Collective" : "Adpt-Collective",
    "callsite"       : "Adpt-Callpath Base",
    "callsite_dq"    : "Adpt-Callpath DQ",
    "callsite_fd"    : "Adpt-Callpath",
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
    "NASLU-MZ"        : "naslu",
    "NASSP-MZ"        : "nassp",
    "NASBT-MZ"        : "nasbt",
    "PF3D"        : "pf3d",
    "amg2"        : "amg",
    "NASSP-MZ"    : "nassp",
    "NASBT-MZ"    : "nasbt",
    "NASLU-MZ"    : "naslu",
    "NASSPMZ"    : "nassp",
    "NASBTMZ"    : "nasbt",
    "NASLUMZ"    : "naslu",

    "icores"    : "Across-Core-LdImb",
    "inodes"    : "Across-Node-LdImb"
}


def map_names(old_names):
    return [new_names[n] for n in old_names]
