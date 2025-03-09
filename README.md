<strong>Product Management</strong>

Product Management is a simple Python-based system for managing products. It allows you to add, remove, modify, and view products in an inventory, as well as export the data to a CSV file.
Features

    Add products: Insert new products with name, price, and quantity.

    Remove products: Delete products from the inventory by index.

    Modify products: Update the price, name, or quantity of an existing product.

    View products: Check specific product details or list all items in the inventory.

    Export to CSV: Save inventory data to a CSV file.

<strong>How to Use</strong>
Prerequisites

    Python 3.x installed.

Running the Project:

    Clone the repository or download the product_management.py file.

    Navigate to the directory where the file is located.

    Run the script:
    bash
    Copy

    python product_management.py

    Follow the on-screen instructions to interact with the system.

Menu Options:

    Add items: Add new products to the inventory.

    Delete items: Remove products from the inventory.

    Show items: View product details.

    Modify items: Update product information.

    Export to CSV: Save inventory data to test.csv.

    Exit: Close the program.

Code Structure

    product class:

        Manages the global prod list.

        Includes the csv() method to export data to a CSV file.

    inventory class (inherits from product)**:

        Handles adding, removing, modifying, and viewing products.

        Uses global lists (price, iden, quantity) to store product details.

Contributing

Contributions are welcome! Fork the repository, create a new branch, and submit a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for details.
