import random

import pandas as pd
from faker import Faker

import core.data_access as da
from core.domain import (
    DimCustomer,
    DimProduct,
    DimPromoCode,
    FactSalesOrder,
    FactSalesOrderItem,
)

fake = Faker()


def gen_field(fake_function, percent_null=0):
    r = random.randint(0, 100)
    if r < percent_null:
        return None
    return fake_function()


def gen_dim_customer(num_rows=0, percent_null=0):
    record_list = []
    for i in range(num_rows):
        row = DimCustomer(
            customer_name=gen_field(fake.name),
            customer_email=gen_field(fake.email),
            customer_city=gen_field(fake.city, percent_null),
            customer_state=gen_field(fake.state_abbr, percent_null),
            customer_country=gen_field(fake.country_code, percent_null),
            customer_dob=gen_field(fake.date, percent_null),
            customer_job_title=gen_field(fake.job, percent_null),
            customer_company=gen_field(fake.company),
        )
        record_list.append(row)
    return pd.DataFrame().from_records(record_list)
