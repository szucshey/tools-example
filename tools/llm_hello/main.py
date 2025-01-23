import os
import litellm
import argparse


def main_func(name: str):
    llm_key = os.environ["LLM_API_KEY"]
    llm_base_url = os.environ["LLM_BASE_URL"]
    try:
        print("Calling llm")
        response = litellm.completion(
            model="openai/gpt-4o",
            api_key=llm_key,
            base_url=llm_base_url,
            messages=[
                {
                    "content": f"Your task it to great people in a random movie star way, you must say which movie star you choose",
                    "role": "system",
                },
                {"content": f"My name is {name}, greet me!", "role": "user"},
            ],
        )
    except Exception as e:
        print(e)
        print("tool ended with error")
        return

    print(response.choices[0].message.content)
    print("tool ended successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str, required=True)
    args = parser.parse_args()
    main_func(args.name)
