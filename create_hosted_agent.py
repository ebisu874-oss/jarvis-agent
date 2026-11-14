import os
from pathlib import Path

from mistral import Mistral

INSTRUCTIONS = Path(__file__).with_name("jarvis-system.md").read_text(encoding="utf-8")

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

agent = client.beta.agents.create(
    model="mistral-large-4",
    name="jarvis",
    description=(
        "JARVIS — assistant personnel vocal, domotique et IA. "
        "Personnalité sarcastique, français familier belge, gestion des commandes "
        "Home Assistant (ha_handled / ha_response), sécurité prioritaire."
    ),
    instructions=INSTRUCTIONS,
)

print(agent.id)
print(agent.name)