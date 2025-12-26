# API Reference

## Overview

AI Server Launcher runs an OpenAI-compatible API server. All requests use standard HTTP methods and JSON payloads.

**Base URL:** `http://localhost:8080/v1`

## Authentication

Optional Bearer token authentication via API key parameter.

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" http://localhost:8080/v1/models
```

## Endpoints

### 1. Chat Completions

**Endpoint:** `POST /v1/chat/completions`

Generate chat-style responses.

#### Request

```bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [
      {"role": "system", "content": "You are helpful assistant."},
      {"role": "user", "content": "Hello!"}
    ],
    "temperature": 0.7,
    "top_k": 40,
    "top_p": 0.9,
    "max_tokens": 512
  }'
```

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `model` | string | Yes | - | Model name (use "default") |
| `messages` | array | Yes | - | Message history array |
| `temperature` | float | No | 0.7 | Creativity level (0.0-2.0) |
| `top_k` | integer | No | 40 | Vocabulary filter size |
| `top_p` | float | No | 0.9 | Nucleus sampling threshold |
| `max_tokens` | integer | No | 512 | Maximum response length |
| `repeat_penalty` | float | No | 1.1 | Token repetition penalty |
| `frequency_penalty` | float | No | 0.0 | Frequency penalty |
| `presence_penalty` | float | No | 0.0 | Presence penalty |
| `stream` | boolean | No | false | Stream response (SSE) |

#### Response

```json
{
  "id": "chatcmpl-1234567890",
  "object": "text_completion",
  "created": 1703084400,
  "model": "default",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
      }
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 10,
    "total_tokens": 25
  }
}
```

### 2. Text Completions

**Endpoint:** `POST /v1/completions`

Generate text completions (legacy API).

#### Request

```bash
curl -X POST http://localhost:8080/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "prompt": "Once upon a time",
    "max_tokens": 100,
    "temperature": 0.8
  }'
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `model` | string | Yes | Model name |
| `prompt` | string | Yes | Input text |
| `max_tokens` | integer | No | Maximum tokens |
| `temperature` | float | No | Creativity |
| `top_k` | integer | No | Vocabulary size |
| `top_p` | float | No | Nucleus sampling |
| `stream` | boolean | No | Stream response |

#### Response

```json
{
  "id": "cmpl-1234567890",
  "object": "text_completion",
  "created": 1703084400,
  "model": "default",
  "choices": [
    {
      "text": "\n\nThere lived a great wizard...",
      "finish_reason": "length",
      "index": 0
    }
  ],
  "usage": {
    "prompt_tokens": 4,
    "completion_tokens": 100,
    "total_tokens": 104
  }
}
```

### 3. Embeddings

**Endpoint:** `POST /v1/embeddings`

Generate text embeddings (requires embedding mode).

#### Request

```bash
curl -X POST http://localhost:8080/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "input": "Your text here"
  }'
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `model` | string | Yes | Model name |
| `input` | string\|array | Yes | Text or array of texts |
| `encoding_format` | string | No | "float" or "base64" |

#### Response

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [0.123, -0.456, ...]
    }
  ],
  "model": "default",
  "usage": {
    "prompt_tokens": 4,
    "total_tokens": 4
  }
}
```

### 4. List Models

**Endpoint:** `GET /v1/models`

List available models.

#### Request

```bash
curl http://localhost:8080/v1/models
```

#### Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "default",
      "object": "model",
      "owned_by": "llama.cpp"
    }
  ]
}
```

### 5. Health Check

**Endpoint:** `GET /health`

Check server status.

#### Request

```bash
curl http://localhost:8080/health
```

#### Response

```json
{"status": "ok"}
```

## Streaming Responses

Use `"stream": true` for streaming responses (Server-Sent Events).

```bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [{"role": "user", "content": "Hello"}],
    "stream": true
  }'
```

**Response (streaming):**
```
data: {"choices":[{"delta":{"content":"Hello"}}]}
data: {"choices":[{"delta":{"content":" there"}}]}
data: {"choices":[{"delta":{"content":"!"}}]}
data: [DONE]
```

## Error Handling

Errors return HTTP status codes and error messages.

#### 400 Bad Request

```json
{
  "error": {
    "message": "Invalid request parameters",
    "type": "invalid_request_error",
    "code": "invalid_request"
  }
}
```

#### 500 Server Error

```json
{
  "error": {
    "message": "Internal server error",
    "type": "server_error",
    "code": "internal_error"
  }
}
```

## Common Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad request |
| 401 | Unauthorized |
| 404 | Not found |
| 429 | Rate limited |
| 500 | Server error |

## Examples

### Python

```python
import requests

url = "http://localhost:8080/v1/chat/completions"
headers = {"Content-Type": "application/json"}

data = {
    "model": "default",
    "messages": [
        {"role": "user", "content": "Hello!"}
    ],
    "temperature": 0.7,
    "max_tokens": 100
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

print(result['choices'][0]['message']['content'])
```

### JavaScript

```javascript
const response = await fetch('http://localhost:8080/v1/chat/completions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        model: 'default',
        messages: [{ role: 'user', content: 'Hello!' }],
        temperature: 0.7,
        max_tokens: 100
    })
});

const data = await response.json();
console.log(data.choices[0].message.content);
```

### Using with OpenAI Python Library

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="http://localhost:8080/v1"
)

response = client.chat.completions.create(
    model="default",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

## Rate Limiting

No rate limiting by default. Configure in advanced settings if needed.

## CORS

CORS is enabled for all origins by default. Configure via llama.cpp flags if needed.

## Performance Tips

1. **Use streaming** for better UX with long responses
2. **Adjust max_tokens** based on your needs
3. **Batch requests** when possible
4. **Use appropriate temperature** for your use case
5. **Monitor token usage** for cost estimation

## Version

API version: 1 (OpenAI-compatible)

Last updated: December 2025
