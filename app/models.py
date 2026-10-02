from typing import Any, Literal
from pydantic import BaseModel, Field
class Tool(BaseModel):
    name:str
    description:str
    protocol:Literal["mcp","a2a","function","rest","graphql","cli"]
    endpoint:str|None=None
    risk:Literal["read","write","destructive"]="read"
    tags:list[str]=Field(default_factory=list)
    input_schema:dict[str,Any]=Field(default_factory=dict)
    enabled:bool=True
class DiscoveryRequest(BaseModel):
    query:str
    limit:int=Field(default=5,ge=1,le=50)
class InvokeRequest(BaseModel):
    tool:str
    arguments:dict[str,Any]=Field(default_factory=dict)
    idempotency_key:str|None=None
    approval_token:str|None=None
class InvokeResult(BaseModel):
    status:Literal["ok","denied","approval_required","error"]
    output:Any=None
    error:str|None=None
    invocation_id:str
