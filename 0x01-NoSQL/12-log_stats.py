#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def print_logs_stats(db):
    # Get the total number of documents in the collection
    total_logs = db.nginx.count_documents({})

    print(f"{total_logs} logs")

    # Count the number of documents with each HTTP method
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in http_methods:
        count = db.nginx.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Count the number of documents with method=GET and path=/status
    status_check_count = db.nginx.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    # Check if the correct number of command-line arguments are provided
    import sys
    if len(sys.argv) != 2:
        print('Usage: ./12-log_stats.py <databaseName>')
        sys.exit(1)

    # Get the database name from the command-line argument
    db_name = sys.argv[1]

    # Connect to the MongoDB server
    client = MongoClient()
    db = client[db_name]

    # Print the logs statistics
    print_logs_stats(db)

    # Close the MongoDB connection
    client.close()
