from load_tester import LoadTester
import click


@click.command()
@click.argument('url')
@click.option('--qps', default=10, help='Queries per second (default: 10)')
@click.option('--request_type', default='GET', help='HTTP requests type, "GET" or "POST". Default is GET.')
@click.option('--threads', default=1, help='Number of concurrent requests (default: 1)')
@click.option('--data', default=None, help='Data sent with POST request (default: None)')
def start_load_test(url, qps, request_type, threads, data):
    click.echo(
        f"Starting load testing of {request_type} request on {url} at {qps} QPS for with {threads} threads...")
    load_tester = LoadTester(url, qps, request_type, threads, data)
    load_tester.run_tests(url, qps, request_type, threads, data)
    load_tester.report_creator.create_report()
    load_tester.stop()
    start_benchmarking(url)


def start_benchmarking(url):
    click.echo(f"Starting benchmark for {url}.")


if __name__ == '__main__':
    start_load_test()
