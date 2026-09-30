"""Missing Required Parameter Fallback Injector.
100% Python Standard Library.
"""

class ParameterFallbackInjector:
    """Injects schema-defined default values for missing required parameters."""
    @staticmethod
    def inject_fallbacks(provided_params: dict, required_fields: list, property_schemas: dict) -> dict:
        injected = {}
        missing_unresolved = []
        output = dict(provided_params)

        for req in required_fields:
            if req not in output:
                schema = property_schemas.get(req, {})
                if "default" in schema:
                    output[req] = schema["default"]
                    injected[req] = schema["default"]
                else:
                    ptype = schema.get("type", "string")
                    defaults = {"string": "", "integer": 0, "number": 0.0, "boolean": False, "array": []}
                    val = defaults.get(ptype, None)
                    output[req] = val
                    injected[req] = val
                    missing_unresolved.append(req)

        return {
            "final_params": output,
            "injected_fallbacks": injected,
            "missing_without_defaults": missing_unresolved
        }
