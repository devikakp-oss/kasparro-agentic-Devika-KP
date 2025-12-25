class AssemblyAgents:
    """
    Agents responsible for assembling final JSON pages by filling templates
    with prepared content blocks. Pure structural mapping, no logic or inference.
    """

    def assemble_faq_page(self, questions, answers, product_name):
        """
        Assembles FAQ page by pairing questions with precomputed answers.

        Args:
            questions (list[dict]): Generated questions
            answers (list[str]): Precomputed answers
            product_name (str): Product name

        Returns:
            dict: FAQ page JSON
        """
        faqs = []
        for q, a in zip(questions, answers):
            faqs.append({
                "category": q['category'],
                "question": q['question'],
                "answer": a
            })

        return {
            "page_type": "faq",
            "product_name": product_name,
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
            "price": blocks['pricing']['value']
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