import os
import ffmpeg as ffmpeg_python
import whisper
import tempfile
import warnings

def filename(path):
    return os.path.splitext(os.path.basename(path))[0]

def write_srt(segments, file):
    for segment in segments:
        start = segment['start']
        end = segment['end']
        text = segment['text'].strip().replace('-->', '->')

        file.write(f"{segment['id']}\n")
        file.write(f"{int(start // 3600):02}:{int((start % 3600) // 60):02}:{int(start % 60):02},{int((start % 1) * 1000):03} --> "
                   f"{int(end // 3600):02}:{int((end % 3600) // 60):02}:{int(end % 60):02},{int((end % 1) * 1000):03}\n")
        file.write(f"{text}\n\n")

def extract_audio(video_path):
    temp_dir = tempfile.gettempdir()
    audio_path = os.path.join(temp_dir, f"{filename(video_path)}.wav")
    ffmpeg_python.input(video_path).output(
        audio_path, acodec="pcm_s16le", ac=1, ar="16k").run(quiet=True, overwrite_output=True)
    return audio_path

def generate_subtitles(audio_path, model_name):
    # Suppress the specific whisper warning
    warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    # Re-enable warnings if needed
    warnings.filterwarnings("default")
    return result["segments"]

def overlay_subtitles(video_path, srt_path, output_dir):
    output_path = os.path.join(output_dir, f"{filename(video_path)}_subtitled.mp4")
    video = ffmpeg_python.input(video_path)
    audio = video.audio
    ffmpeg_python.concat(
        video.filter('subtitles', srt_path, force_style="OutlineColour=&H40000000,BorderStyle=3"), audio, v=1, a=1
    ).output(output_path).run(quiet=True, overwrite_output=True)
    return output_path
