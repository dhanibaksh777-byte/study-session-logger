# Study Session Logger 📚📊

A lightweight FastAPI service that converts free-text study updates into clean, structured JSON — using Groq's structured output (JSON mode). No database, no memory — a focused, single-purpose demonstration of turning messy natural language into predictable, machine-usable data.

## What It Does

Send a plain-text message like:

> "aaj maine 2 ghante Python padha aur DSA thoda revise kiya"

...and get back structured data:

```json
{
  "subject": "Python",
  "duration_minutes": 120,
  "topics": ["DSA"]
}
```

If the message isn't study-related, fields are returned as `null` instead of the model guessing or hallucinating data.

## Why Structured Output

Free text is easy for humans to write but hard for software to use. Structured output bridges that gap — the LLM parses the messy, casual input and returns predictable fields that code can directly act on (store, aggregate, chart, filter), without any manual text parsing.

## Tech Stack

- FastAPI
- Groq API (JSON mode via `response_format={"type": "json_object"}`)
- Pydantic

## Project Structure

```
├── main.py            # FastAPI app, /chat route
├── schemas.py           # Pydantic request/response models
├── groq_client.py         # Groq API call wrapper with JSON mode enabled
├── system_prompt.py        # Instruction defining the exact JSON structure & edge-case handling
├── requirements.txt
├── .gitignore
└── README.md
```

## Endpoint

### `POST /chat`

**Request:**
```json
{
  "message": "aaj maine 2 ghante python padha"
}
```

**Response:**
```json
{
  "subject": "python",
  "duration_minutes": 120,
  "topics": null
}
```

## How It Works

1. The user sends a free-text message.
2. A system prompt instructs the model to respond **only** in a fixed JSON structure (`subject`, `duration_minutes`, `topics`), and to set fields to `null` if the message isn't study-related.
3. Groq's `response_format={"type": "json_object"}` enforces that the model always returns valid JSON — never freeform text.
4. The returned JSON string is parsed with `json.loads()` into a Python dict, then unpacked into the `StudyLogs` Pydantic response model for validation and a clean API response.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Create a `.env` file:
   ```
   groq_api_key=your_groq_api_key
   ```
3. Run the server:
   ```
   uvicorn main:app --reload
   ```
4. Test via `/docs` (Swagger UI).

## Author

Built by Bilal (Dhani Baksh) as part of an ongoing series of small, focused FastAPI + AI integration projects — each one built from scratch to lock in a single core concept. This one covers structured output; earlier ones cover conversation memory, personality design, and error handling.
