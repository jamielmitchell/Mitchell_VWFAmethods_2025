# Mitchell_VWFAmethods_2025
Code associated with Mitchell, Fuentes-Jimenez, Stone, Yablonski, & Yeatman, 2025, bioRxiv - VWFA demonstrates individual and task-agnostic consistency but inter-individual variability.

## General Note
The data associated with this manuscript and analysis can be found in a Stanford University Libraries Digital Repository at [https://doi.org/10.25740/jp789mc0395](https://doi.org/10.25740/jp789mc0395). In order for the code to run flawlessly, you should download this data and store it in a folder named `data` and then download the code and store it in a parent folder alongside `data`. Addiotnally, proper installation of Freeview and the FreeSurfer viewing software[[1]](#1) is required for several of the files described below. Software information and installation instructions can be found [here](https://surfer.nmr.mgh.harvard.edu/).

## Content and Instructions
- extract_ROI_PSC.ipynb: A jupyter notebook that extracts mean activations from ROIs.
- group_ROI_differences.ipynb: A jupyter notebook that calculates a text-selectivity index based off activations from group and template ROIs. Requires CSVs generated from extract_ROI_PSC.ipynb.
- sepTask_VWFA_similarity.ipynb: A jupyter notebook that calculates similarity between task-specific VWFAs along with size and selectivity differences between task-specific VWFAs. Requires CSVs generated from extract_ROI_PSC.ipynb.
- second_level_analysis.ipynb: A jupyter notebook that fits a second-level analysis to contrasts maps, plots the results, and grabs screenshots of the results through Freeview. Requires proper installation of FreeSurfer and the Freeview viewing software.
- ROI_overlap.ipynb: A jupyter notebook that creates probability maps displaying overlap of ROIs and grabs screenshots of the results through Freeview. Requires proper installation of FreeSurfer and the Freeview viewing software.
- freeview_label_screenshots.ipynb: A jupyter notebook that grabs screenshots of ROIs through Freeview. Requires proper installation of FreeSurfer and the Freeview viewing software.
- plotting.ipynb: A jupyter notebook that generates the plots from the manuscript.
- usefulFunctions.py: A python script that contains custom functions to help make things a little easier.
- LMEs.Rmd: An r markdown file that contains code to run linear mixed-effects models and save model outputs. Requires CSVs generated from extract_ROI_PSC.ipynb.

## References 
<a id="1">[1]</a> 
Fischl, B. (2012). FreeSurfer. NeuroImage, 62(2), 774–781. https://doi.org/10.1016/j.neuroimage.2012.01.021

