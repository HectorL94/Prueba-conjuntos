class SimilarityMeasures:

    def jaccard_similarity(self, list1: list, list2: list) -> float:
        set1, set2 = set(list1), set(list2)
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        return intersection / union if union != 0 else 0


    def dice_coefficient(self, list1: list, list2: list) -> float:
        set1, set2 = set(list1), set(list2)
        intersection = len(set1 & set2)
        return (2 * intersection) / (len(set1) + len(set2)) if (len(set1) + len(set2)) != 0 else 0


    def overlap_coefficient(self, list1: list, list2: list) -> float:
        set1, set2 = set(list1), set(list2)
        intersection = len(set1 & set2)
        return intersection / min(len(set1), len(set2)) if min(len(set1), len(set2)) != 0 else 0