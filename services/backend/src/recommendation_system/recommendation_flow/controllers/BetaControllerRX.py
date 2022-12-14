from src.recommendation_system.recommendation_flow.candidate_generators.BetaGeneratorRX import (
    BetaGeneratorRX,
)
from src.recommendation_system.recommendation_flow.controllers.AbstractController import (
    AbstractController,
)
from src.recommendation_system.recommendation_flow.filtering.BetaFilterRX import (
    BetaFilterRX,
)
from src.recommendation_system.recommendation_flow.model_prediction.BetaModelRX import (
    BetaModelRX,
)
from src.recommendation_system.recommendation_flow.ranking.BetaRankerRX import (
    BetaRankerRX,
)


class BetaControllerRX(AbstractController):
    def get_content_ids(self, user_id, limit, offset, seed, starting_point):
        candidates_limit = (
            limit * 10 * 10
        )  # 10% gets filtered out and take top 10% of rank
        candidates, scores = BetaGeneratorRX().get_content_ids(
            user_id, candidates_limit, offset, seed, starting_point
        )
        filtered_candidates = BetaFilterRX().filter_ids(
            candidates, seed, starting_point
        )
        predictions = BetaModelRX().predict_probabilities(
            filtered_candidates,
            user_id,
            seed = seed,
            scores = {
                content_id: {"score": score}
                for content_id, score in zip(candidates, scores)
            }
            if scores is not None
            else {},
        )
        rank = BetaRankerRX().rank_ids(limit, predictions, seed, starting_point)

        print('controller final 1-10th ids:', rank[0:10])
        
        return rank
