from fastapi import FastAPI


app = FastAPI()


tasks = [
    {"id": 1, "task": "Learn Python"},
    {"id": 2, "task": "Write CI/CD pipelines"},
]


@app.get("/tasks")
async def get_tasks():
    return tasks