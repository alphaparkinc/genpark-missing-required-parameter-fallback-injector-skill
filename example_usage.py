from client import ParameterFallbackInjector

schemas = {"mode": {"type": "string", "default": "read"}, "retries": {"type": "integer", "default": 3}}
res = ParameterFallbackInjector.inject_fallbacks({}, ["mode", "retries"], schemas)
print("Injected final parameters:", res["final_params"])
