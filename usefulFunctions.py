#import necessary packages
import os
from natsort import natsorted
from nilearn import surface
import numpy as np

# function to generate subject list from BIDS Directory
def subject_list(dir, exclude_subs = None):
    """Returns a list of subject IDs from a parent directory.
       
       Parameters :
       dir : str 
           path to parent directory contain subject-specific folders
       exclude_subs : {None, list}
           List of subject IDs to exclude from list. 
           If None, returns full list of subject IDs in directory.
           If list, returns list of subject IDs in directory excluding specified IDs.
    """

    dir_contents = os.listdir(dir)
    subject_list = [sub for sub in dir_contents if sub.startswith('sub') and '.' not in sub]
    if (exclude_subs != None):
        subject_list = [sub for sub in subject_list if not any(removed_sub in sub for removed_sub in exclude_subs)]
    subject_list_sorted = natsorted(subject_list)
    return(subject_list_sorted)

def read_in_rois(label_path_list):
    """Reads in any number of label paths and return a single roi label.
       
       Parameters :
       label_path_list : list 
           list of label paths
    """

    if len (label_path_list)>0:   
        if len(label_path_list) >1: #multiple labels of same roi
            label =surface.load_surf_data(label_path_list[0])
            for roi_indx in range(len(label_path_list)):
                if roi_indx >0:
                    label=np.concatenate((label,surface.load_surf_data(label_path_list[roi_indx])))
        else: #only 1 label per roi
            label =surface.load_surf_data(label_path_list[0])
        return(label)