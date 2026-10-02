from app.models import Tool
class ToolRegistry:
    def __init__(self):
        self.tools={}
        for t in [
          Tool(name="playwright.navigate",description="Navigate a browser using Playwright MCP",protocol="mcp",risk="read",tags=["browser","web"]),
          Tool(name="m365.search",description="Search authorized Microsoft 365 knowledge",protocol="mcp",risk="read",tags=["m365","search"]),
          Tool(name="github.search",description="Search repositories and engineering data",protocol="mcp",risk="read",tags=["github","code"]),
          Tool(name="remote.agent.invoke",description="Delegate a task to a remote A2A agent",protocol="a2a",risk="write",tags=["agent","a2a"]),
          Tool(name="internal.lookup",description="Invoke an internal function",protocol="function",risk="read",tags=["internal"])
        ]: self.tools[t.name]=t
    def register(self,t): self.tools[t.name]=t; return t
    def get(self,n): return self.tools.get(n)
    def list(self): return list(self.tools.values())
registry=ToolRegistry()
