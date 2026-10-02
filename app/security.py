from dataclasses import dataclass
from fastapi import Header,HTTPException
import jwt
from app.config import settings
@dataclass(frozen=True)
class Principal:
    subject:str; tenant:str; scopes:frozenset[str]
async def principal(authorization:str|None=Header(default=None)):
    if settings.env=="dev" and not authorization:
        return Principal("dev-user","dev-tenant",frozenset({"tools:discover","tools:invoke","tools:admin"}))
    if not authorization or not authorization.startswith("Bearer "): raise HTTPException(401,"missing bearer token")
    try:
        p=jwt.decode(authorization[7:],settings.jwt_secret,algorithms=["HS256"])
        return Principal(str(p["sub"]),str(p["tenant"]),frozenset(str(p.get("scope","")).split()))
    except Exception as e: raise HTTPException(401,f"invalid token: {e}")
def require(p,s):
    if s not in p.scopes: raise HTTPException(403,f"missing scope {s}")
