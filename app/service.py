import uuid
from app.registry import registry
from app.discovery import discovery
from app.policy import firewall
from app.router import router
from app.observability import DISCOVERY,INVOKE,LATENCY
class Fabric:
    def discover(self,q,limit):
        DISCOVERY.inc(); return discovery.search(q,limit)
    async def invoke(self,p,req):
        iid=str(uuid.uuid4()); tool=registry.get(req.tool)
        if not tool: return {"status":"error","error":"unknown tool","invocation_id":iid}
        d=firewall.decide(p,tool,req.arguments,req.approval_token)
        if d.effect=="deny":
            INVOKE.labels(tool.name,"denied").inc()
            return {"status":"denied","error":d.reason,"invocation_id":iid}
        if d.effect=="approval":
            INVOKE.labels(tool.name,"approval_required").inc()
            return {"status":"approval_required","error":d.reason,"invocation_id":iid}
        try:
            with LATENCY.labels(tool.name).time(): out=await router.invoke(tool,req.arguments)
            INVOKE.labels(tool.name,"ok").inc()
            return {"status":"ok","output":out,"invocation_id":iid}
        except Exception as e:
            INVOKE.labels(tool.name,"error").inc()
            return {"status":"error","error":str(e)[:4000],"invocation_id":iid}
fabric=Fabric()
