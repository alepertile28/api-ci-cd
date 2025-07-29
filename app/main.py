from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from statistics import mean, median, mode, StatisticsError


app = FastAPI()


class Numbers(BaseModel):
    numbers: list[float]

@app.post("/stats")
def get_stats(data: Numbers):
    try:
        return {
            "mean": mean(data.numbers),
            "median": median(data.numbers),
            "mode": mode(data.numbers)
        }
    except StatisticsError:
        return HTTPException(status_code=400, detail="No unique mode found")