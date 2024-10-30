import pytest

# Neste exemplo a seguir, usamos uma fixture para configurar dados de teste.

@pytest.fixture
def sample_data():
    return {"name": "Luiza", "age": 22}

def test_sample_data(sample_data):
    assert sample_data["name"] == "Luiza"
    assert sample_data["age"] == 22