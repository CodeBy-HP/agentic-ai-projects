"""
Configuration module for the ComplAI Sales Agent System.
Contains all settings, API configurations, and constants.
"""

import os
from dotenv import load_dotenv
from openai import AsyncAzureOpenAI
from agents import set_default_openai_client

load_dotenv(override=True)


class Config:
    """Centralized configuration for the sales agent system."""
    
    AZURE_API_VERSION = "2025-03-01-preview"
    AZURE_MODEL = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
    
    EMAIL_FROM = "code.by.hp@gmail.com"
    EMAIL_TO = "harshpatelsirt1@gmail.com"
    
    MAX_TURNS = 30


def initialize_azure_client() -> AsyncAzureOpenAI:
    """
    Initialize and configure the Azure OpenAI client.
    
    Returns:
        AsyncAzureOpenAI: Configured Azure OpenAI client
    """
    client = AsyncAzureOpenAI(
        api_version=Config.AZURE_API_VERSION,
    )
    set_default_openai_client(client)
    return client
