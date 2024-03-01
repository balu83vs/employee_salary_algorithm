from db_con import DbConnector
from alg import Alg


# основная программа
def main(conditions):
    current_collection = DbConnector().choice_collection()
    result = Alg(conditions.get('dt_from'),
                 conditions.get('dt_upto'),
                 conditions.get('group_type'),
                 current_collection).get_result()
    return result
    

# точка входа
if __name__ == '__main__':
    conditions = {
   "dt_from": "2022-09-01T00:00:00",
   "dt_upto": "2022-12-31T23:59:00",
   "group_type": "month"
}

    print(main(conditions))