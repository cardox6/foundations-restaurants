

class Restaurant():
    def __init__(self, name, neighbourhood):
        self.name = name
        self.neighbourhood = neighbourhood

# functions to create html elements
def start_html_file():
    return("""
        <html>
        <body>
        <h1>Test</h1>
        """)

def end_of_html_file():
    return("""
        </body>
        </html>
        """)


# loop throgh restaurant file
def restaurant_reader():
    restaurant_html = ""
    with open ("restaurants.txt", "r") as restaurants_file:
        for line in restaurants_file:
            restaurants = line.split(",")
            restaurant = Restaurant(restaurants[0], restaurants[1]) 
            restaurant_html += (f"""<h1>{restaurant.name}, {restaurant.neighbourhood}</h1>""")
    return restaurant_html

def main_html():
    return(start_html_file(), restaurant_reader(), end_of_html_file())