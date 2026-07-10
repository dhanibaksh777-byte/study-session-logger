from dotenv import load_dotenv
from groq import Groq
import os


load_dotenv()


client = Groq(api_key=os.getenv("groq_api_key"))
def get_conversation(message : list):
    Response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages=message,
        response_format={"type" : "json_object"}
    )
    return Response.choices[0].message.content


