import uvicorn


async def app(scope, _, send):
    assert scope["type"] == "http"

    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/plain"],
            ],
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": b"Hello, world!",
        }
    )


if __name__ == "__main__":
    uvicorn.run("main2:app", port=5001, log_level="info", reload=True)
