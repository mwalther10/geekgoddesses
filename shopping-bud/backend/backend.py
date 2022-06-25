from flask import Flask, request, jsonify
from flask_cors import CORS
import openfoodfacts

app = Flask(__name__)
CORS(app)


def extract_product_information(results):
    products = []
    keys = ["_id", "product_name", "image_url", "allergens_tags", "labels_tags", "packaging_tags",
            "stores_tags", "brands_tags", "nutriscore_grade", "categories_tags"]
    if "products" in results:
        results = results["products"]
    else:
        results = [result["product"] for result in results]
    for result in results:
        product = dict.fromkeys(keys)
        for key in keys:
            try:
                product[key] = result[key]
            except KeyError:
                product[key] = -1
        try:
            product["energy-kcal_100g"] = result["nutriments"]["energy-kcal_100g"]
        except KeyError:
            product["energy-kcal_100g"] = -1
        try:
            product["carbohydrates_100g"] = result["nutriments"]["carbohydrates_100g"]
        except KeyError:
            product["carbohydrates_100g"] = -1
        try:
            product["EF_single_score"] = result["ecoscore_extended_data"]["impact"]["likeliest_impacts"][
                "EF_single_score"]
        except KeyError:
            product["EF_single_score"] = -1

        products.append(product)
    return products


@app.route('/')
def index():
    return str(app.url_map)


@app.route('/search')
def search():
    query = request.args.get('query', default="", type=str)
    category = request.args.get('category', default="", type=str)
    allergens = request.args.get('allergens', default="", type=str).split(",")
    labels = request.args.get('labels', default="", type=str).split(",")
    packaging = request.args.get('packaging', default="", type=str).split(",")
    store = request.args.get('store', default="", type=str)
    brand = request.args.get('brand', default="", type=str)
    nutriscore = request.args.get('nutriscore', default="", type=str)
    nutriments = request.args.get('nutriments', default="", type=str).split(",")
    nutriments_op = request.args.get('nutriments_op', default="", type=str).split(",")
    nutriments_val = request.args.get('nutriments_val', default="", type=str).split(",")

    req = {
        "search_terms": query,
        "tagtype_0": "categories",
        "tag_contains_0": "contains",
        "tag_0": category,
        "page_size": 100
    }

    for i, nutriment in enumerate(nutriments):
        req = req | {"nutriment_{}".format(i): nutriment,
                     "nutriment_compare_{}".format(i): nutriments_op[i],
                     "nutriment_value_{}".format(i): nutriments_val[i],
                     }

    i = 1
    if len(allergens) > 1 or len(allergens[0]):
        for allergen in allergens:
            req = req | {"tagtype_{}".format(i): "allergens",
                         "tag_contains_{}".format(i): "does_not_contain",
                         "tag_{}".format(i): allergen,
                         }
            i += 1
    if len(labels) > 1 or len(labels[0]):
        for label in labels:
            req = req | {"tagtype_{}".format(i): "labels",
                         "tag_contains_{}".format(i): "contains",
                         "tag_{}".format(i): label,
                         }
            i += 1
    if len(packaging) > 1 or len(packaging[0]):
        for pack in packaging:
            req = req | {"tagtype_{}".format(i): "packaging",
                         "tag_contains_{}".format(i): "does_not_contain",
                         "tag_{}".format(i): pack,
                         }
            i += 1
    if len(store):
        req = req | {"tagtype_{}".format(i): "stores",
                     "tag_contains_{}".format(i): "contains",
                     "tag_{}".format(i): store,
                     }
        i += 1
    if len(brand):
        req = req | {"tagtype_{}".format(i): "brands",
                     "tag_contains_{}".format(i): "contains",
                     "tag_{}".format(i): brand,
                     }
        i += 1
    if len(nutriscore):
        req = req | {"tagtype_{}".format(i): "nutriscore_grade",
                     "tag_contains_{}".format(i): "contains",
                     "tag_{}".format(i): nutriscore,
                     }
        i += 1

    results = openfoodfacts.products.advanced_search(req)
    return jsonify(extract_product_information(results))


@app.route('/sample')
def sample():
    type = request.args.get('type', default="simple_pasta", type=str)

    if type == "simple_pasta":
        product_keys = ["4864394070560", "20717452", "8424536942122", "8003566000912", "8076809529433", "10022405"]
        prices = [2.08, 1.99, 15.90, 3.49, 3.46, 0.75]
    elif type == "eco_pasta":
        product_keys = ["4864394070560", "20717452", "8424536942122", "8003566000912", "8076809529433", "10022405"]
        prices = [2.08, 1.99, 15.90, 3.49, 3.46, 0.75]
    elif type == "nutri_pasta":
        product_keys = ["4864394070560", "20717452", "8424536942122", "8003566000912", "8076809529433", "10022405"]
        prices = [2.08, 1.99, 15.90, 3.49, 3.46, 0.75]
    elif type == "budget_pasta":
        product_keys = ["4864394070560", "20717452", "8424536942122", "8003566000912", "8076809529433", "10022405"]
        prices = [2.08, 1.99, 15.90, 3.49, 3.46, 0.75]

    results = [openfoodfacts.products.get_product(key) for key in product_keys]
    products = extract_product_information(results)
    for i, product in enumerate(products):
        product["price"] = prices[i]

    return jsonify(products)


if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer
    app.debug = True
    http_server = WSGIServer(('', 8000), app)
    http_server.serve_forever()
