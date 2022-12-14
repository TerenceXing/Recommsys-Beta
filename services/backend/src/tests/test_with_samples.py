# manage.py -> get data from db

import csv
import os
import pickle
import random

from flask.cli import FlaskGroup
from src import create_app, db
from src.api.content.models import (
    Content,
    GeneratedContentMetadata,
    MediaType,
    ModelType,
)
from src.api.users.models import User


# sql queries
# 1: select all images with >=3 total likes (207 images)
select content_id, sum(engagement_value) as like_num from engagement where engagement_type = 'Like' and engagement_value = 1 group by content_id having sum(engagement_value) >= 3;


<img src="https://columbia-e4579-prod-bucket.s3.amazonaws.com/generated_images/txt2img_movies/Hurt-Locker-The/75/11/8.5/13550.png" alt="DOWNRANGE The bot dutifully makes its return voyage to the plastic bag, this time towing a cart which is loaded with C4 and a blasting cap, and a coil of unspooling detonation wire. The robot hits a bump causing the blasting cap to tumble to the ground, where it begins to roll -- UPRANGE Everyone cringes. The cap doesn't explode. Close call.

 In the style of movie: Hurt-Locker-The">

 select id from content where s3_id = 'generated_images/txt2img_movies/Hurt-Locker-The/75/11/8.5/13550.png';

 select * from engagement where content_id = 41868;