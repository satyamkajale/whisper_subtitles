import os
import tempfile
import warnings
import argparse
from whisper_subtitles.utils import filename, write_srt, extract_audio, generate_subtitles, overlay_subtitles

def main():
    parser = argparse.ArgumentParser(description="Generate subtitles for a video file using Whisper.")
    parser.add_argument("video", type=str, help="Path to the video file to transcribe")
    parser.add_argument("--model", type=str, default="large-v2", help="Whisper model to use for transcription")
    parser.add_argument("--output_dir", type=str, default=".", help="Directory to save the output video with subtitles")

    args = parser.parse_args()

    video_path = args.video
    model_name = args.model
    output_dir = args.output_dir

    os.makedirs(output_dir, exist_ok=True)

    print("Extracting audio...")
    audio_path = extract_audio(video_path)

    print("Generating subtitles...")
    segments = generate_subtitles(audio_path, model_name)

    srt_path = os.path.join(tempfile.gettempdir(), f"{filename(video_path)}.srt")
    with open(srt_path, "w", encoding="utf-8") as srt_file:
        write_srt(segments, srt_file)

    print("Overlaying subtitles onto video...")
    output_path = overlay_subtitles(video_path, srt_path, output_dir)

    print(f"Subtitled video saved to: {output_path}")

if __name__ == "__main__":
    main()
