import subprocess

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

print("Token length:", len(token))