# Architecture Decisions
1. **Stable tool IR over provider-specific schemas**: lets routing/policy work uniformly.
2. **Authorization outside the model**: planning cannot grant authority.
3. **Protocol adapters behind a router**: MCP/A2A/REST/GraphQL/CLI evolve independently.
4. **Read/write/destructive risk taxonomy**: simple baseline for approval policy.
5. **Sandbox commands are allowlisted**: no arbitrary shell execution in the API process.
