def get_name(record_store):
    return record_store["name"]

def find_record_by_title(title, record_store):
    for record in record_store["records"]:
        if record["title"] == title:
            return record
    return None


def sell_record(record, record_store):

    # update the record_store money value so that its increased by the price of the record
    
    #this is how to in long hand writing
    # money_value = record_store["money"]
    # record_price = record["price"]
    # new_money_value = money_value + record_price
    # record_store["money"] = new_money_value


    # this is the one line method 
    record_store["money"] += record["price"]

    #remove record from th elist
    record_store["records"].remove(record)




