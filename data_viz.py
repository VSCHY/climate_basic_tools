#################
# USE SPECIFIC FONT

from matplotlib import font_manager as fm
from matplotlib import font_manager

# Set the path to your custom font file
font_path = '/home/aschrapffer/Documents/Exo/static/Exo-SemiBold.ttf'
font_manager.fontManager.addfont(font_path)

plt.rcParams['font.family'] = 'Exo'

#################
# CUSTOM COLORMAP

from matplotlib.colors import LinearSegmentedColormap
colors= ["#BD5333", "#FF9676","#FFEB8A","#D0E0C7","#00514F"]

cmap = LinearSegmentedColormap.from_list('custom_colormap', colors)
cmap_r = LinearSegmentedColormap.from_list('custom_colormap', colors[::-1])

cmap_reds = LinearSegmentedColormap.from_list('custom_colormap', ["gainsboro", "#FF9676", "#BD5333"])


