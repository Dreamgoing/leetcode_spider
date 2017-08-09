# coding=utf-8
from twisted.internet import defer, reactor
from twisted.web.client import getPage
import time

from app.worker.backbone import download_all_submission


# TODO compare twisted and multiprocessing multi-thread
# TODO 对比异步asyio 和 multiprocess速度, 请求获取页面 ==> 进程池==> 写入文件
# Twisted: python 异步网络框架

def processPage(page, url):
    # do somewthing here.
    return url, len(page)


def printResults(result):
    for success, value in result:
        if success:
            print 'Success:', value
        else:
            print 'Failure:', value.getErrorMessage()


def printDelta(_, start):
    delta = time.time() - start
    print 'ran in %0.3fs' % (delta,)
    return delta


urls = [
    'http://www.google.com/',
    'http://www.lycos.com/',
    'http://www.bing.com/',
    'http://www.altavista.com/',
    'http://achewood.com/',
]


def fetchURLs():
    callbacks = []
    for url in urls:
        d = getPage(url)
        d.addCallback(processPage, url)
        callbacks.append(d)

    callbacks = defer.DeferredList(callbacks)
    callbacks.addCallback(printResults)
    return callbacks


@defer.inlineCallbacks
def main():
    times = []
    for x in xrange(5):
        d = fetchURLs()
        d.addCallback(printDelta, time.time())
        times.append((yield d))
    print 'avg time: %0.3fs' % (sum(times) / len(times),)


if __name__ == '__main__':
    print 'test'
    reactor.callWhenRunning(main)
    reactor.run()
