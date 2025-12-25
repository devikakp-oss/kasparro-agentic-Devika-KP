from agents.input_parsing_agent import InputParsingAgent
from agents.question_generation_agent import QuestionGenerationAgent
from agents.content_logic_agents import ContentLogicAgents
from agents.assembly_agents import AssemblyAgents
from agents.comparison_agent import ComparisonAgent

class OrchestratorAgent:
    """
    Agent responsible for controlling execution order and coordinating
    data flow between all agents. Ensures full pipeline completion.
    """

    def orchestrate(self, raw_input):
        """
        Orchestrates the full pipeline from raw input to final JSON outputs.

        Args:
            raw_input (dict): Raw product data

        Returns:
            dict: Dictionary containing faq, product_page, and comparison_page JSONs
        """
        # Step 1: Input Parsing
        parsing_agent = InputParsingAgent()
        normalized_product = parsing_agent.parse(raw_input)

        # Step 2: Question Generation
        question_agent = QuestionGenerationAgent()
        questions = question_agent.generate_questions(normalized_product)

        # Step 3: Content Logic
        content_agent = ContentLogicAgents()
        content_blocks = content_agent.generate_blocks(normalized_product)

        # Step 4: Assembly for FAQ and Product
        assembly_agent = AssemblyAgents()
        faq_page = assembly_agent.assemble_faq_page(questions, content_blocks, normalized_product)
        product_page = assembly_agent.assemble_product_page(content_blocks, normalized_product)

        # Step 5: Comparison
        comparison_agent = ComparisonAgent()
        product_b = comparison_agent.generate_product_b(normalized_product)

        # Step 6: Assembly for Comparison
        comparison_page = assembly_agent.assemble_comparison_page(normalized_product, product_b)

        return {
            "faq": faq_page,
            "product_page": product_page,
            "comparison_page": comparison_page
        }