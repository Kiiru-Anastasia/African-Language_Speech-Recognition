# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 04:10:52 2022

@author: kiiru
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import librosa
import librosa.display
import IPython.display as ipd
from scipy.io import wavfile as wav

import warnings
warnings.filterwarnings("ignore")

class AudiOverview:
    """
    class to read single audio data and give an overview of it.
    Includes waveplots, playbacks and Conversion overviews
    
    """
    
    def _init_(self):
        """
        class init

        Returns
        -------
        None.

        """
        
    def audio_files(self, audio_name, path="../rawdata/additional/Excerpts-Data/wavs"):
        """
        Takes name of audio file and appends the path to it

        Parameters
        ----------
        audio_name : TYPE. string
            DESCRIPTION. file name of your single audio
        path : TYPE, optional
            DESCRIPTION. The default is "../rawdata/additional/Excerpts-Data/wavs".

        Returns
        -------
        Relative path for the audio file

        """
        
        return f'{path}/{audio_name}.wav'
    
    def plot_waveplot(self, audio_path):
        """
        Takes the relative audio file path as argument and returns a waveplot
        and an audio playback

        Parameters
        ----------
        audio_path : TYPE. string 
            DESCRIPTION. relative audio path, generated from previous function

        Returns
        -------
        TYPE. plot, playback
            DESCRIPTION. waveplot and audio playback

        """
        
        plt.figure(figsize=(12, 6))
        audio_data, sample_rate = librosa.load(audio_path)
        librosa.display.waveshow(audio_data, sr=sample_rate)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.show()
        
        return ipd.Audio(audio_data, rate=sample_rate)
    
    def conversion_overview(self, audio_path):
        """
        Loads audio data using scipy(original) and librosa(converted) and returns
        their load data along with sample rate, min and max range as a dataframe.

        Parameters
        ----------
        audio_path : TYPE. string
            DESCRIPTION. relative plot of the audio file

        Returns
        -------
        df : TYPE. dataframe
            DESCRIPTION. a dataframe of the conversion overview
        scipy_data : TYPE. float
            DESCRIPTION. scipy load data
        librosa_data : TYPE. float
            DESCRIPTION. librosa load data

        """
        
        librosa_data, librosa_sample_rate = librosa.load(audio_path)
        scipy_sample_rate, scipy_data = wav.read(audio_path)
        
        data = {'Sample Rate': [scipy_sample_rate, librosa_sample_rate],
               'Wav file min range': [np.min(scipy_data), np.min(librosa_data)],
               'Wav file max range': [np.max(scipy_data), np.max(librosa_data)]}
        
        df = pd.DataFrame(data, index=['Original', 'Converted'])
        
        return df, scipy_data, librosa_data
    
    def plot_conversion(self,conversion_data):
        """
        Takes in scipy/librosa data generated from previous function and returns a plot

        Parameters
        ----------
        conversion_data : TYPE
            DESCRIPTION.

        Returns
        -------
        plot

        """
        
        plt.figure(figsize=(12, 4))
        plt.plot(conversion_data)
        plt.show()
    

