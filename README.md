# genpark-missing-required-parameter-fallback-injector-skill

Automated fallback injector populating default values or typed nulls for missing required tool parameters.

## Architecture

```mermaid
flowchart TD
    Provided[Provided Model Arguments] --> Diff[Compare Against Required List]
    SchemaDefaults[Schema Property Defaults] --> Injector[Fallback Injector]
    Diff --> Injector
    Injector --> Complete[Complete Valid Parameter Dictionary]
```

## Features
- **Graceful Defaults**: Prevents tool call execution failure due to omitted optional or defaulted keys.
- **Pure Python**: 100% standard library.
