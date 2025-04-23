import subprocess


def synthesize_f5tts(transcript: str, ref_audio: str = "voice_sample.wav", model: str = "F5TTS_v1_Base") -> str:
    default_output = "test/infer_cli_basic.wav"
    command = f"""f5-tts_infer-cli --model {model} --ref_audio "{ref_audio}" --ref_text "{ref_text}" --gen_text "{transcript}" """
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
  generate_voiceover(sample_text)
