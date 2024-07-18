import uvicorn

if __name__ == "__main__":
    print("Starting server.....")
    uvicorn.run(
        "src.external.web.fastapi.app:app",
        host="0.0.0.0",
        port=8081,
        reload=True,
    )