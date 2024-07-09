import pandas as pd
import os

class ReportCreator:
    def __init__(self, url, qps, threads, metrics_collector):
        self.url = url
        self.metrics_collector = metrics_collector
        self.qps = qps
        self.threads = threads

    def create_report(self):
        avg_latency = self.metrics_collector.calculate_average_latency()
        error_rate = self.metrics_collector.calculate_error_rate()
        response_times = self.metrics_collector.calculate_response_times()

        print(f"Load Testing Report for {self.url}:")
        print("--------------------------------------------")
        print(f"Threads: {self.threads}")
        print(f"QPS: {self.qps}")
        print(f"Average Latency: {avg_latency:.2f} seconds")
        print(f"Error Rate: {error_rate:.2f}%")
        print("Response Times:")
        print(f"  Average: {response_times['average']:.2f} seconds")
        print(f"  Min: {response_times['min']:.2f} seconds")
        print(f"  Max: {response_times['max']:.2f} seconds")
        print("--------------------------------------------")


