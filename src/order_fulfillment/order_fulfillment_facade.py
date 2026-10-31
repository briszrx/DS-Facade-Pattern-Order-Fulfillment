class OrderFulfillmentFacade:
    def __init__(self, inventory, payment, shipping, notification):
        self.inventory = inventory
        self.payment = payment
        self.shipping = shipping
        self.notification = notification

    def place_order(self, order):
        self.inventory.check_and_reserve(order) 
        self.payment.process(order)
        self.shipping.schedule(order)
        self.notification.send(order)