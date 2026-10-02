# Runbook
## Elevated failures
Break down by protocol/tool. Check provider health and policy denials separately.
## Discovery degradation
Fall back to lexical metadata search and cap results.
## Suspected compromised connector
Disable the registry version, revoke credentials, block egress, preserve audit logs and rotate affected secrets.
## Sandbox incident
Terminate the sandbox, preserve permitted forensic metadata, rotate credentials exposed to the workload and review egress.
