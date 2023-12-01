class Find:
    @staticmethod
    def find_object_by_attribute_value_in_list(lst: list, attribute: str, value: str):
        """
        Search for an object in a list based on a specific attribute and value.

        Parameters:
        - arr: The list of objects to search through.
        - attribute: The parameter to compare against in each object.
        - value: The value to match against the specified parameter.

        Returns:
        - object or None: The first matching object found, or None if no match.
        """
        return next((item for item in lst if getattr(item, attribute, None) == value), None)
