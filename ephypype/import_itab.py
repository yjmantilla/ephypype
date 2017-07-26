# -*- coding: utf-8 -*-

import os
import mne


# -------------------- nodes (Function)
def convert_itab_to_raw_fif(itab_file):
    """Convert from ITAB .raw to .fif and save
    result in pipeline folder structure

    """

    import os.path as op

    from nipype.utils.filemanip import split_filename as split_f
    from mne.io import read_raw_itab

    _, basename, ext = split_f(itab_file)

    raw_fif_file = os.path.abspath(basename + '-raw.fif')

    if not op.isfile(raw_fif_file):
        raw = read_raw_itab(itab_file, preload=True)
        channel_indices = mne.pick_types(raw.info, meg=True)  # TODO
        print('****************************** {}'.format(raw.info['chs'][0]['logno']))
                          
        raw.save(raw_fif_file, picks=channel_indices, overwrite=True)
    else:
        print('*** RAW FIF file %s exists!!!' % raw_fif_file)

    return raw_fif_file
