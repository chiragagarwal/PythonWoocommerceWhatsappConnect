from woocommerce import API

wcapi = API(
    url="http://localhost/lab/pythonwoocommerce",
    consumer_key="XX_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    consumer_secret="XX_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    version="wc/v3"
)

data = {
    "name": "Demo Product Name",
    "description": "Demo Product Description",
    "categories": [
        {
            "id": 16
        },
        {
            "id": 17
        }
    ],
    "images": [
        {
            "src": "http://localhost/DemoSite/wp-content/uploads/2020/07/Image-4.jpeg"
        },
        {
            "src": "http://localhost/DemoSite/wp-content/uploads/2018/01/Image-1.jpeg"
        }
    ]
}

print(wcapi.post("products", data).json())
