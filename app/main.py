from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from statistics import mean, median, mode, StatisticsError
from typing import List


app = FastAPI()


class Numbers(BaseModel):
    numbers: list[float] = Field(..., example=[1, 2, 3])

@app.post("/stats")
def get_stats(numbers: Numbers):
    try:
        values = numbers.numbers
        return {
            "mean": mean(values),
            "median": median(values),
            "mode": mode(values)
        }
    except StatisticsError:
        raise HTTPException(status_code=400, detail="No unique mode found")