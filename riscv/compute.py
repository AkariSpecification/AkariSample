import uvicorn
from fastapi import FastAPI
import subprocess

app = FastAPI()


@app.post("/compute")
async def compute(values: list[int]):
    process = subprocess.Popen(
        ["./compute"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    input_data = "\n".join(map(str, values))
    stdout_data, _ = process.communicate(input=input_data)

    result = stdout_data.strip()
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10080)
