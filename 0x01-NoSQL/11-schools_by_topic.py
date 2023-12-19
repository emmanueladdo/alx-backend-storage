#!/usr/bin/env python3
"""
A python function that returns the list of school having
 a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    this function finds schools by topic
    Returns: list of schools having the specified topic
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
