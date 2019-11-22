import core.data_access as da
import core.data_gen as dg

NUM_CUSTOMERS = 100
PERCENT_NULL_CUSTOMERS = 10


def load_dim_customer():
    df = dg.gen_dim_customer(NUM_CUSTOMERS, PERCENT_NULL_CUSTOMERS)
    da.save_dim_customer_csv(df)
    da.push_sws_dim_customer()
