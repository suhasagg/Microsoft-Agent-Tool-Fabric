# Threat Model
Trust neither planner output nor connector output. Major threats: prompt-injected tool selection, confused-deputy authorization, cross-tenant access, approval replay, SSRF, malicious MCP servers, A2A impersonation, CLI escape, secret leakage and unbounded fan-out.

Controls: authorization outside the LLM, risk metadata, approval boundary, tenant-scoped identity, egress allowlists, endpoint registration policy, schema validation, sandboxing, timeouts, quotas, audit, idempotency and protocol-specific authentication.

Production approval tokens should bind tenant, subject, tool, canonical argument hash, expiry and nonce.
