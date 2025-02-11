from similarity_measures import SimilarityMeasures as sm
import pandas as pd


class ClusterSimilarity:

    def __init__(self, 
                cluster1: dict[str, list[str]],
                cluster2: dict[str, list[str]],
                threshold: int = 0,
                similarity_measures: sm = None
                ):
        
        self.cluster1 = cluster1
        self.cluster2 = cluster2
        self.threshold = threshold
        self.similarity_measures = similarity_measures if similarity_measures else sm().overlap_coefficient

    def calculate_similarity(self) -> pd.DataFrame:
        df = pd.DataFrame(columns=self.cluster2.keys(), index=self.cluster1.keys())
        for key, value in self.cluster1.items():
            for key2, value2 in self.cluster2.items():
                df.at[key, key2] = self.similarity_measures(value, value2)
            n_row = (df > self.threshold).sum(axis=0)
            n_col = (df > self.threshold).sum(axis=1)
        df['n_col'] = n_col
        df.loc['n_row'] = n_row
        return df