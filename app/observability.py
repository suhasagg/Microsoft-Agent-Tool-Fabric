from prometheus_client import Counter,Histogram
DISCOVERY=Counter("fabric_tool_discovery_total","Tool discovery calls")
INVOKE=Counter("fabric_tool_invocations_total","Tool invocations",["tool","status"])
LATENCY=Histogram("fabric_tool_invocation_seconds","Tool invocation latency",["tool"])
