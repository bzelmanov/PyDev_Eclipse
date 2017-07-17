# -*- coding: utf-8 -*-

from calendar import datetime
from group import myGroup
from group import myIncident
from application import myApplication
import pytest


@pytest.fixture
def app(request):
    fixture = myApplication()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_incident(app):
    app.login(myGroup("https://docit-preprod.stopit.fm/", "tj2@stopit.fm", "Stopit1234"))
        
    print('login:%s' % datetime.datetime.now())
        
    app.cancelIncident(myIncident("123", "123"))
        
    print("cancel")
        
    app.logout()    
        
    print("test completed")


