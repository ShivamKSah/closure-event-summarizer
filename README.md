# Closure Event Summarizer

The Closure Event Summarizer is a Python-based application designed to efficiently extract audio from MP4 video files of virtual meetings, transcribe the audio using OpenAI's Whisper model, and generate concise summaries using OpenAI's GPT models. The tool also supports starting the summarization process from audio files and text files.

## Features

- **Audio Extraction**: Extract audio from MP4 video files.
- **Transcription**: Transcribe audio using OpenAI's Whisper model.
- **Summarization**: Generate summaries of the transcriptions using OpenAI's GPT-4o model.
- **File Management**: Save generated summaries as text files in an organized directory structure.

## Requirements

- Python 3.10 or higher (for compatibility with certain libraries and features). Download it [here](https://www.python.org/downloads/).
- An [OpenAI](https://openai.com) API key (ensure this key is kept secure and is not committed to version control).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ShivamKSah/closure-event-summarizer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd closure-event-summarizer
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For Linux or macOS:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

Alternatively, you can use the provided setup script to automate the creation of the virtual environment and installation of dependencies:
```bash
./setup.sh
```

## Usage

### Quick Start Guide

1. **Set Up the OpenAI API Key**: 
   Create a file named `openai_apikey.txt` in the root directory of the project and add your OpenAI API key to this file.
   ```bash
   echo "your-openai-api-key" > openai_apikey.txt
   ```

2. **Run the Script**:
   Execute the `main.py` script in your terminal:
   ```bash
   python main.py
   ```

   You will be prompted to enter the name of the project for which you want to generate a summary. If the project does not exist, a new project directory will be created in the `projects` directory.

### Adding Files for Summarization

#### Video Files
1. Place the MP4 video file in the `videos` directory.
2. The script will extract the audio, transcribe it, and generate a summary, storing results in the respective directories.

#### Audio Files
1. Place the audio file in the `audios` directory.
2. The script will transcribe the audio and generate a summary.

#### Text Files
1. Place the text file in the `transcriptions` directory.
2. The script will generate a summary from the provided text file.

### Re-running the Script
After adding a video, audio, or text file, re-run `main.py` to process the new files:
```bash
python main.py
```

You will be prompted to select the source of your input:
1. Video file
2. Audio file
3. Text file
4. Exit

### Summary Structure

The generated summary follows a structured format, which includes:

```
1. Meeting Objectives
2. Key Discussion Points
3. Important Decisions
4. Action Items
5. Meeting Outcomes
6. Next Steps
```

You can customize this structure by editing the `summary_structure.txt` file in the `generate_meeting_summary/prompts` directory.

## Testing

Run unit tests with the following command:
```bash
python -m unittest discover tests
```
**Note:** Running tests that interact with the OpenAI API will consume your API tokens, so use them wisely.

## Setup Script

The `setup.sh` script automates the virtual environment setup and installation of dependencies:
```bash
./setup.sh
```

## TODO

- [ ] Add support for additional video formats
- [ ] Add support for additional audio formats
- [ ] Rewrite tests to utilize mocks for the OpenAI API
- [ ] Implement support for additional Transformer models
- [ ] Extend to other languages with automatic language detection
- [ ] Improve terminal output for better user experience
- [ ] Conduct testing across different operating systems

## Acknowledgements

- [OpenAI](https://openai.com)
- [MoviePy](https://zulko.github.io/moviepy)
- [Pydub](https://github.com/jiaaro/pydub)

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Contact

For any inquiries, please reach out to Shivam Kumar Sah at [shivamsah.141205@gmail.com].
