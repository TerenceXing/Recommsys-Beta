import operator

from sqlalchemy.sql.expression import func
from sqlalchemy.sql import text

from src import db
from src.api.content.models import Content
from src.api.engagement.models import Engagement, EngagementType
from src.data_structures.approximate_nearest_neighbor import ann_with_offset

from .AbstractGenerator import AbstractGenerator
from .RandomGenerator import RandomGenerator


class BetaGeneratorRX(AbstractGenerator):
	def get_content_ids(self, _, limit, offset, _seed, starting_point):
		
		# rules-based: select out items with likes >= 1, 7244 images 
		if starting_point is None:
			sql_statement = text(f"""
				SELECT content_id, sum(engagement_value) as like_num 
				FROM engagement 
				WHERE engagement_type = 'Like' 
					and engagement_value = 1 -- like
				GROUP BY content_id
				HAVING sum(engagement_value) >= 2
				LIMIT :l
				OFFSET :o
				""")

			with db.engine.connect() as con:
				ids_to_filter = list(con.execute(sql_statement, l = limit, o = offset)) # [(id1,), (id2,)...]
				ids_to_filter = list(map(lambda x: x[0], ids_to_filter)) # {id1, id2, ...}
			
			print(ids_to_filter[0:2])
			return ids_to_filter, None

		elif starting_point.get("content_id", False):
			content_ids, scores = ann_with_offset(
			    starting_point["content_id"], 0.9, limit, offset, return_distances=True
			)
			return content_ids, scores
		
		raise NotImplementedError("Need to provide a key we know about")