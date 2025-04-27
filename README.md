# social-media-voiceover
Generate super realistic voiceover for any social media content using f5-tts


You need to add your voice named: `ref_audio.wav` in the file and provide the `ref_text` 

For more details about inference please read the F5-TTS [repository](https://github.com/SWivid/F5-TTS/tree/main/src/f5_tts/infer)

## Installation

git clone https://github.com/yueyue4359/social-media-voiceover.git

## Setup

```bash

conda create -n f5tts-env
conda activate f5tts-env
poetry install
pip install f5-tts
```

## Prepare Your Audio Sample

Place a reference audio sample (e.g., your own voice) in the root directory of the project and name it:
```voice_sample.wav```
Otherwise it will use the default voice.

## Inference

To synthesize speech, run the following in your terminal:

```bash

python3 voiceover.py --ref_text "Hello" --gen_text "This is a test" 

--ref_text: The exact text spoken in your voice_sample.wav.

--gen_text: The text you want the model to synthesize in your voice.
```

Performance: Generating ~500 words takes approximately 4 minutes on most systems.
