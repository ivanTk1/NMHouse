import gerrychain, numpy as np, pandas as pd
import maup
from gerrychain import Graph
import geopandas as gpd
import matplotlib.pyplot as plt
import networkx as nx

shapefile_path0 = "./nm_vest_20/nm_vest_20.shp"  #Election data
shapefile_path1 = "./nm_pl2020_b/nm_pl2020_p1_b.shp" #Total population counts
shapefile_path2 = "./nm_pl2020_b/nm_pl2020_p3_b.shp"
shapefile_path3 = "./nm_pl2020_cnty/nm_pl2020_cnty.shp"

# vest20_df = gpd.read_file(shapefile_path0)
# population_df = gpd.read_file(shapefile_path1)
vap_df = gpd.read_file(shapefile_path2)
# county_df = gpd.read_file(shapefile_path3)

print(vap_df.columns)

