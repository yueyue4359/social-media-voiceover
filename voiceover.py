import subprocess


def synthesize_f5tts(transcript: str, ref_text: str, gen_text: str, ref_audio: str = "voice_sample.wav", model: str = "F5TTS_v1_Base") -> str:
    default_output = "test/infer_cli_basic.wav"
    command = f"""f5-tts_infer-cli --model {model} --ref_audio "{ref_audio}" --ref_text "{ref_text}" --gen_text "{gen_text}" """
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
  sample_text = "This is a sample text for synthesis."
  synthesize_f5tts(sample_text)
