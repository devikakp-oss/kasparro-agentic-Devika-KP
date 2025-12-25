class ContentLogicAgents:
    """
    Agents responsible for generating reusable content blocks
    from product data: Usage, Benefits, Ingredients, Safety, Pricing.
    Each block has a single responsibility and can be reused across pages.
    """

    def generate_blocks(self, internal_product):
        """
        Generates all reusable content blocks.

        Args:
            internal_product (dict): Normalized product model

        Returns:
            dict: Content blocks
        """
        blocks = {}

        blocks['usage'] = self._generate_usage_block(internal_product)
        blocks['benefits'] = self._generate_benefits_block(internal_product)
        blocks['ingredients'] = self._generate_ingredients_block(internal_product)
        blocks['safety'] = self._generate_safety_block(internal_product)
        blocks['pricing'] = self._generate_pricing_block(internal_product)

        return blocks

    def _generate_usage_block(self, product):
        """Transform usage instructions into reusable content."""
        return product.get('usage_instructions', '')

    def _generate_benefits_block(self, product):
        """Transform benefits list into reusable content."""
        return product.get('benefits', [])

    def _generate_ingredients_block(self, product):
        """Transform ingredients list into reusable content."""
        return product.get('ingredients', [])

    def _generate_safety_block(self, product):
        """Transform side effects into reusable content."""
        return product.get('side_effects', '')

    def _generate_pricing_block(self, product):
        """Transform price into reusable content."""
        price = product.get('price', 0)
        return f"${price:.2f}"