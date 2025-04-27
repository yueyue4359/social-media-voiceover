import argparse
import subprocess
from number_converter import convert_all


def synthesize_f5tts(ref_text: str = " ", gen_text: str = " ", ref_audio: str = "voice_sample.wav", model: str = "F5TTS_v1_Base") -> str:
    
    default_output = "test/infer_cli_basic.wav"
    gen_text_processed = convert_all(gen_text)
    command = f"""f5-tts_infer-cli --model {model} --ref_audio "{ref_audio}" --ref_text "{ref_text}" --gen_text "{gen_text_processed}" """
    subprocess.run(command, shell=True, check=True)
    print('Successfully generated audio from transcript!')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref_text", type=str, default=" ")
    parser.add_argument("--gen_text", type=str, default=" ")
    args = parser.parse_args()

    synthesize_f5tts(ref_text=args.ref_text, gen_text=args.gen_text)
