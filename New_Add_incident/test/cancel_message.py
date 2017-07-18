# -*- coding: utf-8 -*-

from calendar import datetime
from model.group import myGroup
from model.group import myIncident2




def test_cancel_incident(app):
    app.login(myGroup("https://docit-preprod.stopit.fm/", "tj2@stopit.fm", "Stopit1234"))
        
    print('login:%s' % datetime.datetime.now())
        
    app.test_add_incident2(myIncident2("321", "321"))

    print("cancel2")
        
    app.logout()    
        
    print("test completed2")
