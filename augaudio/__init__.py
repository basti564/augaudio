import librosa as lr
import numpy as np
import random


def GaussianNoise(data, noise_factor):
    noise = np.random.randn(len(data))
    return data + noise * noise_factor * noise_factor / 250


def PitchShift(data, pitch_factor, sampling_rate=22050):
    return lr.effects.pitch_shift(data, sampling_rate, pitch_factor * 4)


def TimeStretch(data, stretch_factor):
    return lr.effects.time_stretch(data, abs(stretch_factor) + 1)


def Crush(data, crush_factor, sampling_rate=22050):
    return lr.effects.pitch_shift(lr.effects.pitch_shift(data, sampling_rate, crush_factor * 4), sampling_rate, crush_factor * -4)


augmantations = (GaussianNoise, PitchShift, TimeStretch, Crush)


def augment(data, augmentation=-1, intensity=None):
    if not isinstance(data, np.ndarray):
        raise AttributeError('Expecting type(data) to be numpy.ndarray')
    if augmentation == -1:
        Random(data, intensity)
    elif augmentation == -2:
        Augmentations(data, intensity)
    elif not augmentation in range(0, len(augmantations)):
        raise AttributeError(
            'Augmentation must be an integer in [-2, ' + str(len(augmantations) - 1) + ']')
    if intensity == None:
        intensity = 2
    return augmantations[augmentation](data, intensity).astype(type(data[0]))


def Random(data, intensity=None):
    if intensity == None:
        intensity = random.randint(1, 5)
    return augment(data, random.randint(0, len(augmantations)), intensity)


def Augmentations(data, intensity=None):
    if intensity == None:
        for augmentation in range(0, len(augmantations)):
            if bool(random.getrandbits(1)):
                data = augment(data, augmentation, random.randint(1, 5))
    else:
        for augmentation in range(0, len(augmantations)):
            if bool(random.getrandbits(1)):
                data = augment(data, augmentation, intensity)
    return data
