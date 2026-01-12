import os
import sys
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()

class AI:
    def __init__(self):
        self.messages = []
        self.hf_token = os.environ.get("HF_TOKEN")
        if not self.hf_token:
            print("❌ Mets ton token HF: export HF_TOKEN='...'", file=sys.stderr)
            sys.exit(1) 
        self.MODEL_ID = "deepseek-ai/DeepSeek-V3.2"
        self.client = InferenceClient(token=self.hf_token)

    def chat(self, user_text):
        self.messages.append({"role": "user", "content": user_text})
        resp = self.client.chat_completion(
            model=self.MODEL_ID,
            messages=self.messages,
            max_tokens=400,
            temperature=0.7,
            top_p=0.9,
        )

        assistant_text = resp.choices[0].message.get("content", "")
        self.messages.append({"role": "assistant", "content": assistant_text})
        return f"{assistant_text}\n"


