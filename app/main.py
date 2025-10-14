from fastapi import FastAPI


def read_version() -> str:
    try:
        with open("version.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "0.0.0"


app = FastAPI(title="PythonProject1", version=read_version())


@app.get("/health")
def health():
    return {"status": "ok", "version": app.version}

