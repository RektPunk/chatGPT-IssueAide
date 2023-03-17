import argparse
import openai


def get_openai_response(input_text: str) -> str:
    ## open api key
    openai.api_key: str = "****" #FIXME
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "너는 짧게 대답하는 봇이야."},
            {"role": "user", "content": input_text},
        ],
    )
    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-text")
    args = parser.parse_args()
    print(get_openai_response(args.input_text))
