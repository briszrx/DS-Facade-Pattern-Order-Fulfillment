class OrderFulfillmentFacade:
    def __init__(self, inventory, payment, shipping, notification):
        self.inventory = inventory
        self.payment = payment
        self.shipping = shipping
        self.notification = notification

    def place_order(self, order):
        return [
            self.inventory.reserve(order),
            self.payment.charge(order),
            self.shipping.create_shipment(order),
            self.notification.send_confirmation(order),
        ]