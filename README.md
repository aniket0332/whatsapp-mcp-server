A Python-based MCP server built with **FastMCP** that connects Claude Desktop to WhatsApp through a local bridge.

This project focuses on exposing WhatsApp functionality as MCP tools, enabling Claude Desktop to interact with chats through a standardized local interface for messaging, chat access, and conversation workflows.

- Sending messages
- Listing chats
- Reading message history
- Searching conversations

## Demo

<img width="1512" height="993" alt="Screenshot 2026-05-25 211433" src="https://github.com/user-attachments/assets/c5bf64e5-da44-4a06-aba4-d78600e4239b" />
<img width="1496" height="983" alt="Screenshot 2026-05-25 211545" src="https://github.com/user-attachments/assets/9bae0e5c-e805-4752-a4cf-03e1f0162c53" />
<img width="1292" height="97" alt="Screenshot 2026-05-25 211621" src="https://github.com/user-attachments/assets/f84d1f59-8fe9-4e99-91da-9628c72167f1" />

## Architecture

```text
Claude Desktop
   ↓
Python MCP Server (FastMCP)
   ↓
Python REST Client
   ↓
Go REST API
   ↓
whatsmeow
   ↓
WhatsApp Web
```

---

## Features

### Messaging
- Send text messages
- Send media messages
- Support for direct chat messaging

### Chat Access
- List chats
- Fetch recent conversations
- Search messages

### Local Storage
- Message history stored locally
- Chat metadata caching
- SQLite-based persistence

### Claude Integration
- MCP-compatible tool interface
- Local stdio transport
- Works with Claude Desktop

---

## Tech Stack

### Backend
- Go
- whatsmeow
- SQLite

### MCP Layer
- Python
- FastMCP

### Client
- Claude Desktop

---

## Setup

### 1. Clone repository

```bash
git clone <your-repo-url>
cd whatsapp-mcp
```

---

### 2. Install Python dependencies

```bash
pip install fastmcp requests
```

---

### 3. Install Go dependencies

```bash
go mod tidy
```

---

## Running the Go WhatsApp Bridge

Start the Go server:

```bash
go run main.go
```

On first run:

- Scan the QR code with WhatsApp
- Authenticate your session

Expected output:

```text
✓ Connected to WhatsApp!
Starting REST API server on :8081...
REST server is running.
```

---

## Running the MCP Server

Start the Python MCP server:

```bash
python mcp_server.py
```

---

## Claude Desktop Configuration

Add to Claude Desktop MCP config:

```json
{
  "mcpServers": {
    "whatsapp": {
      "command": "python",
      "args": ["path/to/mcp_server.py"]
    }
  }
}
```

Restart Claude Desktop.


