import subprocess
import requests

token = subprocess.check_output(
    [
        r"C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd",
        "account",
        "get-access-token",
        "--scope",
        "api://86ae4984-1bf5-4431-b403-86de46d5642a/.default",
        "--query",
        "accessToken",
        "-o",
        "tsv"
    ],
    text=True
).strip()

url = "https://aip-df267ac9-api-management-dev.azure-api.net/ai/chat/completions?api-version=2025-01-01-preview"

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    # payload = {
    #     "messages": [
    #         {
    #             "role": "user",
    #             "content": question
    #         }
    #     ],
    #     "max_completion_tokens": 2000
    # }
    payload = {
        "messages": [
            {
                "role": "system",
                "content": "You are an expert Python teacher."
            },
            {
                "role": "user",
                "content": "Explain loops."
            }
        ],
        "max_completion_tokens": 2000
    }

    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    data = response.json()

    print("\nAI:")
    print(data["choices"][0]["message"]["content"])