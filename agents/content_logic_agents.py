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

    def generate_faq_answers(self, questions, product, blocks):
        """
        Generates answers for FAQ questions using product data and content blocks.
        This is content logic, not assembly.

        Args:
            questions (list[dict]): List of question dicts
            product (dict): Normalized product model
            blocks (dict): Content blocks

        Returns:
            list[str]: List of answers in question order
        """
        answers = []
        for q in questions:
            question_lower = q['question'].lower()
            answer = self._generate_single_answer(question_lower, product, blocks)
            answers.append(answer)
        return answers

    def _generate_single_answer(self, question_lower, product, blocks):
        """
        Generates answer for a single question.
        """
        if "concentration" in question_lower:
            conc = product.get('concentration', 'N/A')
            return f"The concentration is {conc}."
        elif "skin types" in question_lower:
            types = product.get('skin_types', [])
            return f"This product is suitable for {', '.join(types)} skin types."
        elif "ingredients" in question_lower:
            return f"The key ingredients are: {', '.join(blocks['ingredients'])}."
        elif "benefits" in question_lower:
            return f"The benefits include: {', '.join(blocks['benefits'])}."
        elif "use" in question_lower or "usage" in question_lower:
            return f"Usage instructions: {blocks['usage']}."
        elif "side effects" in question_lower or "safety" in question_lower:
            if blocks['safety']:
                return f"Side effects: {blocks['safety']}."
            else:
                return "No significant side effects reported."
        elif "cost" in question_lower or "price" in question_lower:
            return f"The price is {blocks['pricing']['display']}."
        elif "name" in question_lower:
            return f"The product is called {product['name']}."
        else:
            return "Please refer to product details."

    def _generate_pricing_block(self, product):
        """Transform price into structured pricing block."""
        price = product.get('price', 0)
        return {
            "display": f"${price:.2f}",
            "value": price
        }