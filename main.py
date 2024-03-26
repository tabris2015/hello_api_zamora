from fastapi import FastAPI

app = FastAPI(title="Hello API")


@app.get("/")
def root():
    return {"status": "OK", "message": "fail"}


@app.get("/estudiantes")
def students(name: str, age: int):
    student = {"name": name, "age": age, "grade": "A+"}

    return student

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)