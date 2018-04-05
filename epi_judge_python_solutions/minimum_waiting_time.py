def minimum_total_waiting_time(service_times):
    # Sort the service times in increasing order.
    service_times.sort()
    total_waiting_time = 0
    for i, service_time in enumerate(service_times):
        num_remaining_queries = len(service_times) - (i + 1)
        total_waiting_time += service_time * num_remaining_queries
    return total_waiting_time


def minimum_total_waiting_time_pythonic(service_times):
    return sum(
        remaining_queries * time
        for remaining_queries, time in enumerate(sorted(service_times)[::-1]))


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
