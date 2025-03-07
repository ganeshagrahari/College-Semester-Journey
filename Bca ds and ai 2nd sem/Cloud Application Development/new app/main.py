from flask import Flask 
app=(__name__) 

# making a page which show one book at a time 
@app.route('/')
def single_book(book_id):
    pass



#adding a new book using post method
@app.route('/home/books',methods=['POST'])    
def add_new_book():
    new_book=
    {
        'id':request.json['id'],
        'name':request.json['name'],
        'author':request.json['author']
    }
    books.append(new_book)
    return jsonify({'message':'Book addes sucesfully'})


#update an exiting book book data 
@app.route('/home/books/<int: book_id>',method=['POST'])
def update_book(book_id):
      for book in booms:
            if book['id']==book_id:
                  



if__name__== '__main__':
         app.run(debug=True,host='0.0.0.0',port=4000)




