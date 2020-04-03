# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: store_inventory.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='store_inventory.proto',
  package='ecommerce',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x15store_inventory.proto\x12\tecommerce\"\xa7\x01\n\x07Product\x12\x11\n\tid_number\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x04 \x01(\t\x12\x16\n\x0ewholesale_cost\x18\x05 \x01(\x01\x12\x11\n\tsale_cost\x18\x06 \x01(\x01\x12\r\n\x05stock\x18\x07 \x01(\x05\x12\x16\n\x0enum_of_product\x18\x08 \x01(\x05\"Q\n\x10ProductAndDemand\x12%\n\x07product\x18\x01 \x01(\x0b\x32\x14.ecommerce.ProductID\x12\x16\n\x0enum_of_product\x18\x02 \x01(\x05\"\x91\x01\n\x05Order\x12\x11\n\tid_number\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12-\n\x08products\x18\x04 \x03(\x0b\x32\x1b.ecommerce.ProductAndDemand\x12\x0f\n\x07is_paid\x18\x05 \x01(\x08\x12\x12\n\nis_shipped\x18\x06 \x01(\x08\"Z\n\tProductID\x12\x11\n\tid_number\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x03 \x01(\t\x12\x16\n\x0enum_of_product\x18\x04 \x01(\x05\"\x1c\n\x07OrderID\x12\x11\n\tid_number\x18\x01 \x01(\t\"\x99\x01\n\x11UpdateProductInfo\x12\x11\n\tid_number\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x04 \x01(\t\x12\x16\n\x0ewholesale_cost\x18\x05 \x01(\x01\x12\x11\n\tsale_cost\x18\x06 \x01(\x01\x12\r\n\x05stock\x18\x07 \x01(\x05\"l\n\x0fUpdateOrderInfo\x12\x11\n\tid_number\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x0f\n\x07is_paid\x18\x05 \x01(\x05\x12\x12\n\nis_shipped\x18\x06 \x01(\x05\"N\n\nAddToOrder\x12\x11\n\tid_number\x18\x01 \x01(\t\x12-\n\x08products\x18\x02 \x03(\x0b\x32\x1b.ecommerce.ProductAndDemand\"S\n\x0fRemoveFromOrder\x12\x11\n\tid_number\x18\x01 \x01(\t\x12-\n\x08products\x18\x02 \x03(\x0b\x32\x1b.ecommerce.ProductAndDemand\"2\n\x0bOrderStatus\x12\x12\n\nis_shipped\x18\x01 \x01(\x05\x12\x0f\n\x07is_paid\x18\x02 \x01(\x05\":\n\x10ListProductsInfo\x12\x14\n\x0cmanufacturer\x18\x01 \x01(\t\x12\x10\n\x08in_stock\x18\x02 \x01(\x08\"\x07\n\x05\x45mpty2\xeb\x04\n\x10ProductInventory\x12\x36\n\naddProduct\x12\x12.ecommerce.Product\x1a\x14.ecommerce.ProductID\x12\x30\n\x08\x61\x64\x64Order\x12\x10.ecommerce.Order\x1a\x12.ecommerce.OrderID\x12\x36\n\ngetProduct\x12\x14.ecommerce.ProductID\x1a\x12.ecommerce.Product\x12\x30\n\x08getOrder\x12\x12.ecommerce.OrderID\x1a\x10.ecommerce.Order\x12\x41\n\rupdateProduct\x12\x1c.ecommerce.UpdateProductInfo\x1a\x12.ecommerce.Product\x12;\n\x0bupdateOrder\x12\x1a.ecommerce.UpdateOrderInfo\x1a\x10.ecommerce.Order\x12=\n\x12\x61\x64\x64ProductsToOrder\x12\x15.ecommerce.AddToOrder\x1a\x10.ecommerce.Order\x12G\n\x17removeProductsFromOrder\x12\x1a.ecommerce.RemoveFromOrder\x1a\x10.ecommerce.Order\x12\x41\n\x0clistProducts\x12\x1b.ecommerce.ListProductsInfo\x1a\x12.ecommerce.Product0\x01\x12\x38\n\nlistOrders\x12\x16.ecommerce.OrderStatus\x1a\x10.ecommerce.Order0\x01\x62\x06proto3'
)




_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='ecommerce.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_number', full_name='ecommerce.Product.id_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ecommerce.Product.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ecommerce.Product.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='ecommerce.Product.manufacturer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wholesale_cost', full_name='ecommerce.Product.wholesale_cost', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sale_cost', full_name='ecommerce.Product.sale_cost', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stock', full_name='ecommerce.Product.stock', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_of_product', full_name='ecommerce.Product.num_of_product', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=204,
)


_PRODUCTANDDEMAND = _descriptor.Descriptor(
  name='ProductAndDemand',
  full_name='ecommerce.ProductAndDemand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product', full_name='ecommerce.ProductAndDemand.product', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_of_product', full_name='ecommerce.ProductAndDemand.num_of_product', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=287,
)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='ecommerce.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_number', full_name='ecommerce.Order.id_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination', full_name='ecommerce.Order.destination', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='ecommerce.Order.date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='products', full_name='ecommerce.Order.products', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_paid', full_name='ecommerce.Order.is_paid', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_shipped', full_name='ecommerce.Order.is_shipped', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=435,
)


_PRODUCTID = _descriptor.Descriptor(
  name='ProductID',
  full_name='ecommerce.ProductID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_number', full_name='ecommerce.ProductID.id_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ecommerce.ProductID.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='ecommerce.ProductID.manufacturer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_of_product', full_name='ecommerce.ProductID.num_of_product', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=437,
  serialized_end=527,
)


_ORDERID = _descriptor.Descriptor(
  name='OrderID',
  full_name='ecommerce.OrderID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_number', full_name='ecommerce.OrderID.id_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=557,
)


_UPDATEPRODUCTINFO = _descriptor.Descriptor(
  name='UpdateProductInfo',
  full_name='ecommerce.UpdateProductInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_number', full_name='ecommerce.UpdateProductInfo.id_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ecommerce.UpdateProductInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ecommerce.UpdateProductInfo.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='ecommerce.UpdateProductInfo.manufacturer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wholesale_cost', full_name='ecommerce.UpdateProductInfo.wholesale_cost', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sale_cost', full_name='ecommerce.UpdateProductInfo.sale_cost', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stock', full_name='ecommerce.UpdateProductInfo.stock', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=560,
  serialized_end=713,
)


_UPDATEORDERINFO = _descriptor.Descriptor(
  name='UpdateOrderInfo',
  full_name='ecommerce.UpdateOrderInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_number', full_name='ecommerce.UpdateOrderInfo.id_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination', full_name='ecommerce.UpdateOrderInfo.destination', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='ecommerce.UpdateOrderInfo.date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_paid', full_name='ecommerce.UpdateOrderInfo.is_paid', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_shipped', full_name='ecommerce.UpdateOrderInfo.is_shipped', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=715,
  serialized_end=823,
)


_ADDTOORDER = _descriptor.Descriptor(
  name='AddToOrder',
  full_name='ecommerce.AddToOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_number', full_name='ecommerce.AddToOrder.id_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='products', full_name='ecommerce.AddToOrder.products', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=825,
  serialized_end=903,
)


_REMOVEFROMORDER = _descriptor.Descriptor(
  name='RemoveFromOrder',
  full_name='ecommerce.RemoveFromOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_number', full_name='ecommerce.RemoveFromOrder.id_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='products', full_name='ecommerce.RemoveFromOrder.products', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=905,
  serialized_end=988,
)


_ORDERSTATUS = _descriptor.Descriptor(
  name='OrderStatus',
  full_name='ecommerce.OrderStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_shipped', full_name='ecommerce.OrderStatus.is_shipped', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_paid', full_name='ecommerce.OrderStatus.is_paid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=990,
  serialized_end=1040,
)


_LISTPRODUCTSINFO = _descriptor.Descriptor(
  name='ListProductsInfo',
  full_name='ecommerce.ListProductsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='ecommerce.ListProductsInfo.manufacturer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in_stock', full_name='ecommerce.ListProductsInfo.in_stock', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1042,
  serialized_end=1100,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='ecommerce.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1102,
  serialized_end=1109,
)

_PRODUCTANDDEMAND.fields_by_name['product'].message_type = _PRODUCTID
_ORDER.fields_by_name['products'].message_type = _PRODUCTANDDEMAND
_ADDTOORDER.fields_by_name['products'].message_type = _PRODUCTANDDEMAND
_REMOVEFROMORDER.fields_by_name['products'].message_type = _PRODUCTANDDEMAND
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['ProductAndDemand'] = _PRODUCTANDDEMAND
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['ProductID'] = _PRODUCTID
DESCRIPTOR.message_types_by_name['OrderID'] = _ORDERID
DESCRIPTOR.message_types_by_name['UpdateProductInfo'] = _UPDATEPRODUCTINFO
DESCRIPTOR.message_types_by_name['UpdateOrderInfo'] = _UPDATEORDERINFO
DESCRIPTOR.message_types_by_name['AddToOrder'] = _ADDTOORDER
DESCRIPTOR.message_types_by_name['RemoveFromOrder'] = _REMOVEFROMORDER
DESCRIPTOR.message_types_by_name['OrderStatus'] = _ORDERSTATUS
DESCRIPTOR.message_types_by_name['ListProductsInfo'] = _LISTPRODUCTSINFO
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'store_inventory_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.Product)
  })
_sym_db.RegisterMessage(Product)

ProductAndDemand = _reflection.GeneratedProtocolMessageType('ProductAndDemand', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTANDDEMAND,
  '__module__' : 'store_inventory_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.ProductAndDemand)
  })
_sym_db.RegisterMessage(ProductAndDemand)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'store_inventory_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.Order)
  })
_sym_db.RegisterMessage(Order)

ProductID = _reflection.GeneratedProtocolMessageType('ProductID', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTID,
  '__module__' : 'store_inventory_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.ProductID)
  })
_sym_db.RegisterMessage(ProductID)

OrderID = _reflection.GeneratedProtocolMessageType('OrderID', (_message.Message,), {
  'DESCRIPTOR' : _ORDERID,
  '__module__' : 'store_inventory_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.OrderID)
  })
_sym_db.RegisterMessage(OrderID)

UpdateProductInfo = _reflection.GeneratedProtocolMessageType('UpdateProductInfo', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPRODUCTINFO,
  '__module__' : 'store_inventory_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.UpdateProductInfo)
  })
_sym_db.RegisterMessage(UpdateProductInfo)

UpdateOrderInfo = _reflection.GeneratedProtocolMessageType('UpdateOrderInfo', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEORDERINFO,
  '__module__' : 'store_inventory_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.UpdateOrderInfo)
  })
_sym_db.RegisterMessage(UpdateOrderInfo)

AddToOrder = _reflection.GeneratedProtocolMessageType('AddToOrder', (_message.Message,), {
  'DESCRIPTOR' : _ADDTOORDER,
  '__module__' : 'store_inventory_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.AddToOrder)
  })
_sym_db.RegisterMessage(AddToOrder)

RemoveFromOrder = _reflection.GeneratedProtocolMessageType('RemoveFromOrder', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEFROMORDER,
  '__module__' : 'store_inventory_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.RemoveFromOrder)
  })
_sym_db.RegisterMessage(RemoveFromOrder)

OrderStatus = _reflection.GeneratedProtocolMessageType('OrderStatus', (_message.Message,), {
  'DESCRIPTOR' : _ORDERSTATUS,
  '__module__' : 'store_inventory_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.OrderStatus)
  })
_sym_db.RegisterMessage(OrderStatus)

ListProductsInfo = _reflection.GeneratedProtocolMessageType('ListProductsInfo', (_message.Message,), {
  'DESCRIPTOR' : _LISTPRODUCTSINFO,
  '__module__' : 'store_inventory_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.ListProductsInfo)
  })
_sym_db.RegisterMessage(ListProductsInfo)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'store_inventory_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.Empty)
  })
_sym_db.RegisterMessage(Empty)



_PRODUCTINVENTORY = _descriptor.ServiceDescriptor(
  name='ProductInventory',
  full_name='ecommerce.ProductInventory',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1112,
  serialized_end=1731,
  methods=[
  _descriptor.MethodDescriptor(
    name='addProduct',
    full_name='ecommerce.ProductInventory.addProduct',
    index=0,
    containing_service=None,
    input_type=_PRODUCT,
    output_type=_PRODUCTID,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='addOrder',
    full_name='ecommerce.ProductInventory.addOrder',
    index=1,
    containing_service=None,
    input_type=_ORDER,
    output_type=_ORDERID,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getProduct',
    full_name='ecommerce.ProductInventory.getProduct',
    index=2,
    containing_service=None,
    input_type=_PRODUCTID,
    output_type=_PRODUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getOrder',
    full_name='ecommerce.ProductInventory.getOrder',
    index=3,
    containing_service=None,
    input_type=_ORDERID,
    output_type=_ORDER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='updateProduct',
    full_name='ecommerce.ProductInventory.updateProduct',
    index=4,
    containing_service=None,
    input_type=_UPDATEPRODUCTINFO,
    output_type=_PRODUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='updateOrder',
    full_name='ecommerce.ProductInventory.updateOrder',
    index=5,
    containing_service=None,
    input_type=_UPDATEORDERINFO,
    output_type=_ORDER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='addProductsToOrder',
    full_name='ecommerce.ProductInventory.addProductsToOrder',
    index=6,
    containing_service=None,
    input_type=_ADDTOORDER,
    output_type=_ORDER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='removeProductsFromOrder',
    full_name='ecommerce.ProductInventory.removeProductsFromOrder',
    index=7,
    containing_service=None,
    input_type=_REMOVEFROMORDER,
    output_type=_ORDER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='listProducts',
    full_name='ecommerce.ProductInventory.listProducts',
    index=8,
    containing_service=None,
    input_type=_LISTPRODUCTSINFO,
    output_type=_PRODUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='listOrders',
    full_name='ecommerce.ProductInventory.listOrders',
    index=9,
    containing_service=None,
    input_type=_ORDERSTATUS,
    output_type=_ORDER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRODUCTINVENTORY)

DESCRIPTOR.services_by_name['ProductInventory'] = _PRODUCTINVENTORY

# @@protoc_insertion_point(module_scope)
