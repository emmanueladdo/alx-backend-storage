#!/usr/bin/env python3
"""
Python function that returns all students sorted by average score:
"""


def top_students(mongo_collection):
    """
    Aggregate pipeline to calculate the average score for each student
    """
    pipeline = [
        {
            '$unwind': '$topics'
        },
        {
            '$group': {
                '_id': '$_id',
                'name': {'$first': '$name'},
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]

    # Execute the aggregation pipeline
    result = list(mongo_collection.aggregate(pipeline))

    # Add the averageScore to each item in the result
    for item in result:
        item['averageScore'] = round(item['averageScore'], 2)

    return result
