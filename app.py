import os
from dotenv import load_dotenv
import autogen

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

config = autogen.config_list_from_dict(
    {
        "model": "gpt-4.1-mini",
        "api_key": API_KEY
    }
)

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config}
)

user = autogen.UserProxyAgent(
    name="user",
    human_input_mode="ALWAYS"
)

assistant.llm_config["autonomous"] = True

assistant.initiate_chat(
    user,
    message="Hi! What task can I help you with?"
)
