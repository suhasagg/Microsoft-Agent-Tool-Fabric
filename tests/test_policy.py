from app.policy import firewall
from app.registry import registry
from app.security import Principal
def test_write_requires_approval():
    p=Principal("u","t",frozenset())
    d=firewall.decide(p,registry.get("remote.agent.invoke"),{},None)
    assert d.effect=="approval"
def test_read_allowed():
    p=Principal("u","t",frozenset())
    assert firewall.decide(p,registry.get("github.search"),{}).effect=="allow"
