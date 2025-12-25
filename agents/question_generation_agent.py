class QuestionGenerationAgent:
    """
    Agent responsible for generating customer-style questions
    based on product attributes, categorized appropriately.
    """

    def generate_questions(self, internal_product):
        """
        Generates rule-based questions from the internal product model.

        Args:
            internal_product (dict): Normalized product model

        Returns:
            list[dict]: List of questions with category and question text
        """
        questions = []

        # Name
        questions.append({
            "category": "General",
            "question": f"What is the name of this product?"
        })

        # Concentration (if present)
        if internal_product.get('concentration'):
            questions.append({
                "category": "Ingredients",
                "question": f"What is the concentration of {internal_product['name']}?"
            })

        # Skin Types
        if internal_product.get('skin_types'):
            questions.append({
                "category": "Usage",
                "question": f"What skin types is {internal_product['name']} suitable for?"
            })

        # Ingredients
        if internal_product.get('ingredients'):
            questions.append({
                "category": "Ingredients",
                "question": f"What are the key ingredients in {internal_product['name']}?"
            })

        # Benefits
        if internal_product.get('benefits'):
            questions.append({
                "category": "Benefits",
                "question": f"What are the benefits of using {internal_product['name']}?"
            })

        # Usage Instructions
        if internal_product.get('usage_instructions'):
            questions.append({
                "category": "Usage",
                "question": f"How should I use {internal_product['name']}?"
            })

        # Side Effects (if present)
        if internal_product.get('side_effects'):
            questions.append({
                "category": "Safety",
                "question": f"Are there any side effects associated with {internal_product['name']}?"
            })

        # Price
        if 'price' in internal_product:
            questions.append({
                "category": "Pricing",
                "question": f"How much does {internal_product['name']} cost?"
            })

        return questions