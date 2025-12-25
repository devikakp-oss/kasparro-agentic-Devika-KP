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
        # Map alternative keys
        mapped_input = {}
        for key, value in raw_input.items():
            if key == 'product_name':
                mapped_input['name'] = value
            elif key == 'skin_type':
                mapped_input['skin_types'] = value
            elif key == 'key_ingredients':
                mapped_input['ingredients'] = value
            elif key == 'how_to_use':
                mapped_input['usage_instructions'] = value
            else:
                mapped_input[key] = value

        # Now validate with mapped keys
        # Check required fields
        for field in self.REQUIRED_FIELDS:
            if field not in mapped_input or mapped_input[field] is None:
                raise ValueError(f"Required field '{field}' is missing")

        # Normalize fields
        normalized = {}

        # String fields
        normalized['name'] = str(mapped_input['name']).strip()
        normalized['usage_instructions'] = str(mapped_input['usage_instructions']).strip()

        # Optional string fields
        for field in self.OPTIONAL_FIELDS:
            if field in mapped_input and mapped_input[field] is not None:
                normalized[field] = str(mapped_input[field]).strip()
            else:
                normalized[field] = None

        # List fields (normalize from comma-separated strings)
        list_fields = ['skin_types', 'ingredients', 'benefits']
        for field in list_fields:
            if field in mapped_input:
                value = str(mapped_input[field])
                # Split by comma, strip whitespace, filter empty
                normalized[field] = [item.strip() for item in value.split(',') if item.strip()]
            else:
                raise ValueError(f"Required field '{field}' is missing")

        # Price as number
        try:
            normalized['price'] = float(mapped_input['price'])
        except (ValueError, TypeError):
            raise ValueError("Price must be a valid number")

        return normalized