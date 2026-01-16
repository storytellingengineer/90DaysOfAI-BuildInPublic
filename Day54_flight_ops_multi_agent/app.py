from fastapi import FastAPI
from orchestration.run_pipeline import run
from agents.synthesizer import synthesize

app = FastAPI()

@app.get("/decision")
def decision(query: str):
    results = run(query)
    final = synthesize(results)
    return {
        "inputs": results,
        "decision": final
    }
