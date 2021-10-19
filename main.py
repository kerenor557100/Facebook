
import facebook
import requests


access_token = "my facebook token"
user = "my user id"


def some_action(post):
  
    print(post)


graph = facebook.GraphAPI(access_token)
posts = graph.get_connections(user, "posts")


while True:
    try:

        [some_action(post=post) for post in posts["data"]]
        posts = requests.get(posts["paging"]["next"]).json()
    except KeyError:

        break
