# RAG Chatbot Backend

## Description
A FastAPI-based backend for a chatbot that uses OpenAI's GPT model to generate responses and MongoDB for storing knowledge. The project is containerized with Docker for easy deployment.

## Features
- RESTful API using FastAPI
- OpenAI GPT-4o for chatbot responses
- MongoDB Atlas for storing and retrieving knowledge
- Dockerized for easy deployment

## Technologies Used
- Python
- FastAPI
- OpenAI API
- MongoDB Atlas
- Docker
- Railway.app (for deployment)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rag-chatbot-backend.git
   cd rag-chatbot-backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root with the following content:
   ```env
   OPENAI_API_KEY=your-openai-api-key
   MONGO_URI=your-mongodb-uri
   ```

## Running the Application

### Using Python
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Using Docker
1. Build the Docker image:
   ```bash
   docker build -t rag-chatbot .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 --env-file .env rag-chatbot
   ```

## API Endpoints

- `GET /docs` - Access API documentation (Swagger UI)
- `POST /chat` - Send a chat message and get a response

## Deployment

1. Push code to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. Deploy on Railway.app:
   - Connect your GitHub repository
   - Set environment variables on the Railway dashboard
   - Deploy the application

## License
This project is licensed under the MIT License.
