from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for tweets
tweets = []
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    if not username or username in users:
        return jsonify({'error': 'Invalid or duplicate username'}), 400
    users[username] = []
    return jsonify({'message': 'User registered'}), 201

@app.route('/tweet', methods=['POST'])
def tweet():
    data = request.json
    username = data.get('username')
    content = data.get('content')
    if not username or username not in users or not content:
        return jsonify({'error': 'Invalid data'}), 400
    tweet = {'username': username, 'content': content}
    tweets.append(tweet)
    users[username].append(tweet)
    return jsonify({'message': 'Tweet posted'}), 201

@app.route('/timeline/<username>', methods=['GET'])
def timeline(username):
    if username not in users:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'tweets': users[username]}), 200

@app.route('/tweets', methods=['GET'])
def all_tweets():
    return jsonify({'tweets': tweets}), 200

if __name__ == '__main__':
    app.run(debug=True)