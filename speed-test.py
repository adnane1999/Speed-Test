import speedtest

Speed = speedtest.Speedtest()

Choice = int(input('''What speed do you want to test :\n
1) Download speed.
2) Upload speed.
3) Ping test.
                      
Your choice : '''))

if Choice == 1 :
    print(Speed.download())
elif Choice == 2 :
    print(Speed.upload())
elif Choice == 3 :
    ServerNames = []
    Speed.get_servers(ServerNames)
    print(Speed.results.ping)
else :
    print("Enter a correct choice !!")
