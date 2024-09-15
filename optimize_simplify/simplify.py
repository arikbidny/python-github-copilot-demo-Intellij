import csv
from datetime import datetime

class CustomerTransaction:
    def __init__(self, transaction_id, customer_id, amount, date_str):
        self.transaction_id = transaction_id
        self.customer_id = customer_id
        self.amount = float(amount)
        self.date = datetime.strptime(date_str, '%Y-%m-%d')

    def __repr__(self):
        return f"Transaction({self.transaction_id}, {self.customer_id}, {self.amount}, {self.date})"

class TransactionProcessor:
    def __init__(self):
        self.transactions = []
        self.customers = {}

    def load_transactions_from_csv(self, file_path):
        try:
            with open(file_path, newline='') as csvfile:
                next(csvfile)  # Skip the header
                for row in csv.reader(csvfile):
                    if len(row) == 4:
                        transaction = CustomerTransaction(*row)
                        self.transactions.append(transaction)
                        self.customers.setdefault(transaction.customer_id, []).append(transaction)
        except Exception as e:
            print(f"Error loading transactions: {e}")

    def filter_transactions_by_date(self, start_date_str, end_date_str):
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            return [t for t in self.transactions if start_date <= t.date <= end_date]
        except Exception as e:
            print(f"Error filtering transactions by date: {e}")
            return []

    def get_total_amount_by_customer(self, customer_id):
        return sum(t.amount for t in self.customers.get(customer_id, []))

    def get_average_transaction_amount_by_customer(self, customer_id):
        transactions = self.customers.get(customer_id, [])
        return sum(t.amount for t in transactions) / len(transactions) if transactions else 0

    def get_highest_transaction_amount(self):
        return max((t.amount for t in self.transactions), default=0)

    def get_transaction_summary(self):
        return {
            'total_transactions': len(self.transactions),
            'total_customers': len(self.customers),
            'total_amount': sum(t.amount for t in self.transactions),
            'highest_transaction': self.get_highest_transaction_amount()
        }

def main():
    processor = TransactionProcessor()
    processor.load_transactions_from_csv('transactions.csv')
    print(f"Filtered transactions: {processor.filter_transactions_by_date('2023-01-01', '2023-12-31')}")
    customer_id = 'C001'
    print(f"Total amount spent by customer {customer_id}: {processor.get_total_amount_by_customer(customer_id)}")
    print(f"Average transaction amount for customer {customer_id}: {processor.get_average_transaction_amount_by_customer(customer_id)}")
    print(f"Highest transaction amount: {processor.get_highest_transaction_amount()}")
    print(f"Transaction summary: {processor.get_transaction_summary()}")

if __name__ == "__main__":
    main()