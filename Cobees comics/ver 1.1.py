
from bottle import run, route, view, get, post, request
from itertools import count

class comic_book:
    _ids = count(0)
    
    def __init__(self, name, image, stock):
        self.id = next(self._ids)
        self.comic_name = name
        self.comic_image = image
        self.comic_stock = stock
    
    
comic_test = [
    comic_book("Super Dude", "image", 8),
    comic_book("Lizard Man", "image", 12),
    comic_book("Water Woman", "image", 3)
    ]





































run(host="0.0.0.0", port = 8080, reloader=True, debug=True)