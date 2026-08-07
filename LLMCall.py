import subprocess
import requests
import json

# Get Access Token
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

print("Token retrieved successfully")

url = "https://aip-df267ac9-api-management-dev.azure-api.net/ai/chat/completions?api-version=2025-01-01-preview"

payload = {
    "messages": [
        {
            "role": "user",
            "content": "Explain what an LLM is in simple terms."
        }
    ],
    "max_completion_tokens": 500
}

response = requests.post(
    url,
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    },
    json=payload,
    timeout=60
)

print("Status Code:", response.status_code)
print("\nResponse:")
print(response.text)