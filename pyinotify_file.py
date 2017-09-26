#coding:utf-8
from diff_file import betweenDiff
from mail_send import send_mail
from pyinotify import ProcessEvent,WatchManager,Notifier,ALL_EVENTS

monitor_dirs = ['../jiankong']
monitor_files = ['../jiankong/test.txt']
old_file = '../jiankong/test.txt'

class MyEvent(ProcessEvent):
    def process_IN_MODIFY(self,event):
        print('%s is %s.' %(event.pathname,event.maskname))
        if event.pathname in monitor_files:
            html = betweenDiff(old_file,event.pathname)
            send_mail('The file content have been modified.',html)
    def process_IN_ACCESS(self, event):
        print('%s is %s.' %(event.pathname,event.maskname))

def main():
    vm = WatchManager()
    vm.add_watch(monitor_dirs,ALL_EVENTS,rec = True)

    en = MyEvent()
    notifier = Notifier(vm,en)
    notifier.loop()

if __name__ == '__main__':
    main()