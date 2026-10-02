import asyncio
from app.config import settings
class ProtocolRouter:
    async def invoke(self,tool,args):
        # Real protocol adapters are isolated behind this interface.
        # Built-in safe local functions keep the project runnable without credentials.
        if tool.protocol=="function":
            if tool.name=="internal.lookup": return {"found":True,"query":args}
        if tool.protocol in {"mcp","a2a","rest","graphql","cli"}:
            return {"adapter":tool.protocol,"tool":tool.name,"arguments":args,
                    "note":"Configure endpoint/provider adapter for external execution."}
        raise ValueError("unsupported protocol")
router=ProtocolRouter()
