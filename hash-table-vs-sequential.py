import time

# Medicine Entity Class
class Medicine:
    def __init__(self, medicine_id, name, price, quantity):
        self.medicine_id = medicine_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (
            f"ID: {self.medicine_id} | "
            f"Name: {self.name} | "
            f"Price: RM{self.price:.2f} | "
            f"Quantity: {self.quantity}"
        )

# Hash Table Class
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, medicine_id):
        return medicine_id % self.size

    # Insert medicine using linear probing
    def insert(self, medicine):
        index = self.hash_function(medicine.medicine_id)

        for i in range(self.size):
            position = (index + i) % self.size

            if self.table[position] is None:
                self.table[position] = medicine
                return True

            if self.table[position].medicine_id == medicine.medicine_id:
                print("Medicine ID already exists!")
                return False

        print("Hash Table is full!")
        return False

    def search(self, medicine_id):
        index = self.hash_function(medicine_id)

        for i in range(self.size):
            position = (index + i) % self.size
            current = self.table[position]

            if current is None:
                break

            if current.medicine_id == medicine_id:
                return current

        return None

    def display(self):
        print("\nMedicine Table:")
        for i, value in enumerate(self.table):
            if value is not None:
                print(f"{i}: {value}")

# Array Search
def array_search(medicine_arr, medicine_id):
    for medicine in medicine_arr:
        if medicine.medicine_id == medicine_id:
            return medicine

    return None

# Medicine Record Generator
def generate_medicines(number):
    medicine_arr = []

    medicine_names = [
        "Paracetamol",
        "Ibuprofen",
        "Vitamin C",
        "Antacid",
        "Cough Syrup",
        "Cetirizine",
        "Loratadine",
        "Amoxicillin",
        "Omeprazole",
        "Vitamin B Complex",
        "Aspirin",
        "Diclofenac",
        "Loperamide",
        "Metformin",
        "Salbutamol",
        "Calcium Tablets",
        "Zinc Tablets",
        "Hydrocortisone Cream",
        "Antiseptic Cream",
        "Eye Drops",
        "Nasal Spray"
    ]

    for i in range(number):
        medicine_id = 1001 + i
        name = medicine_names[i % len(medicine_names)]

        price = round(5.00 + (i % 100) * 0.50, 2)
        quantity = 20 + (i % 100)

        medicine = Medicine(
            medicine_id,
            name,
            price,
            quantity
        )

        medicine_arr.append(medicine)
    return medicine_arr

# Main
def main():
    table_size = 1000
    ht = HashTable(table_size)

    # Generate a number of medicine records
    medicine_arr = generate_medicines(500)

    # Insert initial records into Hash Table
    for medicine in medicine_arr:
        ht.insert(medicine)

    # Main Menu
    while True:
        print("\n===== PHARMACY INVENTORY SYSTEM =====")
        print("1. Insert medicine")
        print("2. Search medicine")
        print("3. Display all medicines")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Insert medicine
        if choice == '1':
            medicine_id = int(input("Enter medicine ID: "))
            name = input("Medicine name: ")
            price = float(input("Price (RM): "))
            quantity = int(input("Quantity: "))

            if not name or price < 0 or quantity < 0:
                print("Invalid medicine details.")
                continue

            medicine = Medicine(medicine_id, name, price, quantity)

            if ht.insert(medicine):
                medicine_arr.append(medicine)
                print("Medicine inserted successfully!")

        # Search medicine
        elif choice == '2':
            medicine_id = int(input("Enter Medicine ID to search: "))

            # Hash Table Search
            start_time = time.perf_counter()
            hash_result = ht.search(medicine_id)
            hash_end_time = time.perf_counter()

            hash_time = hash_end_time - start_time

            # 1D Array Search
            start_time = time.perf_counter()
            array_result = array_search(medicine_arr, medicine_id)
            array_end_time = time.perf_counter()

            array_time = array_end_time - start_time

            # Display Hash Table Result
            print("\n===== HASH TABLE SEARCH =====")

            if hash_result is not None:
                print("Medicine Found!")
                print(hash_result)
            else:
                print("Medicine not found!")

            print(f"Search Time: {hash_time:.10f} seconds")

            # Display Array Result
            print("\n===== 1D ARRAY SEARCH =====")

            if array_result is not None:
                print("Medicine Found!")
                print(array_result)
            else:
                print("Medicine not found!")

            print(f"Search Time: {array_time:.10f} seconds")

        # Display list of medicines
        elif choice == '3':
            ht.display()

        # End program
        elif choice == '4':
            print("Exiting Pharmacy Inventory System.")
            break

if __name__ == "__main__":
    main()
