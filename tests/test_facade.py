
from order_fulfillment.inventory_service import InventoryService
from order_fulfillment.notification_service import NotificationService
from order_fulfillment.order import Order
from order_fulfillment.order_fulfillment_facade import OrderFulfillmentFacade
from order_fulfillment.payment_service import PaymentService
from order_fulfillment.shipping_service import ShippingService

def test_facade_places_order_successfully():
    inventory = InventoryService()
    payment = PaymentService()
    shipping = ShippingService()
    notification = NotificationService()
    order = Order("item_id", 2)
   
    facade = OrderFulfillmentFacade(inventory, payment, shipping, notification)
    
    facade.place_order(order)
    
    
    assert order.status == "PROCESSED" 