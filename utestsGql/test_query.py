import pytest
import json
from tradeTools.schema import schema
from graphene.test import Client
from .data import initdata_users, initdata_categories
from .models import AuthUser


pytestmark = pytest.mark.django_db


def test_users():
    initdata_users()
    client = Client(schema)
    executed = client.execute("""query 
                                 {
                                     users
                                     {
                                        username
                                     }
                            }""")
    expected = {
        "data": {
            "users": [
              {
                "username": "testUser"
              },
              {
                "username": "testUser2"
              }
            ]
        }
    }
    executed_json = json.dumps(executed)
    assert executed == expected


def test_categories():
    initdata_categories()
    client = Client(schema)
    executed = client.execute("""query 
                                     {
                                         categories
                                         {
                                            title
                                         }
                                }""")
    expected = {
        "data": {
            "categories": [
                {
                    "title": "Category1"
                },
                {
                    "title": "Category2"
                },
                {
                    "title": "Category3"
                }
            ]
        }
    }
    executed_json = json.dumps(executed)
    assert executed == expected


def test_userbyid():
    initdata_users()
    client = Client(schema)
    executed = client.execute("""query 
                                 {
                                     user(userid:5)
                                     {
                                        username
                                     }
                            }""")
    expected = {
        "data": {
            "user": {
                "username": "testUser"
            }
        }
    }
    assert executed == expected
