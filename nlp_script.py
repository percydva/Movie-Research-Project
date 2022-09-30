from ipynb.fs.full.nlp_task import *
import sys

from script import handle_df
import pandas as pd

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def main(filename, output, output_file):
    data = pd.read_csv(filename, parse_dates=['FRI_RELEASE_DAYBO', 'TUE_V_RELEASE'])
    df, exception = handle_data(output_file, data, hdr)
    # df, exception = handle_file(output_file, data, hdr)
    df.to_csv(output, index=False)
    print(exception)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])