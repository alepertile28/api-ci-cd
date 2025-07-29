from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from statistics import mean, median
from typing import List
from collections import Counter

app = FastAPI()

class Numbers(BaseModel):
    numbers: list[float] = Field(..., example=[1, 2, 3])

@app.post("/stats")
def get_stats(numbers: Numbers):
    values = numbers.numbers
    freqs = Counter(values)
    max_freq = max(freqs.values())
    modes = [num for num, count in freqs.items() if count == max_freq]

    if len(modes) != 1:
        raise HTTPException(status_code=400, detail="No unique mode found")

    return {
        "mean": mean(values),
        "median": median(values),
        "mode": modes[0]
    }
