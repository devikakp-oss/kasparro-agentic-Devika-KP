class ComparisonAgent:
    """
    Agent responsible for generating a fictional Product B for comparison.
    Mirrors Product A's structure, same category, partial ingredient overlap,
    price difference within controlled range.
    """

    def generate_product_b(self, product_a):
        """
        Generates a fictional Product B based on Product A.

        Args:
            product_a (dict): Internal product model for Product A

        Returns:
            dict: Product B model
        """
        product_b = {}

        # Name: Similar but different
        product_b['name'] = "Hyaluronic Acid Moisturizer"

        # Concentration: Different value
        product_b['concentration'] = "2%"

        # Skin types: Same as A
        product_b['skin_types'] = product_a['skin_types'].copy()

        # Ingredients: Partial overlap - share some, add new
        shared_ingredients = product_a['ingredients'][:2]  # First 2 from A
        new_ingredients = ["glycerin", "aloe vera"]
        product_b['ingredients'] = shared_ingredients + new_ingredients

        # Benefits: Similar but different
        product_b['benefits'] = ["hydrates skin", "reduces fine lines", "improves elasticity"]

        # Usage: Similar
        product_b['usage_instructions'] = "Apply twice daily after cleansing"

        # Side effects: Different
        product_b['side_effects'] = "Possible mild dryness"

        # Price: 10% higher than A
        product_b['price'] = round(product_a['price'] * 1.1, 2)

        return product_b