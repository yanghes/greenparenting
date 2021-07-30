class GPProcessor:
    def run(self, myjson):
        values=dict(myjson)
        img_url = values['image_url']
        
        import gp
        book_name, book_desc = gp.readBook(img_url)
        resp=dict({'book_name':book_name, 'book_description':book_desc})
        return resp
