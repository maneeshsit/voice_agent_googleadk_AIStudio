# Google ADK installation
pip install -q google-adk>=1.12.0

# Grab the API key from Google AI Studio
adk create --type=code agentadk --model gemini-2.0-flash-live-001 --api_key $GEMINI_API_KEY

# Run the adk web
adk web --host 127.0.0.1 --port 8001
