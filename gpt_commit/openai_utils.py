import os
import openai
from .diff_utils import parse_diff, assemble_diffs
from .conventional_commits import CONVENTIONAL_COMMITS
import asyncio

DIFF_PROMPT = "Generate a succinct summary of the following code changes:"
COMMIT_MSG_PROMPT = (
    "Using no more than 50 characters, "
    "generate a descriptive commit message from these summaries:"
)
PROMPT_CUTOFF = 10000

openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.environ["OPENAI_API_KEY"]

async def complete(prompt):
    model_name = "gpt-3.5-turbo"

    print(f"Using AI model: {model_name}")
    print("----- Start of Prompt -----")
    print(prompt)
    print("----- End of Prompt -----")

    completion_resp = await openai.ChatCompletion.acreate(
        model=model_name,
        messages=[{"role": "user", "content": prompt[: PROMPT_CUTOFF + 100]}],
        max_tokens=128,
    )
    completion = completion_resp.choices[0].message.content.strip()

    print("----- Start of OpenAI Response -----")
    print(completion)
    print("----- End of OpenAI Response -----")

    return completion


async def summarize_diff(diff):
    assert diff
    return await complete(DIFF_PROMPT + "\n\n" + diff + "\n\n")

async def summarize_summaries(summaries):
    assert summaries
    return await complete(COMMIT_MSG_PROMPT + "\n\n" + summaries + "\n\n")

async def generate_single_commit_message(diff):
    if not diff:
        return "Fix whitespace"
    prompt = (
        "Act as a software engineer who is analyzing the guide ["
        + CONVENTIONAL_COMMITS
        + "] in order to write a commit message that effectively describes this diff file ["
        + diff
        + "]. Your message should clearly and concisely capture the changes made, following all instructions and conventions outlined in the provided guide. Please be sure to avoid including any explanations or additional information about your process - only provide the generated commit message."
    )
    
    # Chamamos a API com o novo prompt
    return await complete(prompt)

async def generate_commit_message(diff):
    if not diff:
        return "Fix whitespace"
    assembled_diffs = assemble_diffs(parse_diff(diff), PROMPT_CUTOFF)
    summaries = await asyncio.gather(
        *[summarize_diff(diff) for diff in assembled_diffs]
    )
    return await summarize_summaries("\n".join(summaries))
