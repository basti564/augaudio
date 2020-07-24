import soundfile as sf
from . import augment
import librosa as lr
from sys import argv
import os


def augmentFile(file, augmentation, intensity, output):
    y, sr = lr.load(file)
    print('Loaded ' + file)
    augmented = augment(y, int(augmentation), int(intensity))
    sf.write(output + '/' + os.path.splitext(os.path.basename(file))
             [0] + '-augmented.wav', augmented, sr)
    print('Wrote data to ' + output + '/' +
          os.path.splitext(os.path.basename(file))[0] + '-augmented.wav')


def help():
    print(
        'Usage: augaudio [input dir/file] [augmentation] [intensity] {output dir}')


def main():
    if len(argv) == 1:
        help()
    else:
        if len(argv) <= 4:
            dir = os.getcwd()
        else:
            dir = argv[4]
        if os.path.isfile(argv[1]):
            augmentFile(argv[1], argv[2], argv[3], dir)
        elif os.path.isdir(argv[1]):
            print('This is a directory')
            for file in os.listdir(argv[1]):
                filename = os.fsdecode(file)
                if filename.endswith(".wav"):
                    augmentFile(argv[1] + '/' + filename,
                                argv[2], argv[3], dir)
                    continue
        else:
            raise ValueError(argv[1] + ' is neither a file nor a directory')
