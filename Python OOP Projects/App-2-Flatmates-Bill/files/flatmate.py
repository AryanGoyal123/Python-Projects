class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days = days_in_house

    def pays(self, receipt, flatmate):
        # Calculate how much one flatmate pays
        weight = self.days / (self.days + flatmate.days)
        return receipt.amount * weight
