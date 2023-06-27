from typing import Union

from fastapi import FastAPI
from time import sleep
from starlette.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://127.0.0.1",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get('/events')
async def events():
    async def event_generator():
        for i in range(10):
            yield f'data: Event {i}\n\n'
            sleep(1)
    return StreamingResponse(event_generator(), media_type="text/event-stream")

# @app.get("/events")
# async def events():
#     async def event_generator():
#         # 이벤트 메시지 생성
#         yield "data: Event 1\n\n"
#         sleep(1)
#         yield "data: Event 2\n\n"
#         sleep(1)
#         yield "data: Event 3\n\n"
    
#     return StreamingResponse(event_generator(), media_type="text/event-stream")