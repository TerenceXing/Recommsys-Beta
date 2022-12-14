
# TBD, copy RandomModel For now

import random

from .AbstractModel import AbstractModel


class BetaModelRX(AbstractModel):
    def predict_probabilities(self, content_ids, user_id, seed=None, **kwargs):
        if seed:
            random.seed(seed)
        return list(
            map(
                lambda content_id: {
                    "content_id": content_id,
                    "p_engage": random.random(),
                    "score": kwargs.get("scores", {})
                    .get(content_id, {})
                    .get("score", None),
                },
                content_ids,
            )
        )