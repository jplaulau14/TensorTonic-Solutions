def promote_model(models: list) -> str:
    best = max(models, key=lambda model: (model["accuracy"], -model["latency"], model["timestamp"]))
    return best["name"]