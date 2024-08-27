import unittest
from customerSuccessBalancing import customerSuccessBalancing

class TestCustomerSuccessBalancing(unittest.TestCase):
    def test_case_1(self):
        customer_success = [
            {'id': 1, 'nivel': 60},
            {'id': 2, 'nivel': 20},
            {'id': 3, 'nivel': 95},
            {'id': 4, 'nivel': 75}
        ]

        customers = [
            {'id': 1, 'nivel': 90},
            {'id': 2, 'nivel': 20},
            {'id': 3, 'nivel': 70},
            {'id': 4, 'nivel': 40},
            {'id': 5, 'nivel': 60},
            {'id': 6, 'nivel': 10}
        ]

        customer_success_away = [2, 4]

        result = customerSuccessBalancing(customer_success, customers, customer_success_away)
        self.assertEqual(result, 1)

    def test_case_large_input(self):
        customer_success = [{'id': i, 'nivel': i * 10} for i in range(1, 100)]
        customers = [{'id': i, 'nivel': i * 5} for i in range(1, 1000)]
        customer_success_away = [i for i in range(1, 10)]

        result = customerSuccessBalancing(customer_success, customers, customer_success_away)
        self.assertTrue(result > 0)

    def test_case_all_cs_unavailable(self):
        customer_success = [
            {'id': 1, 'nivel': 60},
            {'id': 2, 'nivel': 20},
            {'id': 3, 'nivel': 95},
            {'id': 4, 'nivel': 75}
        ]

        customers = [
            {'id': 1, 'nivel': 90},
            {'id': 2, 'nivel': 20},
            {'id': 3, 'nivel': 70},
            {'id': 4, 'nivel': 40}
        ]

        customer_success_away = [1, 2, 3, 4]

        result = customerSuccessBalancing(customer_success, customers, customer_success_away)
        self.assertEqual(result, 0)

    def test_case_no_customers(self):
        customer_success = [
            {'id': 1, 'nivel': 60},
            {'id': 2, 'nivel': 20}
        ]
        customers = []
        customer_success_away = []

        result = customerSuccessBalancing(customer_success, customers, customer_success_away)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
