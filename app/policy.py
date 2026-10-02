from dataclasses import dataclass
@dataclass
class Decision:
    effect:str; reason:str
class PermissionFirewall:
    def decide(self,principal,tool,arguments,approval_token=None):
        if not tool.enabled: return Decision("deny","tool disabled")
        if tool.risk=="read": return Decision("allow","read-only capability")
        if tool.risk=="write":
            return Decision("allow","approved write") if approval_token else Decision("approval","write requires approval")
        return Decision("deny","destructive tools denied by default")
firewall=PermissionFirewall()
