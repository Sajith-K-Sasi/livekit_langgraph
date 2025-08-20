# livekit_langgraph

This is a simple example of a livekit agent that uses langgraph to process audio and generate responses.

## Setup

```bash
cp example.env .env
```

Fill in the values in the .env file.

```bash
uv sync
```
To install the dependencies.

## Usage

1. Create an account in livekit to get the url and api-key/secret
2. Before your first run, you must download certain models such as Silero VAD and the LiveKit turn detector:
	- `uv run python src/agent.py download-files`

3. Next, run this command to speak to your agent directly in your terminal:
	- `uv run python src/agent.py console`

4. To run the agent for use with a frontend or telephony, use the dev command:
	- `uv run python src/agent.py dev`

5. In production, use the start command:
	- `uv run python src/agent.py start`
	
6. Frontend starter templates:
	- Use the pre-built frontend starter apps from livekit to speak to the agent from frontend.
		- Eg. Web voice AI assistant with React & Next.js: https://github.com/livekit-examples/agent-starter-react
		- `git clone https://github.com/livekit-examples/agent-starter-react.git`
		- `cd agent-starter-react`
		- `npm install`
		- `npm run dev`
		
	- Run the agent in dev or production mode to chat through frontend
		- `uv run python src/agent.py dev`
		- `uv run python src/agent.py start`

