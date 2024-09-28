import openai
from meeting_summarizer.utils import create_messages_from_transcripts
from openai_api_interaction import OpenAICompletionAPI

def generate_meeting_summary(
        summary: str,
        config: OpenAICompletionAPI,
        prompt_template: str,
) -> str:
    """
    Generates a meeting summary using OpenAI's Completion API.
    
    Parameters
    ----------
    summary : str
        The meeting summary.
    config : OpenAICompletionAPI
        The configuration for the OpenAI Completion API.
    prompt_template : str
        The template for creating the summary prompt.

    Returns
    -------
    str
        The generated meeting summary.
    """
    openai.api_key = config.api_key

    # Use gpt-3.5-turbo by default if gpt-4 is not accessible
    model_to_use = "gpt-3.5-turbo"

    # Optional: If you want to check for access to gpt-4 and use it if available
    try:
        models = openai.Model.list()
        if any(model.id == "gpt-4" for model in models["data"]):
            model_to_use = "gpt-4"
    except Exception as e:
        print("Error checking models:", e)

    # Create the messages
    messages = create_messages_from_transcripts(
        transcriptions=summary,
        model=model_to_use,
        num_token_completion=config.max_tokens
    )

    if len(messages) == 1:
        response = openai.ChatCompletion.create(
            model=model_to_use,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": messages[0]["content"]}
            ],
            max_tokens=config.max_tokens,
            temperature=config.temperature,
            top_p=config.top_p,
            n=config.n,
            presence_penalty=config.presence_penalty,
            frequency_penalty=config.frequency_penalty,
        )
        summary = response.choices[0]["message"]["content"].strip()
        return summary

    elif len(messages) < 20:
        response = openai.ChatCompletion.create(
            model=model_to_use,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "\n".join([msg["content"] for msg in messages])}
            ],
            max_tokens=config.max_tokens,
            temperature=config.temperature,
            top_p=config.top_p,
            n=config.n,
            presence_penalty=config.presence_penalty,
            frequency_penalty=config.frequency_penalty,
        )
        summary = [choice["message"]["content"].strip() for choice in response.choices]
        summary = merge_summaries(summary, config)
        return summary

    else:
        responses = []
        for i in range(0, len(messages), 20):
            response = openai.ChatCompletion.create(
                model=model_to_use,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "\n".join([msg["content"] for msg in messages[i:i + 20]])}
                ],
                max_tokens=config.max_tokens,
                temperature=config.temperature,
                top_p=config.top_p,
                n=config.n,
                stream=config.stream,
                presence_penalty=config.presence_penalty,
                frequency_penalty=config.frequency_penalty,
            )
            summary = [choice["message"]["content"].strip() for choice in response.choices]
            responses += summary
        summary = merge_summaries(responses, config)
        return summary
