from flask import Flask,request, jsonify, render_template
import webhook
import database


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def handle_webhook():
    # Ensure that the request has JSON data and it's valid
    if request.is_json:
        data = request.get_json()  # Use get_json() to retrieve JSON data
        # Assuming webhook.handle_podio_webhook expects 'data' as an argument
        result_data = webhook.handle_podio_webhook(data)
        return jsonify({"status": "success","data":result_data}), 200
    else:
        return jsonify({"error": "Request body is not JSON"}), 400




@app.route('/get_items', methods=['GET'])
def get_items():
    if request.method == 'GET':
        items = database.get_items()
        return jsonify(items)
    


if __name__ == '__main__':
    app.run(debug=True)