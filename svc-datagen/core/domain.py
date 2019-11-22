""" 
Author: Rafael Battesti - rafaelbattesti.com
Since: 2019-11-20
Module to declare the domain objects utilized in the datagen service
"""

from collections import namedtuple

DimCustomer = namedtuple(
    "DimCustomer",
    [
        "customer_name",
        "customer_email",
        "customer_city",
        "customer_state",
        "customer_country",
        "customer_dob",
        "customer_job_title",
        "customer_company",
    ],
)

DimProduct = namedtuple("DimProduct", ["product_content", "product_price"])
DimPromoCode = namedtuple("DimPromoCode", ["promo_code_id", "promo_code_discount"])
FactSalesOrder = namedtuple(
    "FactSalesOrder",
    [
        "customer_id",
        "sales_order_created",
        "sales_order_updated",
        "sales_order_fulfilled",
    ],
)
FactSalesOrderItem = namedtuple(
    "FactSalesOrderItem", ["sales_order_id", "product_id", "sales_order_item_qty"]
)
