class Post:
    def __init__(self, post):
        self.id = post["id"]
        self.title = post["title"]
        self.sub = post["subtitle"]
        self.body = post["body"]
