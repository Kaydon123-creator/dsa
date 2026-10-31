class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:

        result = []
        products.sort()
        word = ""
        for c in searchWord:
            word+= c
            ans = []
            for product in products:
                if product.startswith(word):
                    ans.append(product)
                if len(ans)>= 3:
                    break
            result.append(ans)
        return result
                
        