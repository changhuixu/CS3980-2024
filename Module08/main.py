import asyncio
import os

from db import init_db
from models.product import Category, Product


async def main():
    await init_db()

    chocolate = Category(
        name="Chocolate", description="A preparation of roasted cacao seeds"
    )

    tony_bar = Product(name="TTTT", price=8.99, category=chocolate)
    mars_bar = Product(name="MMMM", price=5.99, category=chocolate)

    print(tony_bar)
    await tony_bar.insert()
    print(tony_bar.id)

    await mars_bar.insert()
    products = await Product.find(Product.price < 10).to_list()
    print(products)


asyncio.run(main())
