from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def products(products_data, categories_data, product_category_data):
    products_df = spark.createDataFrame(products_data, ["product_name"])
    categories_df = spark.createDataFrame(categories_data, ["category_name"])
    product_category_df = spark.createDataFrame(product_category_data, ["product_name", "category_name"])

    product_category_pairs = product_category_df.select("product_name", "category_name")

    products_with_categories = product_category_df.select("product_name").distinct()
    products_without_categories = products_df.join(products_with_categories, on="product_name", how="left_anti")

    products_without_categories_list = products_without_categories.select("product_name").rdd.flatMap(lambda x: x).collect()

    print("Пары 'Имя продукта - Имя категории':")
    product_category_pairs.show()

    print("Продукты без категорий:")
    for product in products_without_categories_list:
        print(product)

if __name__ == '__main__':
    products(None, None, None)