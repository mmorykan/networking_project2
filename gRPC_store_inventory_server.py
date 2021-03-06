import grpc
import gRPC_store_inventory_pb2
import gRPC_store_inventory_pb2_grpc


class ProductInventory(gRPC_store_inventory_pb2_grpc.ProductInventoryServicer):
    """
    Class for gRPC server and methods
    Server is run from store_inventory_run_servers.py 
    """

    def __init__(self, shared_database):
        """
        Initializes the inventory object for the shared database
        """
        self.shared_database = shared_database

    
    def determineSuccessfulConnection(self, request, context):
        """
        Determines if the client can successfully connect to this server 
        """
        return gRPC_store_inventory_pb2.Empty()


    def update_product_fields(self, product):
        """
        Creates and returns the gRPC product object from the given product
        """
        return gRPC_store_inventory_pb2.Product(id_number=product['id_number'], name=product['name'], description=product['description'], manufacturer=product['manufacturer'], wholesale_cost=product['wholesale_cost'], sale_cost=product['sale_cost'], amount_in_stock=product['amount_in_stock'])


    def addProduct(self, request, context):
        """
        Adds a product to the product id and name databases as well as obtains a unique id for the new product
        Returns a product id
        May return a null product if if the requested name for the product is already in use
        """
        valid_id = self.shared_database.add_product(name=request.name, description=request.description, manufacturer=request.manufacturer, wholesale_cost=request.wholesale_cost, sale_cost=request.sale_cost, amount_in_stock=request.amount_in_stock)
        if valid_id != 'null product':
            return gRPC_store_inventory_pb2.ProductID(id_number=valid_id, name=request.name)
        else:
            return gRPC_store_inventory_pb2.ProductID(id_number=valid_id, name='Product already exists')


    def getProduct(self, request, context):
        """
        Returns the current product based on product id or name
        Returns a product
        Return value may be the null product if requested product id or name is invalid
        """
        product = self.shared_database.getProductByIDorName({'id_number': request.id_number, 'name': request.name})
        return self.update_product_fields(product)


    def updateProduct(self, request, context):
        """
        Update the specified fields for the given project. Can update every field except product id and name
        Returns a product
        Return value may be null product if the requested product id or name is invalid
        """
        product = self.shared_database.update_product(id_number=request.id_number, name=request.name, description=request.description, manufacturer=request.manufacturer, wholesale_cost=request.wholesale_cost, sale_cost=request.sale_cost, amount_in_stock=request.amount_in_stock)
        return self.update_product_fields(product)    


    def listProducts(self, request, context):
        """
        Lists all total products or just the products in stock and/or produced by a specified manufacturer
        Yields all appropriate products
        """
        product_list = self.shared_database.list_products(request.in_stock, request.manufacturer)
        for product in product_list:
            yield self.update_product_fields(product)


    def update_order_fields(self, order):
        """
        Converts a list of dictionaries of products and demands to a gRPC object of product and demand
        Returns an order
        """
        list_of_products = []
        for product_demand in order['products']:
            product_conversion = gRPC_store_inventory_pb2.ProductAndDemand(product=gRPC_store_inventory_pb2.ProductID(id_number=product_demand['id_number']), num_of_product=product_demand['number_of_product'])
            list_of_products.append(product_conversion)

        return gRPC_store_inventory_pb2.Order(id_number=order['id_number'], destination=order['destination'], date=order['date'], products=list_of_products, is_paid=order['is_paid'], is_shipped=order['is_shipped'])


    def get_list_of_products(self, product_list):
        """
        Converts gRPC product objects to dictionaries based on the specified identifiers
        Returns a list of dictionaries
        """
        list_of_products = []
        for product_and_demand in product_list:
            if product_and_demand.product.id_number:
                product_id_and_demand = {'id_number': product_and_demand.product.id_number}
            else:
                product_id_and_demand = {'name': product_and_demand.product.name}
            product_id_and_demand['number_of_product'] = product_and_demand.num_of_product

            list_of_products.append(product_id_and_demand)

        return list_of_products


    def addOrder(self, request, context):
        """
        Add an order which contains a destination, date, list of products and counts, shipped status, and paid status
        Returns an order id
        """
        list_of_products = self.get_list_of_products(request.products)
        order_id = self.shared_database.add_order(destination=request.destination, date=request.date, products=list_of_products, is_paid=request.is_paid, is_shipped=request.is_shipped)
        return gRPC_store_inventory_pb2.OrderID(id_number=order_id)

    
    def getOrder(self, request, context):
        """
        Receive an order based on the specified id value
        Returns an order
        Return value may be null order if the requested order id is invalid
        """
        order = self.shared_database.get_order(request.id_number)
        return self.update_order_fields(order)


    def updateOrder(self, request, context):
        """
        Updates the specified fields for an order.
        Can update destination, date, shipped status, and paid status
        Returns an order
        Return value may be null order if the requested order id is invalid
        """
        order = self.shared_database.update_order(id_number=request.id_number, destination=request.destination, date=request.date, is_shipped=request.is_shipped, is_paid=request.is_paid)
        return self.update_order_fields(order)


    def addProductsToOrder(self, request, context):
        """
        Add products to an existing order or increase the amounts of existing products already in the order
        Returns an order
        Return value may be null order if the requested order id is invalid
        """
        list_of_products = self.get_list_of_products(request.products)
        order = self.shared_database.add_products_to_order(request.id_number, list_of_products)
        return self.update_order_fields(order)


    def removeProductsFromOrder(self, request, context):
        """
        Removes products from an order specified by the order id or decrease the amounts of existing products within the order
        Returns an order
        Return value may be null order if the requested order id is invalid
        """
        list_of_products = self.get_list_of_products(request.products)
        order = self.shared_database.remove_products_from_order(request.id_number, list_of_products)
        return self.update_order_fields(order)


    def listOrders(self, request, context):
        """
        Lists all the orders based on shipped status and paid status or all total orders
        Yields all appropriate orders
        """
        list_of_orders = self.shared_database.list_orders(request.is_shipped, request.is_paid)
        for order in list_of_orders:
            yield self.update_order_fields(order)


    def clearDatabase(self, request, context):
        """
        Clears the database
        """
        self.shared_database.clear_database()
        return gRPC_store_inventory_pb2.Empty()
