class window_card:
    RAM = "8GB"
    SSD = "512GB"
    def details(self):
        print("Ram -->",self.RAM,"SSD -->",self.SSD)


print("Before")
card1 = window_card()
card1.RAM = "16GB"
window_card.details(card1)

card2 = window_card()
window_card.details(card2)

window_card.SSD = "1020GB"

print("Company Change")

card2 = window_card()
window_card.details(card2)

card3 = window_card()
window_card.details(card3)