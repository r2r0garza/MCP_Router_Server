import os
from dotenv import load_dotenv

load_dotenv()

def get_provider():
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")
    if LLM_PROVIDER == "openai":
        from .openai_provider import OpenAIProvider
        return OpenAIProvider()
    elif LLM_PROVIDER == "lmstudio":
        from .lmstudio_provider import LMStudioProvider
        return LMStudioProvider()
    elif LLM_PROVIDER == "openrouter":
        from .openrouter_provider import OpenRouterProvider
        return OpenRouterProvider()
    elif LLM_PROVIDER == "ollama":
        from .ollama_provider import OllamaProvider
        return OllamaProvider()
    elif LLM_PROVIDER == "anthropic":
        from .anthropic_provider import AnthropicProvider
        return AnthropicProvider()
    elif LLM_PROVIDER == "azure":
        from .azure_foundry_provider import AzureFoundryProvider
        return AzureFoundryProvider()
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")
