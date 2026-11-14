# JARVIS — agent Mistral

Projet agent pour Mistral Studio, basé sur le prompt `jarvis-system.md`.

## Option A — agent hébergé (Build → Agents, sans rien héberger)

    pip install mistralai
    python create_hosted_agent.py   # avec MISTRAL_API_KEY dans l'environnement

Équivalent API : POST https://api.mistral.ai/v1/agents avec `model`, `name`, `description`, `instructions`.

## Option B — agent SDK déployé (déploiement managé Mistral depuis ce dépôt)

L'agent enregistré est appelable par nom : `agents.Agent.load_from(agent_name="jarvis")`.

Test local :

    export MISTRAL_API_KEY=...
    uv run python main.py
    uv run agents chat