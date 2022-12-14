
import heapq
import random

from .AbstractRanker import AbstractRanker


class BetaRankerRX(AbstractRanker):
    # Top k Ranker
    def rank_ids(self, limit, probabilities, seed, starting_point):
        k = limit
        top_k = heapq.nlargest(k, probabilities, key=lambda x: x["p_engage"])
        top_k_ids = list(map(lambda x: x["content_id"], top_k))
        print(top_k_ids[0:10])
        return top_k_ids