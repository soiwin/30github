

class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = []

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_product = []
            return

        idx = len(self.prefix_product)

        if idx == 0:
            self.prefix_product.append(num)
            return

        self.prefix_product.append(self.prefix_product[idx - 1] * num)

    def get_product(self, k: int) -> int:
        if len(self.prefix_product) < k:
            return 0

        if len(self.prefix_product) == k:
            return self.prefix_product[-1]

        return self.prefix_product[-1] // self.prefix_product[-k - 1]


productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)
productOfNumbers.add(0)
productOfNumbers.add(2)
productOfNumbers.add(5)
productOfNumbers.add(4)
print(productOfNumbers.get_product(0))

