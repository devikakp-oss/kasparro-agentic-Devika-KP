import json

class InputParsingAgent:
    """
    Agent responsible for validating and normalizing raw product input
    into the internal product model.
    """

    REQUIRED_FIELDS = ['name', 'skin_types', 'ingredients', 'benefits', 'usage_instructions', 'price']
    OPTIONAL_FIELDS = ['concentration', 'side_effects']

    def parse(self, raw_input):
        """
        Validates and normalizes raw product input.

        Args:
            raw_input (dict): Raw product data

        Returns:
            dict: Normalized internal product model

        Raises:
            ValueError: If validation fails
        """
        # Check required fields
        for field in self.REQUIRED_FIELDS:
            if field not in raw_input or raw_input[field] is None:
                raise ValueError(f"Required field '{field}' is missing")

        # Normalize fields
        normalized = {}

        # String fields
        normalized['name'] = str(raw_input['name']).strip()
        normalized['usage_instructions'] = str(raw_input['usage_instructions']).strip()

        # Optional string fields
        for field in self.OPTIONAL_FIELDS:
            if field in raw_input and raw_input[field] is not None:
                normalized[field] = str(raw_input[field]).strip()
            else:
                normalized[field] = None

        # List fields (normalize from comma-separated strings)
        list_fields = ['skin_types', 'ingredients', 'benefits']
        for field in list_fields:
            if field in raw_input:
                value = str(raw_input[field])
                # Split by comma, strip whitespace, filter empty
                normalized[field] = [item.strip() for item in value.split(',') if item.strip()]
            else:
                raise ValueError(f"Required field '{field}' is missing")

        # Price as number
        try:
            normalized['price'] = float(raw_input['price'])
        except (ValueError, TypeError):
            raise ValueError("Price must be a valid number")

        return normalized