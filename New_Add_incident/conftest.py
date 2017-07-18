
from fixture.application import myApplication
import pytest

#for the same browser session added =+(scope="session")+=
@pytest.fixture(scope="session")
def app(request):
    fixture = myApplication()
    request.addfinalizer(fixture.destroy)
    return fixture