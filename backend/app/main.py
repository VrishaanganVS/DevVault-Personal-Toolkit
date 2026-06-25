from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def read_root():
    return{"Message":"Welcome to DevVault"}

commands = [
    {
        "command": "git status",
        "description": "Check the status of your git repository",
        "category": "Git"
    }
]

@app.get("/commands")
def get_commands():
    return commands