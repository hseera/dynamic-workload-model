# Dynamic Workload
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
![Alt text](/image/Image1.png?raw=true "Optional Title")


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
![Alt text](/image/Image2.png?raw=true "Optional Title")

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
![Alt text](/image/Image3.png?raw=true "Optional Title")


## Authors

* **Harinder Seera** - *Initial work* - [OzPerf](https://ozperf.com/)

If you would like to contribute to this project, please reachout to me.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
