class NoImage(Exception):
    def __init__(self):
        super().__init__("The passed image was not a PIL.Image or bytes!")