from flask import Flask
from flask_restful import Api, Resource
from src.controllers.Quoters import create_quoter, get_all_quoters, get_spefic_quoter
from src.controllers.Products import create_product, delete_product, get_all_products, get_all_female_products, get_all_male_products, get_spefic_product, delete_product

app = Flask(__name__)

# quoters
app.add_url_rule('/quoters', 'quoters', get_all_quoters, methods=['GET'])
app.add_url_rule('/quoters/<quoter_id>', 'get specific quoter', get_spefic_quoter, methods=['GET'])
app.add_url_rule('/quoters', 'create quoter', create_quoter, methods=['POST'])


# products
app.add_url_rule('/products', 'products', get_all_products, methods=['GET'])
app.add_url_rule('/products/female', 'female products', get_all_female_products, methods=['GET'])
app.add_url_rule('/products/male', 'male products', get_all_male_products, methods=['GET'])
app.add_url_rule('/products/<product_id>', 'get specific product', get_spefic_product, methods=['GET'])
app.add_url_rule('/products', 'create product', create_product, methods=['POST'])
app.add_url_rule('/products/<product_id>', 'delete specific product', delete_product, methods=['DELETE'])




if __name__ == '__main__':
  app.run(debug=True)