import os


def load_env_vars():
    """Load only required environment variables based on the selected LLM provider."""
    provider = os.getenv("LLM_PROVIDER", "").strip().lower()
    model = os.getenv("MODEL")

    if provider not in ["groq", "ollama", "openai", "openrouter"]:
        raise ValueError(
            f"Unsupported LLM_PROVIDER: {provider}. Supported values are: groq, ollama, openai, openrouter."
        )

    if not model:
        raise ValueError("MODEL must be explicitly set in the environment.")

    config = {"provider": provider, "model": model}

    if provider in ["groq", "openai", "openrouter"]:
        api_key = os.getenv("LLM_API_KEY")
        if not api_key:
            raise ValueError(f"LLM_API_KEY is required for {provider.capitalize()} provider.")
        config["api_key"] = api_key

    if provider == "ollama":
        config["host"] = os.getenv("OLLAMA_HOST", "http://localhost:11434")

    if provider == "openai":
        config["base_url"] = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    elif provider == "openrouter":
        # OpenRouter uses OPENAI_API_BASE convention or defaults to its own endpoint
        config["base_url"] = os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1")


    return config
