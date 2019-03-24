
from bottle import run, route, view, get, post, request, static_file
from itertools import count

class comic_book:
    _ids = count(0)
    
    
    def __init__(self, name, image, stock, description):
        self.id = next(self._ids)
        self.comic_name = name
        self.comic_image = image
        self.comic_stock = stock
        self.comic_description = description
    
    
comic_test = [
    comic_book("Super Dude", "super_dude.jpg", 8, "this comic is about super dude"),
    comic_book("Lizard Man", "lizard_man.jpg", 12, "this comic is about Lizard man"),
    comic_book("Water Woman", "water_woman.jpg", 3, "this comic is about water woman")
    ]



@route("/")
@view("index")
def index(): #this function attatches decorators above
    pass


@route("/comics")
@view("comics")
def check_in():
    data = dict (comic_list = comic_test)
    return data    


@route('/picture/<filename>')
def saved_pics(filename):
    return static_file(filename, root = './images')


@route("/purchase/<comic_id>")
@view("purchase")
def purchase_page(comic_id):
    comic_id = int(comic_id)

    found_comic = None
    for comic in comic_test:
        if comic.id == comic_id:
            found_comic = comic
    data = dict(comic = found_comic)

    found_comic.comic_stock= found_comic.comic_stock -1

    return data


run(host="0.0.0.0", port = 8080, reloader=True, debug=True)