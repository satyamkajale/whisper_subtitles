from setuptools import setup, find_packages

setup(
    name="whisper_subtitles",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ffmpeg-python",
        "whisper",
        "argparse"
    ],
    entry_points={
        "console_scripts": [
            "whisper_subtitles=whisper_subtitles.main:main",
        ],
    },
    author="Satyam Kajale",
    author_email="satyamkajale@gmail.com",
    description="A tool to generate subtitles for videos using Whisper",
    license="MIT",
    keywords="subtitles whisper video",
    url="https://github.com/satyamkajale/whisper_subtitles",
)
