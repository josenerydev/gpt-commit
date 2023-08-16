param (
    [string]$openaiKey
)

if (-not $openaiKey) {
    Write-Error "Please provide the OpenAI key using -openaiKey."
    exit
}

# Set the OpenAI API key as an environment variable
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", $openaiKey, "Machine")

Write-Output "Configuration completed."
