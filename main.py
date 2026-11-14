import asyncio
from pathlib import Path

from mistralai import agents

INSTRUCTIONS = Path(__file__).with_name("jarvis-system.md").read_text(encoding="utf-8")

agent = agents.Agent(
    model="mistral-large-4",
    name="jarvis",
    instructions=INSTRUCTIONS,
)


async def main() -> None:
    result = await agent.run("Bonjour Jarvis")
    print(result.text)


if __name__ == "__main__":
    asyncio.run(main())