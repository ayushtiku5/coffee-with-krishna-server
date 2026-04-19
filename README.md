# coffee-with-krishna-server

A chat API server that answers questions as Lord Krishna, offering insights and teachings from the Bhagavad Gita. Powered by Google Gemini.

## Running locally

```bash
export API_KEY=your_gemini_api_key
go run main.go
```

## Building

```bash
go build -o server .
./server
```

## Deploying on Cloud Run

```bash
gcloud run deploy
```

## API

### POST /chat

**Request:**
```json
{ "prompt": "What is the meaning of dharma?" }
```

**Response:**
```json
{ "response": "..." }
```
