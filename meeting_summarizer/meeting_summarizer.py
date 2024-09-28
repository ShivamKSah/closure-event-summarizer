import openai

def summarize_transcription(transcriptions: str, api_key: str) -> str:
    """
    Summarizes the transcription text using OpenAI's GPT model.

    Parameters
    ----------
    transcriptions : str
        The transcription text to be summarized.
    api_key : str
        The API key for OpenAI.

    Returns
    -------
    str
        The summary of the transcription.
    """
    openai.api_key = api_key  # Set the API key

    # Call the OpenAI API for summarization
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or any other model you're using
            messages=[
                {"role": "user", "content": f"Summarize the following transcription:\n\n{transcriptions}"}
            ]
        )
        summary = response.choices[0].message['content'].strip()
        return summary

    except Exception as e:
        print(f"An error occurred while summarizing: {e}")
        return ""

def text_to_summary(project: str, transcription: str, audio_name: str, api_key: str):
    """
    Converts audio transcription to summary.

    Parameters
    ----------
    project : str
        The name of the project.
    transcription : str
        The transcription text.
    audio_name : str
        The name of the audio file.
    api_key : str
        The OpenAI API key.
    """
    summary = summarize_transcription(transcriptions=transcription, api_key=api_key)
    print(f"Summary for {audio_name}: {summary}")
