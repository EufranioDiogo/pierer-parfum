from flask import Flask
from flask_cors import CORS
from controllers.Quoters import create_quoter, get_all_quoters, get_spefic_quoter
from controllers.Products import create_product, delete_product, get_all_products, get_all_female_products, get_all_male_products, get_spefic_product, delete_product
from controllers.Account import create_account, account_verification
from blue_prints.home import home as homeBlueprint
from blue_prints.homens import homens as homensBlueprint
from blue_prints.mulheres import mulheres as mulheresBlueprint
from blue_prints.about import about as aboutBlueprint
from blue_prints.buy import buy as buyBlueprint
from blue_prints.auth import auth as authBlueprint




app = Flask(__name__)
CORS(app)

app.register_blueprint(homeBlueprint, url_prefix="")
app.register_blueprint(homensBlueprint, url_prefix="/homens")
app.register_blueprint(mulheresBlueprint, url_prefix="/mulheres")
app.register_blueprint(aboutBlueprint, url_prefix="/about")
app.register_blueprint(buyBlueprint, url_prefix="/buy")
app.register_blueprint(authBlueprint, url_prefix="/auth")


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

# account
app.add_url_rule('/account', 'account', create_account, methods=['POST'])
app.add_url_rule('/account/verify', 'account verify', account_verification, methods=['POST'])




if __name__ == '__main__':
  app.run(debug=True)