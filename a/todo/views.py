from django.shortcuts import render
def index(requests):
    r = requests.POST
    print(r)
    with open('saved.txt', 'a', encoding='1258') as f:
        f.write(str(requests))
        f.write('\n')
    return render(requests, 'robot/index.html')