Feature: Product management

Scenario: Creating a product
  Given a user is authenticated
  When the user creates a product
  Then the product is created successfully

Scenario: Updating a product
  Given a product exists
  When the user updates the product
  Then the product is updated successfully
