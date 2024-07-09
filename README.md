## LoadTestLib: A general-purpose HTTP load-testing and benchmarking library

### How to run a Load Test
- build a docker image
  - `docker  build -t loadtest .`
- run a docker image
  - `docker run loadtest <url_generated_from_json_server> --qps <qps_input> --threads <threads_input>`
  - e.g. `docker run loadtest http://192.168.1.75:3000 --qps 10 --threads 25`
- Read load testing report from the output
```angular2html
Starting load testing of GET request on http://192.168.1.75:3000 at 10 QPS for with 25 threads...
Load test completed requests in 0.37 seconds.
Load Testing Report for http://192.168.1.75:3000:
--------------------------------------------
Threads: 25
QPS: 10
Average Latency: 0.04 seconds
Error Rate: 0.00%
Response Times:
  Average: 0.04 seconds
  Min: 0.01 seconds
  Max: 0.09 seconds
--------------------------------------------
```