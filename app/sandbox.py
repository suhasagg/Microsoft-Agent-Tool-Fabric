import asyncio, os
class Sandbox:
    ALLOWED={"python-version":["python","--version"],"git-version":["git","--version"]}
    async def exec_named(self,name):
        if name not in self.ALLOWED: raise PermissionError("command not allowlisted")
        p=await asyncio.create_subprocess_exec(*self.ALLOWED[name],stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)
        out,err=await asyncio.wait_for(p.communicate(),10)
        return {"code":p.returncode,"stdout":out.decode()[:10000],"stderr":err.decode()[:10000]}
sandbox=Sandbox()
