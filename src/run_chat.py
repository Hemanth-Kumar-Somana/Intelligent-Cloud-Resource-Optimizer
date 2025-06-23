# run_chat.py
import asyncio
from agentkit import processor

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
]

async def main():
    response = await processor.llm_chat("gpt-3.5-turbo", messages)
    print(response)

asyncio.run(main())
