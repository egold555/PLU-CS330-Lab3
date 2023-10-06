# Lab3
This program splits input data into training and test data.

With the arguments below, you can randomize the data, skip lines, and provide a ratio of training data to test data.

## Contributors
- [x] Eric Golde


## How to use the program

### Arguments
| Argument | Type | Description | Defaults
| --- | --- | --- | --- |
| --help | N/A | Help menu | N/A |
| --input | String | Input file | N/A - Required |
| --skiplines | Integer | Amount of lines to skip from the top | 0 |
| --ratio | Float | Ratio of training data to test data. 0-1 | 0.5 |
| --mode | Char | Mode of the program. **R**andom or **N**ormal | R |

### Example
```bash
# This will run the program, evenly splitting the data into training and test data, and skipping the CSV header, and randomly selecting the data
python3 Lab3.py --input "DATA/covid19_open_data.csv" --skiplines 1 --ratio 0.5 --mode R
```