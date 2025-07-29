from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from statistics import mean, median, mode, StatisticsError
from typing import List


app = FastAPI()


class Numbers(BaseModel):
    numbers: list[float] = Field(..., example=[1, 2, 3])

@app.post("/stats")
def get_stats(payload: Numbers):
    try:
        return {
            "mean": mean(payload.values),
            "median": median(payload.values),
            "mode": mode(payload.values)
        }
    except StatisticsError:
        return HTTPException(status_code=400, detail="No unique mode found")