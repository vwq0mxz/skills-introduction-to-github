from __future__ import annotations

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class AIAgent:
    """A minimal AI agent.

    Replace the body of ``run`` with your own agent logic. The UI only
    depends on the ``run(messages) -> str`` interface, so you can swap in
    any backend (custom API, local model, LangChain, etc.) without touching
    the UI code.
    """

    def __init__(self, model: str = "gpt-4o-mini", system_prompt: str | None = None):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "your-api-key-here":
            raise ValueError(
                "OPENAI_API_KEY is not set. Copy .env.example to .env and add your key."
            )
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.system_prompt = system_prompt or "You are a helpful assistant."

    def run(self, messages: list[dict]) -> str:
        """Take the chat history and return the agent's reply.

        Args:
            messages: A list of ``{"role": "user"|"assistant", "content": str}``.

        Returns:
            The assistant's reply as a string.
        """
        full_messages = [{"role": "system", "content": self.system_prompt}] + messages
        response = self.client.chat.completions.create(
            model=self.model,
            messages=full_messages,
        )
        return response.choices[0].message.content


