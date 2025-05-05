from quart import Quart, jsonify

app = Quart(__name__)

@app.route('/api/test', methods=['GET'])
async def test():
    """Test endpoint to verify the backend is running."""
    return jsonify({"message": "Backend is running successfully!"})

if __name__ == '__main__':
    app.run()