import json

payload = '{"system":{"time":"15088599000","soc":43,"charge":false,"rssi":-62,"unit":"C"}, "channel":[{"number":1,"name":"Kanal 1","typ":8,"temp":19.90,"min":10.00,"max":25.00,"alarm":false,"color":"#0C4C88"},{"number":2,"name":"Kanal 2","typ":0,"temp":999.00,"min":10.00,"max":35.00,"alarm":false,"color":"#22B14C"}], "pitmaster":[{"id":0,"channel":1,"pid":0,"value":0,"set":20.80,"typ":"off"}]}'


def main():
    data = json.loads(payload)
    print(data['channel'])

    for c in data['channel']:
        print(c)

main()