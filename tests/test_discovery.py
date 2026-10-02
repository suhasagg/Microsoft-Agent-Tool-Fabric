from app.discovery import discovery
def test_github_discovery():
    r=discovery.search("search github repositories",5)
    assert any(x["tool"]["name"]=="github.search" for x in r)
