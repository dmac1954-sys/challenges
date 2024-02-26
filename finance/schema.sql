.open finance.db

CREATE TABLE transactions(id PRIMARY KEY, type TEXT NOT NULL, amount DECIMAL(10, 2), date TEXT, category_id INTEGER, description TEXT, FOREIGN KEY (category_id) REFERENCES categories(id));
CREATE TABLE categories(id PRIMARY KEY, category TEXT NOT NULL UNIQUE);
CREATE TABLE budgets(id PRIMARY KEY, category_id INTEGER, amount DECIMAL(10, 2), FOREIGN KEY (category_id) REFERENCES categories(id));

INSERT INTO categories(id, category)
VALUES 
(1, "Salary"),
(2, "Rent"),
(3, "Taxes"),
(4, "Shopping"),
(5, "Entertainment"),
(6, "Transport"),
(7, "Gifts"),
(8, "F and B");
