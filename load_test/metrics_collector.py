# metrics_collector.py

import statistics


class MetricsCollector:
    def __init__(self):
        self.latencies = []
        self.errors = 0
        self.successful_requests = 0

    def record_latency(self, latency):
        self.latencies.append(latency)

    def record_error(self):
        self.errors += 1

    def record_successful_requests(self):
        self.successful_requests += 1

    def calculate_average_latency(self):
        if not self.latencies:
            return 0.0
        return statistics.mean(self.latencies)

    def calculate_error_rate(self):
        total_requests = self.successful_requests + self.errors
        if total_requests == 0:
            return 0.0
        return (self.errors / total_requests) * 100.0

    def calculate_response_times(self):
        return {
            'average': self.calculate_average_latency(),
            'min': min(self.latencies) if self.latencies else 0.0,
            'max': max(self.latencies) if self.latencies else 0.0
        }
