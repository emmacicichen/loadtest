import threading
import time

from http_client import HTTPClient
from metrics_collector import MetricsCollector
from report_creator import ReportCreator
import click


class LoadTester:
    def __init__(self, url, qps, request_type, threads, data):
        self.url = url
        self.qps = qps
        self.request_type = request_type
        self.threads = threads
        self.data = data
        self.http_client = HTTPClient()
        self.metrics_collector = MetricsCollector()
        self.report_creator = ReportCreator(url, qps, threads, self.metrics_collector)

    def _send_request(self, url, request_type, data, interval):
        """
        :param url: url endpoint to send request to.
        :param request_type: http request type, GET or POST
        :param data: payload data for POST request
        :param interval: interval between each request (1/qps)
        :return: a dictionary containing the performance data
        """
        start_time = time.time()
        latency = 0
        failed_request = 0
        succeed_request = 0
        try:
            if request_type == "GET":
                respond = self.http_client.get(url)
                # record latency
                latency = respond.elapsed.total_seconds()
                self.metrics_collector.record_latency(latency)
                # record error
                if respond.status_code != 200:
                    self.metrics_collector.record_error()
                    failed_request += 1
                else:
                    self.metrics_collector.record_successful_requests()
                    succeed_request += 1
            elif request_type == "POST":

                respond = self.http_client.post(url, data=data)
                latency = respond.elapsed.total_seconds()

                self.metrics_collector.record_latency(latency)

                if respond.status_code != 200 and respond.status_code != 201:
                    self.metrics_collector.record_error()
                    failed_request += 1
                else:
                    self.metrics_collector.record_successful_requests()
                    succeed_request += 1

        except Exception as e:
            self.metrics_collector.record_error()
            failed_request += 1

        res = {
            "latency": latency,
            "failed_request": failed_request,
            "succeed_request": succeed_request
        }

        time.sleep(max(0, interval - (time.time() - start_time)))
        return res

    def run_tests(self, url, qps, request_type, threads, data):
        """
        :param url endpoint to send request to.
        :param qps: Queries-per-second
        :param request_type: http request type, GET or POST
        :param threads: number of threads
        :param data: payload data for POST request
        """
        interval = 1.0 / qps
        start_time = time.time()
        threads_list = []

        for _ in range(threads):
            thread = threading.Thread(target=self._send_request, args=(url, request_type, data, interval))
            thread.start()
            threads_list.append(thread)

        for thread in threads_list:
            thread.join()

        end_time = time.time()
        click.echo(f"Load test completed requests in {end_time - start_time:.2f} seconds.")

    def stop(self):
        time.sleep(10)


if __name__ == '__main__':
    pass
