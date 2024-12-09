from flask import Flask, request, jsonify
from fashion_dataset import FASHION_ITEMS  

app = Flask(__name__)

@app.route('/api/fashion', methods=['GET'])
def get_fashion_items():
    try:
        # Parse query parameters
        filters = request.args
        category = filters.get('category')  # Filter by category
        price_min = float(filters.get('price_min', 0))  # Minimum price
        price_max = float(filters.get('price_max', float('inf')))  # Maximum price
        size = filters.get('size')  # Filter by size
        color = filters.get('color')  # Filter by color
        designer = filters.get('designer')  # Filter by designer
        rating = float(filters.get('rating', 0))  # Minimum rating
        sort_by = filters.get('sort_by', 'price')  # Sort by field (default: price)
        order = filters.get('order', 'asc')  # Sort order (default: ascending)
        page = int(filters.get('page', 1))  # Current page (default: 1)
        limit = int(filters.get('limit', 10))  # Items per page (default: 10)

        # Apply filters
        filtered_items = FASHION_ITEMS
        if category:
            filtered_items = [item for item in filtered_items if item['category'] == category]
        if price_min or price_max:
            filtered_items = [item for item in filtered_items if price_min <= item['price'] <= price_max]
        if size:
            filtered_items = [item for item in filtered_items if size in item['size']]
        if color:
            filtered_items = [item for item in filtered_items if item['color'].lower() == color.lower()]
        if designer:
            filtered_items = [item for item in filtered_items if item['designer'].lower() == designer.lower()]
        if rating:
            filtered_items = [item for item in filtered_items if item['rating'] >= rating]

        # Sort items
        reverse = (order == 'desc')
        filtered_items.sort(key=lambda x: x.get(sort_by, 0), reverse=reverse)

        # Paginate results
        start = (page - 1) * limit
        end = start + limit
        paginated_items = filtered_items[start:end]

        # Return response
        return jsonify(paginated_items), 200

    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
