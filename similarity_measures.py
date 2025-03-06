class SimilarityMeasures:

    def jaccard_similarity(self, list1: list, list2: list) -> float:
        """Calculates the Jaccard similarity between two lists.
        Jaccard similarity is defined as the size of the intersection divided by the size of the union of the sample sets.
        A value of 1 means the lists are identical in terms of unique items,
        while a value of 0 indicates no common items."""
        set1, set2 = set(list1), set(list2)
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        return intersection / union if union != 0 else 0

    def dice_coefficient(self, list1: list, list2: list) -> float:
        """"Calculates the Dice coefficient between two lists.
        The Dice coefficient is defined as twice the size of the intersection divided by the sum of the sizes of the two sets.
        A value of 1 indicates complete similarity (all items match) and 0 indicates no similarity."""
        set1, set2 = set(list1), set(list2)
        intersection = len(set1 & set2)
        return (2 * intersection) / (len(set1) + len(set2)) if (len(set1) + len(set2)) != 0 else 0

    def overlap_coefficient(self, list1: list, list2: list) -> float:
        """"Calculates the Overlap Coefficient between two lists.
        The Overlap Coefficient is the size of the intersection divided by the smaller set's size.
        A value of 1 means one list is entirely contained in the other,
        while a value of 0 indicates no common elements."""
        set1, set2 = set(list1), set(list2)
        intersection = len(set1 & set2)
        return intersection / min(len(set1), len(set2)) if min(len(set1), len(set2)) != 0 else 0