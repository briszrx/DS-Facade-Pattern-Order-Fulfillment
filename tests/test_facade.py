
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
        order = Order("item_id", "2", 250.50, "Av. ITESO 8585")
        
        facade = OrderFulfillmentFacade(inventory, payment, shipping, notification)
        
       
        results = facade.place_order(order)
        
        
        assert results == [
            "inventory:reserved:2",
            "payment:charged:250.50",
            "shipping:created:Av. ITESO 8585",
            "notification:sent:item_id"
        ]