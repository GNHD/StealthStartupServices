# StealthStartupServices
Implement a crucial  component of our marketplace: a filter service that helps users find fashion items based on  various criteria.

# Setup Instructions
# Clone the repository

git clone https://github.com/StealthStartupServices

cd StealthStartupServices

# API DOCUMENTATION
Endpoint: /api/fashion

Method: GET

# Query Parameters:
category (optional): Filter items by category (e.g., "Dresses", "Shoes", "Accessories").

price_min (optional): Minimum price of the item.

price_max (optional): Maximum price of the item.

size (optional): Size(s) of the item (e.g., "S", "M", "L").

color (optional): Color of the item (e.g., "Black", "Red").

designer (optional): Designer or brand name (e.g., "Nike", "Gucci").

rating (optional): Minimum rating (between 1 and 5).

sort_by (optional): Sort by attribute ("price" or "rating"). Default is "price".

order (optional): Sort order ("asc" or "desc"). Default is "asc".

page (optional): Page number for pagination. Default is 1.

limit (optional): Number of items per page. Default is 10.

Response:

The API will return a paginated list of filtered, sorted fashion items.


Success Response (200 OK):

[

  {
    
    "id": 1,
    "name": "Men's Casual T-Shirt",
    "category": "Dresses",
    "price": 30.00,
    "size": ["S", "M", "L"],
    "color": "Blue",
    "designer": "Nike",
    "rating": 4.5
  },
  
  
  {
   
    "id": 2,
    "name": "Women's Leather Jacket",
    "category": "Dresses",
    "price": 250.00,
    "size": ["M", "L"],
    "color": "Black",
    "designer": "Gucci",
    "rating": 5.0
  
  }

]


# Design Choices

Data Structure: The fashion items are stored in a list of dictionaries, with each dictionary representing an individual item. This was chosen for simplicity and because the dataset is small enough to be held in memory.


 Filter and Sorting Logic: The filtering and sorting are implemented as list comprehensions for efficiency and clarity. The filters and sorts are applied in sequence, allowing flexible user queries. Sorting is done using Python’s sort method and a lambda function.


Pagination: Pagination is implemented by slicing the filtered and sorted list based on the page and limit parameters. This ensures only the requested portion of the data is returned.


Error Handling: Basic error handling is included for cases like invalid input (e.g., non-numeric values for price or rating) and other unforeseen errors. This ensures the API is robust and user-friendly.

# Assumptions Made

In-memory Storage: The dataset is stored in memory, meaning no persistent database is required. This is suitable for small datasets but would not scale well for larger applications.

Fixed Number of Fashion Items: A static dataset of fashion items is used, which means the API does not dynamically update or change based on real-world data.

Basic Filters: The filtering logic assumes simple string and numerical comparisons (e.g., exact matches for category and designer, ranges for price, and rating comparisons for rating).

Sort Options: Sorting is limited to two attributes: price and rating. More sorting options could be added based on future requirements.

No Authentication: This API does not include any authentication or authorization mechanisms. In a production system, user authentication might be required for certain operations.

# Potential Improvements (With More Time)

Persistent Database: Instead of keeping the data in memory, a database (such as PostgreSQL or MongoDB) could be integrated for better scalability and persistence.

Advanced Filtering: Implement more complex filtering capabilities (e.g., multiple size selections, filtering by multiple colors, price ranges with sliders).

Full-Text Search: Implement a full-text search engine for more sophisticated item searches, like fuzzy matching or searching by item descriptions.

Authentication and Authorization: Add user authentication for personalized experiences (e.g., saving favorite items, managing shopping carts).

Caching: Implement caching for frequently accessed queries to improve performance, especially for expensive filtering and sorting operations.

Dynamic Data Updates: Allow for real-time updates to the fashion items dataset via an admin interface or API.

Front-End UI: Develop a user-friendly front-end interface to interact with the API, allowing users to apply filters, sort results, and navigate through pages.

Testing and Documentation: Include unit tests and a more comprehensive documentation system (e.g., Swagger) to make the API easier to understand and use.

