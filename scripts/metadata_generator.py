# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 15:19:32 2022

@author: kiiru
"""

import pandas as pd

import librosa

import os
import sys
sys.path.insert(0, '../scripts')

from audio_overview import AudiOverview
audio_obj = AudiOverview()

class MetadataGenerator():
    def _init_(self):
        """
        class init

        Returns
        -------
        None.

        """
        pass
    
    def meta_data(self, path, sep="|"):
        """
        Takes the metadata/transcription file and generates more
        metadata for it including; audio duration, sample rate etc.

        Parameters
        ----------
        path : os.path
            Path to the transcription data
        sep : separator, optional
            used as delimiter for the transcription file. The default is "|".

        Returns
        -------
        df : dataFrame
            DF with audio path, transcription and generated metadata.

        """
        df = pd.read_csv(path, sep=sep, header=None)
        df = df.drop([1], axis=1)
        df.columns = ['filename', 'transcription']
        
        toDrop = []
        filepaths = []
        sample_rates = []
        duration = []
        
        for f in df['filename']:
            f_name = f.strip()
            filepath = audio_obj.audio_files(f_name)
            try:
                if os.path.isfile(filepath):
                    audio, fs = librosa.load(filepath, sr=None)
                    filepaths.append(filepath)
                    sample_rates.append(fs)
                    duration.append(float(len(audio)/fs))
                else:
                    toDrop.append(f)
                    continue
            except:
                print("filepath not found")
                
        df = df[df.filename.isin(toDrop) == False]
        df['filepath'] = filepaths
        df['sample_rate'] = sample_rates
        df['duration'] = duration
        
        return df