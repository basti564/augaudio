# augaudio
This package contains multiple simple audio data augmentations in order to increase/test the robustness of neural networks.

###### Original
<img src="https://user-images.githubusercontent.com/34898868/87811710-60d15000-c85f-11ea-8bda-da417d84b2ba.png" width="600">

###### Gaussian Noise
<img src="https://user-images.githubusercontent.com/34898868/87811713-629b1380-c85f-11ea-8c7a-f059138b8048.png" width="600">

###### Pitch Shift
<img src="https://user-images.githubusercontent.com/34898868/87811726-6464d700-c85f-11ea-9f31-f58aa7e91785.png" width="600">

###### Time Stretch
<img src="https://user-images.githubusercontent.com/34898868/87811730-65960400-c85f-11ea-93af-828c98aa9f51.png" width="600">

###### Crush
<img src="https://user-images.githubusercontent.com/34898868/87811733-66c73100-c85f-11ea-8bc0-5f4b2c5e7c79.png" width="600">

## Installation

You can install this package via
`pip install augaudio`

## Usage

### Example usage:
```python
import librosa
import augaudio
import soundfile

y, sr = librosa.load('audio.wav')

augmented = augaudio.augment(y, 1, 4)

soundfile.write('augmented.wav', augmented, sr)
```
#### Directly access one of the augmentations:
```python
...
augmented = augaudio.GaussianNoise(y, 4)
...
```
#### Chain augmentations together:
```python
...
augmented = augaudio.GaussianNoise(augaudio.TimeStretch(y, 2), 4)
...
```
#### Iterate over augmentations:
```python
...
for augmentation in range(4):
  for intensity in range(1,10):
    augmented = augaudio.augment(y, augmentation, intensity)
    soundfile.write(str(augmentation) + '-' + str(intensity) + '.wav', augmented, sr)
...
```
### Command Line Usage:
#### Single File:
`augaudio augaudio /path/to/audio.wav 0 5`
#### Complete Folder:
`augaudio /path/to/input 0 5 /path/to/output`

## Augmentations
| Augmentation | index | Description | negative intensity |
| --- | --- | --- | --- |
| Augmentations | -2 | Applies /multiple/ random augmentations | available |
| Random | -1 | Applies random augmentation | available |
| GaussianNoise | 0 | Applies gaussian noise to the audio data | n/a |
| PitchShift | 1 | Shifts the pitch of the audio data | available |
| TimeStretch | 2 | Stretches the time of the audio data | n/a |
| Crush | 3 | Crushes details by applying and reversing a pitch shift | available |

## Copyright Notice
```
Copyright 2020 Bastian Schwickert

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
