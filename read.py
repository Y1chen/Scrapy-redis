import redis
import json
import pandas as pd
from sqlalchemy import create_engine


# 将数据写入mysql
def process_item():
    # save = pd.DataFrame([item])
    conn = create_engine('mysql+mysqldb://root:980205@localhost:3306/Recommendation_system?charset=utf8')
    # pd.io.sql.to_sql(save, 'shanghai_java', con=conn, if_exists='append', index=False)

def main():
    # ITEM_KEY = 'Scrapy_Redis_Spider:items'
    # r = redis.StrictRedis(host='47.93.221.209', port=6379)
    # for _ in range(r.llen(ITEM_KEY)):
    #     data = r.lpop(ITEM_KEY)
    #     item = json.loads(data.decode('utf8'))
    #     process_item(item)
    process_item()

if __name__ == '__main__':
    main()
