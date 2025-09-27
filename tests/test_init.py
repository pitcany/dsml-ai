import dsml_ai

def test_version_and_hello():
    assert hasattr(dsml_ai, "__version__")
    assert dsml_ai.hello() == "Hello, DSML!"
