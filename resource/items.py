
from flask_restful import Resource,reqparse

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="This cannot be blank")

    parser.add_argument('name',
    type=string,
    required=True,
    help="This cannot be blank")

    def get(self):
        data = Item.parser.parse_args()
        print(data)
        name = data["name"]
        item = product.query.filter_by(name=name).first()

        if item:
            ret = {
                "name": item.name,
                "price": item.price
            }
        else:
            ret = {
                "msg": "Not found"
            }
        return ret
    
    def post(self):
        data = Item.parser.parse_args()
        name = data["name"]
        price = data["price"]
        print(data)

        item = product(name=name,price=price)
        db.session.add(item)
        db.session.commit()
        ret = {
            "name": item.name,
            "price": item.price
        }
        return ret
    
    def delete(self):
        data = Item.parser.parse_args()
        name = data["name"]
        price = data["price"]

        item = product.query.filter_by(name=name)
        db.session.delete(item)
        db.session.commit()

        ret = {
            "msg": "Item Deleted"
        }
        return ret

    def put(self):
       
        data = Item.parser.parse_args()
        name = data["name"]
        price = data["price"]

        item = product.query.filter_by(name=name)
        item.price = price

        db.session.commit()

        ret = {
            "msg": "Item Updated with price {}".format(price)
        }
        return ret