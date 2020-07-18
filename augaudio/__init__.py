import librosa as lr
import numpy as np
import random

def GaussianNoise(data, noise_factor):
    noise = np.random.randn(len(data))
    return data + noise * noise_factor * noise_factor / 250

def PitchShift(data, pitch_factor, sampling_rate=22050):
    return lr.effects.pitch_shift(data, sampling_rate, pitch_factor*4)

def TimeStretch(data, stretch_factor):
    if stretch_factor < 0:
        raise AttributeError('stretch_factor must be positive')
    return lr.effects.time_stretch(data, stretch_factor + 1)

def Crush(data, crush_factor, sampling_rate=22050):
    return lr.effects.pitch_shift(lr.effects.pitch_shift(data, sampling_rate, crush_factor*4), sampling_rate, crush_factor*-4)

augmantations = (GaussianNoise, PitchShift, TimeStretch, Crush)

def augment(data, augmentation=-1, intensity=1, sampling_rate=None):
    if not isinstance(data,np.ndarray):
        raise AttributeError('Expecting type(data) to be numpy.ndarray')
    if not augmentation in range(0,len(augmantations)):
        raise AttributeError('Augmentation must be an integer in [0, ' + str(len(augmantations)-1) + ']')
    if not sampling_rate == None:
        return augmantations[augmentation](data, intensity, sampling_rate).astype(type(data[0]))
    else:
        return augmantations[augmentation](data, intensity).astype(type(data[0]))

def randomAugmentations(data):
    for augmentation in range(0,len(augmantations)):
        if bool(random.getrandbits(1)):
            data = augment(data,augmentation,random.randint(1,5))
    return data
