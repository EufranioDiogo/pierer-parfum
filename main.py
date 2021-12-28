from flask import Flask
from flask_cors import CORS
from src.controllers.Quoters import create_quoter, get_all_quoters, get_spefic_quoter
from src.controllers.Products import create_product, delete_product, get_all_products, get_all_female_products, get_all_male_products, get_spefic_product, delete_product
from src.controllers.Origem import get_all_origems, get_spefic_origem, delete_origem, create_origem
from src.controllers.Family import get_all_families, get_spefic_family, delete_family, create_family
from src.controllers.Account import create_account, account_verification

app = Flask(__name__)
CORS(app)


# quoters
app.add_url_rule('/quoters', 'quoters', get_all_quoters, methods=['GET'])
app.add_url_rule('/quoters/<quoter_id>', 'get specific quoter', get_spefic_quoter, methods=['GET'])
app.add_url_rule('/quoters', 'create quoter', create_quoter, methods=['POST'])


# families
app.add_url_rule('/families', 'families', get_all_families, methods=['GET'])
app.add_url_rule('/families/<family_id>', 'get specific family', get_spefic_family, methods=['GET'])
app.add_url_rule('/families', 'create family', create_family, methods=['POST'])
app.add_url_rule('/families/<family_id>', 'delete specific family', delete_family, methods=['DELETE'])


# origem
app.add_url_rule('/origems', 'origems', get_all_origems, methods=['GET'])
app.add_url_rule('/origems/<origem_id>', 'get specific origem', get_spefic_origem, methods=['GET'])
app.add_url_rule('/origems', 'create origem', create_origem, methods=['POST'])
app.add_url_rule('/origems/<origem_id>', 'delete specific origem', delete_origem, methods=['DELETE'])


# products
app.add_url_rule('/products', 'products', get_all_products, methods=['GET'])
app.add_url_rule('/products/female', 'female products', get_all_female_products, methods=['GET'])
app.add_url_rule('/products/male', 'male products', get_all_male_products, methods=['GET'])
app.add_url_rule('/products/<product_id>', 'get specific product', get_spefic_product, methods=['GET'])
app.add_url_rule('/products', 'create product', create_product, methods=['POST'])
app.add_url_rule('/products/<product_id>', 'delete specific product', delete_product, methods=['DELETE'])


# account
app.add_url_rule('/account', 'account', create_account, methods=['POST'])
app.add_url_rule('/account/verify', 'account verify', account_verification, methods=['POST'])


if __name__ == '__main__':
  app.run(debug=True)