''' Audacity Timestamp Converter
    Converts Audacity timestamp file times from seconds to HH:MM:SS.ss

    Command parameters
    ----------
    file_name : string
        The exported Audacity timestamp file path.
    output_file_name : string
        The path of the file to write the results to.

    Returns
    -------
    file
        New timesamp file with timestamp in HH:MM:SS.ss format.
'''
import datetime
import argparse

seconds_to_timestamp = lambda seconds: datetime.timedelta(seconds=seconds)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Audacity timestamps from seconds to date (HH:MM:SS.ss")
    parser.add_argument("input", type=str, help="Input file path")
    parser.add_argument("output", type=str, help="Output file path")

    args = parser.parse_args()


    output_text = ""
    with open(args.input) as file:
        for line in file.readlines():
            fields = line.split("\t")
            start_time = f"{seconds_to_timestamp(float(fields[0]))}"[:-4]
            chapter_name = fields[2]
            output_text += f"{start_time} \t {chapter_name}"

    with open(args.output, 'w+') as output:
        output.write(output_text)

    print(f"Result written to {args.output}")
