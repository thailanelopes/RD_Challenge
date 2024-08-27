import logging
import time
from bisect import bisect_right

logging.basicConfig(level=logging.INFO)

def customerSuccessBalancing(customer_success, customers, customer_success_away):

    if not customer_success or not customers:
        logging.error("Customer Success ou Clientes não podem ser vazios.")
        return 0

    available_cs = sorted(
        [cs for cs in customer_success if cs['id'] not in customer_success_away],
        key=lambda cs: cs['nivel']
    )

    if not available_cs:
        logging.error("Nenhum Customer Success disponível.")
        return 0

    cs_customer_count = {cs['id']: 0 for cs in available_cs}

    for customer in customers:
        pos = bisect_right([cs['nivel'] for cs in available_cs], customer['nivel'])
        if pos < len(available_cs):
            cs_customer_count[available_cs[pos]['id']] += 1

    max_clients = max(cs_customer_count.values())
    best_cs = [cs_id for cs_id, count in cs_customer_count.items() if count == max_clients]

    if len(best_cs) > 1:
        logging.info("Empate entre Customer Success.")
        return 0
    else:
        return best_cs[0]

def benchmark():
    sizes = [1000, 10000, 100000]
    for size in sizes:
        customer_success = [{'id': i, 'nivel': i * 10} for i in range(1, size // 10)]
        customers = [{'id': i, 'nivel': i * 5} for i in range(1, size)]
        customer_success_away = []

        start_time = time.time()
        customerSuccessBalancing(customer_success, customers, customer_success_away)
        end_time = time.time()

        logging.info(f"Tamanho {size}: {end_time - start_time:.4f} segundos")

if __name__ == '__main__':
    benchmark()
