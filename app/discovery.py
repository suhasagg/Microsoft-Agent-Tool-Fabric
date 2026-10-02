import re
from app.registry import registry
class ToolDiscovery:
    def search(self,query,limit=5):
        q=set(re.findall(r"[a-z0-9]+",query.lower()))
        scored=[]
        for t in registry.list():
            if not t.enabled: continue
            text=" ".join([t.name,t.description,*t.tags]).lower()
            tokens=set(re.findall(r"[a-z0-9]+",text))
            overlap=len(q & tokens)
            score=overlap/max(1,len(q))
            scored.append((score,t))
        scored.sort(key=lambda x:(x[0],x[1].name),reverse=True)
        return [{"score":s,"tool":t.model_dump()} for s,t in scored[:limit] if s>0]
discovery=ToolDiscovery()
