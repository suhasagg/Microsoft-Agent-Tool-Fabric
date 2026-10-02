from fastapi import FastAPI,Depends,HTTPException
from fastapi.responses import Response
from prometheus_client import generate_latest,CONTENT_TYPE_LATEST
from app.models import Tool,DiscoveryRequest,InvokeRequest
from app.security import principal,require
from app.registry import registry
from app.service import fabric
app=FastAPI(title="Microsoft Agent Tool Fabric",version="1.0.0")
@app.get("/health/live")
async def live(): return {"status":"ok"}
@app.get("/v1/tools")
async def tools(p=Depends(principal)):
    require(p,"tools:discover"); return registry.list()
@app.post("/v1/tools/discover")
async def discover(r:DiscoveryRequest,p=Depends(principal)):
    require(p,"tools:discover"); return fabric.discover(r.query,r.limit)
@app.post("/v1/tools/register")
async def register(t:Tool,p=Depends(principal)):
    require(p,"tools:admin"); return registry.register(t)
@app.post("/v1/invoke")
async def invoke(r:InvokeRequest,p=Depends(principal)):
    require(p,"tools:invoke"); return await fabric.invoke(p,r)
@app.get("/metrics")
async def metrics(): return Response(generate_latest(),media_type=CONTENT_TYPE_LATEST)
