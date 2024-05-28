from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample user data
users = [
    {'username': 'saaras', 'classes': ['AP Calculus AB', 'AP World History', 'Physics 1']},
    {'username': 'sri', 'classes': ['AP Calculus AB', 'World History', 'Honors Humanities']},
    {'username': 'austin', 'classes': ['AP Calculus BC', 'AP World History', 'Honors Humanities']},
    {'username': 'erox', 'classes': ['AP Calculus AB', 'AP World History', 'Honors Humanities']},
    {'username': 'cayden', 'classes': ['AP Calculus AB', 'World History', 'English 3']},
    {'username': 'alice', 'classes': ['Biology', 'Chemistry', 'AP US History']},
    {'username': 'bob', 'classes': ['Physics 1', 'Honors Humanities', 'AP US History']},
    {'username': 'charlie', 'classes': ['World History', 'English 3', 'Biology']},
    {'username': 'diana', 'classes': ['Chemistry', 'AP World History', 'AP Calculus BC']},
    {'username': 'ethan', 'classes': ['AP US History', 'Honors Humanities', 'AP Calculus AB']}
]

@app.route('/api/get_user_classes', methods=['GET'])
def get_user_classes():
    username = request.args.get('username')
    user = next((user for user in users if user['username'] == username), None)
    if user:
        # Sorting example
        sorted_classes = sorted(user['classes'])  # Sort classes alphabetically
        
        return jsonify({'username': user['username'], 'classes': sorted_classes})
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/api/search_user_classes', methods=['GET'])
def search_user_classes():
    search_term = request.args.get('search')
    result = [user for user in users if search_term in user['classes']]
    return jsonify(result)

@app.route('/api/all_users', methods=['GET'])
def all_users():
    # 2D iteration example: Processing a 2D list of users and their classes
    user_class_grid = [[user['username'], *user['classes']] for user in users]
    processed_grid = []
    for row in user_class_grid:
        processed_row = [f"Processed-{item}" for item in row]
        processed_grid.append(processed_row)

    return jsonify(users=users, processed_grid=processed_grid)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8132)
