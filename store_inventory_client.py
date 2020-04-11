import XML_store_inventory_client
import gRPC_store_inventory_client
import xmlrpc.client
import sys
import argparse


def get_client(server, address, port):
    """
    Returns the correct client based on the specified server on the given address and port
    """
    if server == 'xml':
        client = XML_store_inventory_client.xmlrpcStoreInventoryClient(address, port)
    else:
        client = gRPC_store_inventory_client.grpcStoreInventoryClient(address, port)

    print(client)
    x = client.successful_connection()
    print(x)
    if not x:
        print('Please enter a valid connection')
        sys.exit()

    return client



def product_fields(subparser):
    subparser.add_argument('description', help='The description of product')
    subparser.add_argument('manufacturer', help='The manufacturer of product')
    subparser.add_argument('wholesale_cost', type=float, help='The wholesale cost of the product')
    subparser.add_argument('sale_cost', type=float, help='The sale cost of the product')
    subparser.add_argument('amount_in_stock', type=int, help='Amount of product in stock')


def optional_product_fields(subparser):
    subparser.add_argument('--description', help='The description of product')
    subparser.add_argument('--manufacturer', help='The manufacturer of product')
    subparser.add_argument('--wholesale_cost', type=float, help='The wholesale cost of the product')
    subparser.add_argument('--sale_cost', type=float, help='The sale cost of the product')
    subparser.add_argument('--amount_in_stock', type=int, help='Amount of product in stock')


def order_fields(subparser):
    subparser.add_argument('destination', help='The destination of the order')
    subparser.add_argument('date', help='The date the order is to be shipped')
    subparser.add_argument('is_shipped', help='Whether or not the order has been shipped')
    subparser.add_argument('is_paid', help='Whether or not the order has been paid')


def optional_order_fields(subparser):
    subparser.add_argument('--destination', help='The destination of the order')
    subparser.add_argument('--date', help='The date the order is to be shipped')
    subparser.add_argument('--is_shipped', help='Whether or not the order has been shipped')
    subparser.add_argument('--is_paid', help='Whether or not the order has been paid')


def main():
    parser = argparse.ArgumentParser(description='Client to interact with either the gRPC or XML-RPC store inventory server')
    parser.add_argument('address', help='The IP address of the server to connect to')
    parser.add_argument('--port', type=int, help='The port of the server to connect to', default=50052)
    parser.add_argument('grpc_or_xml', choices=['grpc', 'xml'], help='Which server to interact with')

    subparsers = parser.add_subparsers(title='command', dest='cmd', required=True)

    add_product = subparsers.add_parser(name='add-product', help='Add a product to the inventory database')
    add_product.add_argument('name', help='The name of a product')
    product_fields(add_product)

    get_product_by_id = subparsers.add_parser(name='get-product-by-id', help='Get a product specified by id from the inventory database')
    get_product_by_id.add_argument('id_number', help='The id of a product')

    get_product_by_name = subparsers.add_parser(name='get-product-by-name', help='Get a product specified by its name from the inventory database')
    get_product_by_name.add_argument('name', help='the name of a product')

    update_product_by_id = subparsers.add_parser(name='update-product-by-id', help='Update a product specified by its id')
    update_product_by_id.add_argument('id_number', help='The id number of product')
    optional_product_fields(update_product_by_id)

    update_product_by_name = subparsers.add_parser(name='update-product-by-name', help='Update a product specified by its name')
    update_product_by_name.add_argument('name', help='The name of the product')
    optional_product_fields(update_product_by_name)
            
    list_products = subparsers.add_parser(name='list-products', help='List products based on manufacturer and/or products are in stock')
    list_products.add_argument('--manufacturer', help='The product manufacturer to search for')
    list_products.add_argument('--in-stock', help='Whether or not the product is in stock', default='T')




    add_order = subparsers.add_parser(name='add-order', help='Add an order to the inventory database')
    order_fields(add_order)
    add_order.add_argument('products', nargs='+', help='The list of product ids followed by their counts to be added to the order')

    get_order = subparsers.add_parser(name='get-order', help='Get an order from the inventory database')
    get_order.add_argument('id_number', help='The id of the desired order')

    update_order = subparsers.add_parser(name='update-order', help='Update the given order')
    update_order.add_argument('id_number', help='The id of the order to update')
    optional_order_fields(update_order)

    add_products_to_order = subparsers.add_parser(name='add-to-order', help='Add products to an order')
    add_products_to_order.add_argument('id_number', help='The id of the order to update')
    add_products_to_order.add_argument('products', nargs='+', help='A list of products followed by their counts to be added to the order')

    remove_products_from_order = subparsers.add_parser(name='remove-from-order', help='Remove products from an order')
    remove_products_from_order.add_argument('id_number', help='The id of the order to update')
    remove_products_from_order.add_argument('products', nargs='+', help='A list of products followed by their counts to be removed from an order')

    list_orders = subparsers.add_parser(name='list-orders', help='List all orders based on shipped status and paid status')
    list_orders.add_argument('--is_shipped', help='Whether or not the order has been shipped', default='T')
    list_orders.add_argument('--is_paid', help='Whether or not the order has been paid', default='T')

    args = parser.parse_args()

    client = get_client(args.grpc_or_xml, args.address, args.port)
    print('does it exit here??')
    # List methods function?

    if args.cmd == 'add-product':
        client.addProduct(args.name, args.description, args.manufacturer, args.wholesale_cost, args.sale_cost, args.amount_in_stock)
    elif args.cmd == 'get-product-by-id':
        client.getProductById(args.id_number)
    elif args.cmd == 'get-product-by-name':
        client.getProductByName(args.name)
    elif args.cmd == 'update-product-by-id':
        client.updateProductById(args.id_number, args.description, args.manufacturer, args.wholesale_cost, args.sale_cost, args.amount_in_stock)
    elif args.cmd == 'update-product-by-name':
        client.updateProductByName(args.name, args.description, args.manufacturer, args.wholesale_cost, args.sale_cost, args.amount_in_stock)
    elif args.cmd == 'list-products':
        client.listProducts(args.manufacturer, args.in_stock)
    
    elif args.cmd == 'add-order':
        client.addOrder(args.destination, args.date, args.products, args.is_shipped, args.is_paid)
    elif args.cmd == 'get-order':
        client.getOrder(args.id_number)
    elif args.cmd == 'update-order':
        client.updateOrder(args.id_number, args.destination, args.date, args.is_shipped, args.is_paid)
    elif args.cmd == 'add-to-order':
        client.addProductsToOrder(args.id_number, args.products)
    elif args.cmd == 'remove-from-order':
        client.removeProductsFromOrder(args.id_number, args.products)
    else:
        client.listOrders(args.is_shipped, args.is_paid)


if __name__ == '__main__':
    main()

