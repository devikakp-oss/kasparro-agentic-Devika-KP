class AssemblyAgents:
    """
    Agents responsible for assembling final JSON pages by filling templates
    with prepared content blocks. Pure structural mapping, no logic or inference.
    """

    def assemble_faq_page(self, questions, blocks, product):
        """
        Assembles FAQ page by pairing questions with answers from content blocks.

        Args:
            questions (list[dict]): Generated questions
            blocks (dict): Content blocks
            product (dict): Internal product model

        Returns:
            dict: FAQ page JSON
        """
        faqs = []
        for q in questions:
            answer = self._generate_answer(q['category'], q['question'], blocks, product)
            faqs.append({
                "category": q['category'],
                "question": q['question'],
                "answer": answer
            })

        return {
            "page_type": "faq",
            "product_name": product['name'],
            "faqs": faqs
        }

    def assemble_product_page(self, blocks, product):
        """
        Assembles Product page by filling template with content blocks.

        Args:
            blocks (dict): Content blocks
            product (dict): Internal product model

        Returns:
            dict: Product page JSON
        """
        return {
            "page_type": "product",
            "name": product['name'],
            "ingredients": blocks['ingredients'],
            "benefits": blocks['benefits'],
            "usage": blocks['usage'],
            "side_effects": blocks['safety'],
            "price": float(blocks['pricing'].strip('$'))
        }

    def assemble_comparison_page(self, product_a, product_b):
        """
        Assembles Comparison page by filling template with Product A and B.

        Args:
            product_a (dict): Internal product model A
            product_b (dict): Generated product model B

        Returns:
            dict: Comparison page JSON
        """
        return {
            "page_type": "comparison",
            "product_a": {
                "name": product_a['name'],
                "concentration": product_a.get('concentration'),
                "skin_types": product_a['skin_types'],
                "ingredients": product_a['ingredients'],
                "benefits": product_a['benefits'],
                "usage_instructions": product_a['usage_instructions'],
                "side_effects": product_a.get('side_effects'),
                "price": product_a['price']
            },
            "product_b": {
                "name": product_b['name'],
                "concentration": product_b.get('concentration'),
                "skin_types": product_b['skin_types'],
                "ingredients": product_b['ingredients'],
                "benefits": product_b['benefits'],
                "usage_instructions": product_b['usage_instructions'],
                "side_effects": product_b.get('side_effects'),
                "price": product_b['price']
            }
        }

    def _generate_answer(self, category, question, blocks, product):
        """
        Generates answer for a question based on category, question text, content blocks, and product data.
        """
        question_lower = question.lower()

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
            return f"The price is {blocks['pricing']}."
        elif "name" in question_lower:
            return f"The product is called {product['name']}."
        else:
            return "Please refer to product details."