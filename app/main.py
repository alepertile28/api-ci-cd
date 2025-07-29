from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from statistics import mean, median, mode, StatisticsError


app = FastAPI()


class Numbers(BaseModel):
    numbers: list[float]

@app.post("/stats")
def get_stats(numbers: Numbers):
    try:
        return {
            "mean": mean(numbers.values),
            "median": median(numbers.values),
            "mode": mode(numbers.values)
        }
        return result
    except StatisticsError:
        return HTTPException(status_code=400, detail="No unique mode found")