# API NFR Conversion To JMETER Base Template
Convert NFR document into a base JMeter template.
This simple python script takes an API throughput NFR in an excel file and converts into a Jmeter template which can then be enhanced with payload and other information. It is created to reduce the timeframe required to create new scripts.

Use the baseprofile_template.xlsx to create your NFR requirements. 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to execute the script


* Install python [YAML](https://pypi.org/project/PyYAML/#files) package
* Install python [xlrd](https://pypi.org/project/xlrd/#files) package
* python >=3.5


### Execution

```
1: Use the baseprofile_template.xlsx to create your NFR requirements. Do not change the xlsx file name. Currently it is hardcoded.
2: Once above prequisites are setup, execute the convert.py python script. Make sure the basetemplate file is in the same folder as the convert.py script
```

### Output
Following is a screenshot of what you will get when you run the python script passing the basetemplate excel file.

The NFR excel file will first be converted to a YAML file which will then be converted to JMX. 

![Alt text](/image/Screenshot.png?raw=true "Optional Title")

## Improvements

* Pass NFR template as a parameter to the conversion script
* Have a capability down the track to just use a YAML file as an NFR document instead of excel
* Remove the hardcoded concurrency value and replace it with dynamic value
## Authors

* **Harinder Seera** - *Initial work* - [OzPerf](https://ozperf.com/)

If you would like to contribute to this project, please reachout to me.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
