
# Whisper Subtitles

Whisper Subtitles is a powerful tool that generates subtitles for video files using the Whisper AI model. This project aims to make video content more accessible by providing accurate and easy-to-read subtitles for videos in all languages.

## Features

- **Automated Subtitle Generation:** Leverages the Whisper AI model to transcribe audio into text.
- **Subtitles Overlay:** Integrates subtitles directly into video files.
- **Customizable Models:** Supports different Whisper models for various levels of accuracy and performance.
- **Easy to Use:** Simple command-line interface for quick subtitle generation.

## Table of Contents

- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setting Up](#setting-up)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

Ensure you have FFmpeg installed on your system. FFmpeg is a multimedia framework to decode, encode, transcode, and stream audio and video.

- **macOS:**

  \`\`\`sh
  brew install ffmpeg
  \`\`\`

- **Windows:**

  Download FFmpeg from the [official website](https://ffmpeg.org/download.html) and follow the instructions to set up the environment variables.

- **Ubuntu/Debian:**

  \`\`\`sh
  sudo apt update
  sudo apt install ffmpeg
  \`\`\`

### Setting Up

Clone the repository and install the package along with its dependencies:

\`\`\`sh
git clone https://github.com/yourusername/whisper_subtitles.git
cd whisper_subtitles
pip install -r requirements.txt
pip install .
\`\`\`

## Usage

Generate subtitles for a video by running the following command:

\`\`\`sh
whisper_subtitles path/to/video.mp4 --model large-v2 --output_dir path/to/output
\`\`\`

### Command Line Options

- \`video\`: Path to the video file to transcribe.
- \`--model\`: Whisper model to use for transcription (default is \`large-v2\`).
- \`--output_dir\`: Directory to save the output video with subtitles (default is the current directory).

## Examples

Here are a few examples to get you started:

### Basic Usage

Generate subtitles using the default model and save the output in the current directory:

\`\`\`sh
whisper_subtitles path/to/video.mp4
\`\`\`

### Specify Output Directory

Save the subtitled video in a specific directory:

\`\`\`sh
whisper_subtitles path/to/video.mp4 --output_dir ./subtitled_videos
\`\`\`

### Use a Different Whisper Model

Use a smaller Whisper model for faster processing:

\`\`\`sh
whisper_subtitles path/to/video.mp4 --model base
\`\`\`


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
