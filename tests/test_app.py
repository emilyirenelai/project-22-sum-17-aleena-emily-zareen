# tests/test_app.py

import unittest
import os
from tests.common import TimelinePost
os.environ['TESTING'] = 'true'

#from app import app 

class AppTestCase(unittest.TestCase):
    # def setUp(self):
    #     self.client = app.test_client()

    # def test_home(self):
    #     response = self.client.get("/")
    #     assert response.status_code == 200
    #     html = response.get_data(as_text=True)
    #     assert "<title>Emily Lai</title>" in html
        # More tests relating to the home page
        # response = self.client.get("/")
        # assert response.status_code == 200
        # html = response.get_data(as_text=True)
        # assert "<div class=\"slider\">" in html

    def tautology(self):
        assert 1 == 1

    # def test_timeline(self):
    #     response = self.client.get("/api/timeline_post")
    #     assert response.status_code == 200
    #     assert response.is_json
    #     json = response.get_json()
    #     assert "timeline_posts" in json
    #     assert len(json["timeline_posts"]) == 0
        # Tests relating to the /api/timeline_post GET and POST apis
        # response = self.client.get("/api/timeline_post")
        # assert response.status_code == 200
        # html = response.get_data(as_text=True)
        # assert "timeline_post" in html

        # response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email":"john@example.com", "content": "Hello World, I'm John!"})
        # assert response.status_code == 200
        # html = response.get_data(as_text=True)


        # TODO Add more tests relating to the timeline page
        # response = self.client.get("/timeline")
        # assert response.status_code == 200
        # html = response.get_data(as_text=True)
        # assert "<h2>Make a Post</h2>" in html

    # def test_malformed_timeline_post(self):
    #     response = self.client.get("/timeline")
    #     assert response.status_code == 200
    #     html = response.get_data(as_text=True)
    #     assert "<h2>Make a Post</h2>" in html

        # response = self.client.get("/timeline")
        # assert response.status_code == 200
        # html = response.get_data(as_text=True)
        # assert "<h2>Make a Post</h2>" in html

        # response = self.client.get("/timeline")
        # assert response.status_code == 200
        # html = response.get_data(as_text=True)
        # assert "<h2>Make a Post</h2>" in html
        # POST request missing name
        # response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        # assert response.status_code == 400
        # html = response.get_data(as_text=True)
        # #Outputs contents of "html" when fail
        # #self.fail(html)
        # assert "Invalid name" in html

        # POST request with empty content
        # response = self.client.post("/api/timeline_post", data={"name": "John Doe" , "email": "john@example.com", "content": ""})
        # assert response.status_code == 400
        # html = response.get_data(as_text=True)
        # assert "Invalid content" in html

        # POST request with malformed email
        # response = self.client.post("/api/timeline_post", data={"name": "John Doe" , "email": "not-an-email", "content": "Hello world, I'm John!"})
        # assert response.status_code == 400
        # html = response.get_data(as_text=True)
        # assert "Invalid email" in html
