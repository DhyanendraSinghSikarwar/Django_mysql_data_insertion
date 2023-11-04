from myapp.models import *
import threading
from django.db import transaction


# def update_model(Transaction,data_chunk):
#     with transaction.atomic():
#         for item in data_chunk:
#             obj = Transaction.objects.get(id=item['id'])
#             obj.id = item['id']
#             obj.amount=item['amount']
#             obj.description=item['description']
#             obj.original_description=item['original_description']
#             obj.transaction_at=item['transaction_at']
#             obj.notes=item['notes']
#             obj.payload=item['payload']
#             obj.account_id=item['account_id']
#             obj.kreditz_transaction_type=item['kreditz_transaction_type']
#             obj.internal_transfer=item['internal_transfer']
#             obj.balance=item['balance']
#             obj.created_at=item['created_at']
#             obj.updated_at=item['updated_at']
#             obj.kreditz_income_type=item['kreditz_income_type']
#             obj.formatted_description=item['formatted_description']
#             obj.category_id=item['category_id']
#             obj.matched_by=item['matched_by']

#             obj.save()


def insert_model(data):
    with transaction.atomic():
        for item in data:
            new_transaction = Tf_20230920(
                # id=item['id'],
                ApplicationId=item['ApplicationId'],
                ApplicationDate=item['ApplicationDate'],
                IdRow=item['IdRow'],
                AccountId=item['AccountId'],
                Balance=item['Balance'],
                Bank=item['Bank'],
                transactionDate=item['transactionDate'],
                transactionAmount=item['transactionAmount'],
                transactionClass=item['transactionClass'],
                transactionDescription=item['transactionDescription'],
                predictedCategoryDescription=item['predictedCategoryDescription'],
                # created_at=item['created_at'],
                # updated_at=item['updated_at']
            )
            new_transaction.save()



def save_trans(transac):
    
    batch_size = 500000
    batches = [transac[i:i + batch_size] for i in range(0, len(transac), batch_size)]
    import pdb
    for trans in batches:
        #insert_model(trans)
        num_threads = 256
        chunk_size = len(trans) // num_threads

        threads = []
        for i in range(num_threads):
            start = i * chunk_size
            end = start + chunk_size if i < num_threads - 1 else len(trans)
            data_chunk = trans[start:end]
            
            #pdb.set_trace()
            thread = threading.Thread(target=insert_model, args=(data_chunk,))
            thread.start()
            threads.append(thread)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

def save_trans2(transac):
    batch_size = 100
    batches = [transac[i:i + batch_size] for i in range(0, len(transac), batch_size)]
    import pdb
    for trans in batches:
        insert_model(trans)
    
    # batch_size = 100
    # batches = [transac[i:i + batch_size] for i in range(0, len(transac), batch_size)]
    # import pdb
    # for trans in batches:
    #     #insert_model(trans)
    #     num_threads = 2
    #     chunk_size = len(trans) // num_threads

    #     threads = []
    #     for i in range(num_threads):
    #         start = i * chunk_size
    #         end = start + chunk_size if i < num_threads - 1 else len(trans)
    #         data_chunk = trans[start:end]
            
    #         #pdb.set_trace()
    #         thread = threading.Thread(target=insert_model, args=(data_chunk,Tf20230920mkes2022))
    #         thread.start()
    #         threads.append(thread)

    #     # Wait for all threads to complete
    #     for thread in threads:
    #         thread.join()