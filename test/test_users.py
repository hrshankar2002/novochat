from app import schemas

from .database import client, session


def test_root(client):
   res=client.get('/')
   assert res.json().get("message") == 'Hello World!!!'
   assert res.status_code==200
   
def test_create_user(client):
    res=client.post(
        '/users/',json={
            "email":"kon1122@gmail.com",
            "password":"password123"
        })
    new_user=schemas.UserOut(**res.json())
    assert new_user.email=='kon1122@gmail.com'
    assert res.status_code==201
        
  