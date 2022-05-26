
import json
import boto3
import sys
import os
#Lambda layer added
import yfinance as yf

StreamName = os.environ['StreamName']
REGION = os.environ['REGION']


kinesis = boto3.client('kinesis', region_name = REGION)
stocks = ["FB", "SHOP", "BYND", "SNAP", "NFLX", "PINS", "SQ", "TTD", "OKTA", "DDOG"]

    
def lambda_handler(event, context):

    for stock in stocks:
        ticker = yf.Ticker(stock)
        ticker_hist = ticker.history(period = "1d", interval="5m", start="2022-05-02")
        
        for row in range(len(ticker_hist)):
            if str(ticker_hist.index[row])[0:10] == "2022-05-02":
                data = {"company":stock, 
                        "high": ticker_hist["High"][row], 
                        "low":ticker_hist["Low"][row], 
                        "ts":ticker_hist.index[row].strftime('%Y/%m/%d %H:%M:%S')}
                print(data)
                
                data = json.dumps(data)+"\n"
                #print(data)
                output = kinesis.put_record(
                    StreamName= StreamName,
                    Data=data,
                    PartitionKey="partitionkey")
                #print(output)

    return {
        'statusCode': 200,
        'body': json.dumps('Done!')
    }
