from src.findb import add_transaction, create_connection

DB_PATH = "/workspaces/challenges/finance/finance.db"

class Transaction:
    def __init__(self, action, amount, date, category_id, description):
        self.action = action
        self.amount = amount
        self.date = date
        self.category_id = category_id
        self.description = description

    def __str__(self):
        return f"Type is {self.action}\nAmount is {self.amount}\nDate is {self.date}\nCategory is {self.category_id}\nDescription is {self.description}"

    def update_db(self):
        conn = create_connection(DB_PATH)
        with conn:
            transaction = (
                self.action,
                self.amount,
                self.date,
                self.category_id,
                self.description,
            )
            add_transaction(conn, transaction)
