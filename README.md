# Remote smart home

Hack infra-red remote controllers at home.

## Setup

```
sudo pip3 install wiringpi
```

## Detail

### recieve-remote-controller-signal.py

Output high and low switch interval.  

```
$ python3 recieve-remote-controller-signal.py
> Start! value: 1, start_time: 1648954030.0795293
> H:L = None:2932753
> H:L = 2947:1474
> H:L = 411:941
> H:L = 410:1075
> H:L = 411:272
> ...
```

### visualize-remote-controller-signal.py

Visualize 0/1 signal.  
Time interval value is embedded in code.  

```
$ python3  visualize-remote-controller-signal.py
> Start! value: 1, start_time: 1648961509.5187747
> start
> 110010001110100000101010
> ...
```

### send-signal.py

Send signal to lignt.  
Options are in json file.  

```
$ sudo python3 send-signal.py on
$ sudo python3 send-signal.py warm
$ sudo python3 send-signal.py dark
```

## ToDo
- Check meaning of signals
- Add circuit diagram to readme
- Implement LINE bot to operate remotely
- Air conditioner

## References
- https://qiita.com/kitahara1152/items/378a36c9e60dca78f80a
- https://osoyoo.com/2017/07/07/ir-remote/
- https://paltee.net/archives/180
- https://www.zumid.net/entry/raspberry-pi-irled/
- http://elm-chan.org/docs/ir_format.html