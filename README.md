# Dynamic Workload Model
![Language Python](https://img.shields.io/badge/%20Language-python-blue.svg) [![MIT License](http://img.shields.io/badge/License-MIT-blue.png)](LICENSE)

[![GitHub Last Commits](https://img.shields.io/github/last-commit/hseera/dynamic-workload-model.svg)](https://github.com/hseera/dynamic-workload-model/commits/) [![GitHub Size](https://img.shields.io/github/repo-size/hseera/dynamic-workload-model.svg)](https://github.com/hseera/dynamic-workload-model/)
[![Open GitHub Issue](https://img.shields.io/badge/Open-Incident-brightgreen.svg)](https://github.com/hseera/dynamic-workload-model/issues/new/choose)
[![GitHub Open Issues](https://img.shields.io/github/issues/hseera/dynamic-workload-model?color=purple)](https://github.com/hseera/dynamic-workload-model/issues?q=is%3Aopen+is%3Aissue)
[![GitHub Closed Issues](https://img.shields.io/github/issues-closed/hseera/dynamic-workload-model?color=purple)](https://github.com/hseera/dynamic-workload-model/issues?q=is%3Aclosed+is%3Aissue)

There are times when you want to generate dynamic workload model to test different scenarios. For example testing autoscaling in cloud. 

In your load test tool call the python code to get the load to generate value per second. Based on the value received then make appropriate # of requests per second.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to execute the script

* python >=3.5


### Execution

Before running your test, you will need to invoke this function to generate the load profile profile which you can then feed in your test run.

Play around with the function values to get the correct workload model you want to emulate for your testing.

### Output
Following are same of the workload model examples that you can generate based on cosine parameter values.

**Scenario 1:**

With following Cosine function values, you will get the following workload graph
```
duration = 3600
y1Amplitude = 25
y2Amplitude = 25
y1NoofCycles = 12
y2NoofCycles = 4
y1HorizontalShift = 0
y2HorizontalShift = 0
y1VerticalShift = 25
y2VerticalShift = 25
```
![Alt text](/images/Image1.png?raw=true "Optional Title")


**Scenario 2:**

With following Cosine function values, you will get the following workload graph
```
duration = 3600
y1Amplitude = 25
y2Amplitude = 25
y1NoofCycles = 4
y2NoofCycles = 8
y1HorizontalShift = 0
y2HorizontalShift = 0
y1VerticalShift = 25
y2VerticalShift = 25
```
![Alt text](/images/Image2.png?raw=true "Optional Title")

**Scenario 3:**

With following Cosine function values, you will get the following workload graph
```
duration = 3600
y1Amplitude = 25
y2Amplitude = 25
y1NoofCycles = 4
y2NoofCycles = 10
y1HorizontalShift = 0
y2HorizontalShift = 0
y1VerticalShift = 25
y2VerticalShift = 25
```
![Alt text](/images/Image3.png?raw=true "Optional Title")

**Scenario 4:**

With following Cosine function values, you will get the following workload graph
```
duration = 3600
y1Amplitude = 25
y2Amplitude = 25
y1NoofCycles = 4
y2NoofCycles = 5
y1HorizontalShift = 0
y2HorizontalShift = 0
y1VerticalShift = 25
y2VerticalShift = 25
```
![Alt text](/images/Image4.png?raw=true "Optional Title")

## Contribute

If you would like to contribute to this project, please reachout to me. Issues and pull requests are welcomed too.

## Author
[<img id="github" src="./images/github.png" width="50" a="https://github.com/hseera/">](https://github.com/hseera/)    [<img src="./images/linkedin.png" style="max-width:100%;" >](https://www.linkedin.com/in/hpseera) [<img id="twitter" src="./images/twitter.png" width="50" a="twitter.com/HarinderSeera/">](https://twitter.com/@HarinderSeera) <a href="https://twitter.com/intent/follow?screen_name=harinderseera"> <img src="https://img.shields.io/twitter/follow/harinderseera.svg?label=Follow%20@harinderseera" alt="Follow @harinderseera" /> </a>          [![GitHub followers](https://img.shields.io/github/followers/hseera.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/hseera?tab=followers)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
