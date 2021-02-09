# Python的多任务

[//]: # (__author__ = "Clark Aaron")

多任务是当下需求的重要特征，实这一目标的技术手段有进程技术、线程技术、协程技术以及CPU的并行与并发技术。

* 任务分为计算密集型与IO密集型;
* 计算密集型的多任务应与CPU内核数相同;
* IO密集性:的多任务可以更多;

* 事件驱动模型 (异步IO模型) Nginx：在Python中称为协程;

* 使用 Master-Worker模式:一个Master(负责分配任务),多个Worker(执行任务)
* 异步IO可以提升IO密集型的任务处理能力;

## 进程

一个独立的任务，具有独立的内存空间；是系统中常见的一个任务。

在Python中，提供一个multiprocessing模块来实现有关进程的技术。

### multiprocessing

* 【功能】主进程创建子进程：

  * 直接调用Process创建子进程：

    ```python
    from multiprocessing import Process

    process_one = Process(target=<function>,args=<function args>)
    process_two = Process(target=<function>,args=<function args>)

    process_one.start()
    process_two.start()

    process_one.join()
    process_two.join()
    ```

  * 继承调用Process创建子进程：

    ```python
    from multiprocessing import Process
    class <class name>(Process):
      def __init__(self):
          pass
      def run(self):
          pass
    process_one = <class name>()
    process_two = <class name>()

    process_one.start()
    process_two.start()

    process_one.join()
    process_two.join()
    ```

* 【功能】主进程守护子进程：

* 【功能】进程间数据同步：

* 【功能】进程间通信技术：

* 【功能】进程池的管理：

* 【功能】回调函数：

* 创建子进程:
  ```
  import os
  print('Process (%s) start...' % os.getpid())
  # Only works on Unix/Linux/Mac:
  pid = os.fork()
  if pid == 0:
      print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
  else:
      print('I (%s) just created a child process (%s).' % (os.getpid(), pid)
  ```

* 进程池的方式:
  ```
  from multiprocessing import Pool
    import os, time, random

    def long_time_task(name):
        print('Run task %s (%s)...' % (name, os.getpid()))
        start = time.time()
        time.sleep(random.random() * 3)
        end = time.time()
        print('Task %s runs %0.2f seconds.' % (name, (end - start)))

    if __name__=='__main__':
        print('Parent process %s.' % os.getpid())
        p = Pool(4)  #同时运行4个进程
        for i in range(5):
            p.apply_async(long_time_task, args=(i,))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')
  ```
  * 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

### 子进程

* 使用subprocess模块实现子进程的启动,并控制其输入与输出;
* call():启动一个子进程;
* communicate():对子进程进行数据输入;

* Python的multiprocessing模块实现进程间的通信,使用Queue/Pipes交换数据:
  ```
  rom multiprocessing import Process, Queue
    import os, time, random

    # 写数据进程执行的代码:
    def write(q):
        print('Process to write: %s' % os.getpid())
        for value in ['A', 'B', 'C']:
            print('Put %s to queue...' % value)
            q.put(value)
            time.sleep(random.random())

    # 读数据进程执行的代码:
    def read(q):
        print('Process to read: %s' % os.getpid())
        while True:
            value = q.get(True)
            print('Get %s from queue.' % value)

    if __name__=='__main__':
        # 父进程创建Queue，并传给各个子进程：
        q = Queue()
        pw = Process(target=write, args=(q,))
        pr = Process(target=read, args=(q,))
        # 启动子进程pw，写入:
        pw.start()
        # 启动子进程pr，读取:
        pr.start()
        # 等待pw结束:
        pw.join()
        # pr进程里是死循环，无法等待其结束，只能强行终止:
        pr.terminate()
  ```
* 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

### 分布式(多机运行)

* 使用multiprocess中的managers模块实现多级运行:
  ```
  import random, time, queue
    from multiprocessing.managers import BaseManager

    # 发送任务的队列:
    task_queue = queue.Queue()
    # 接收结果的队列:
    result_queue = queue.Queue()

    # 从BaseManager继承的QueueManager:
    class QueueManager(BaseManager):
        pass

    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable=lambda: task_queue)
    QueueManager.register('get_result_queue', callable=lambda: result_queue)
    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('', 5000), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')
  ```
  ```
  import time, sys, queue
    from multiprocessing.managers import BaseManager

    # 创建类似的QueueManager:
    class QueueManager(BaseManager):
        pass

    # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # 连接到服务器，也就是运行task_master.py的机器:
    server_addr = '127.0.0.1'
    print('Connect to server %s...' % server_addr)
    # 端口和验证码注意保持与task_master.py设置的完全一致:
    m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
    # 从网络连接:
    m.connect()
    # 获取Queue的对象:
    task = m.get_task_queue()
    result = m.get_result_queue()
    # 从task队列取任务,并把结果写入result队列:
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)
        except Queue.Empty:
            print('task queue is empty.')
    # 处理结束:
    print('worker exit.')
  ```

## 线程

* 多线程:Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
  ```
  import time, threading
    # 新线程执行的代码:
    def loop():
        print('thread %s is running...' % threading.current_thread().name)
        n = 0
        while n < 5:
            n = n + 1
            print('thread %s >>> %s' % (threading.current_thread().name, n))
            time.sleep(1)
        print('thread %s ended.' % threading.current_thread().name)

    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
  ```

### 线程的变量共享的保护

* 使用threading.Lock()实现数据上锁;
  ```
  balance = 0
    lock = threading.Lock()

    def run_thread(n):
        for i in range(100000):
            # 先要获取锁:
            lock.acquire()
            try:
                # 放心地改吧:
                change_it(n)
            finally:
                # 改完了一定要释放锁:
                lock.release()
  ```
* Python在使用多线程时,有一个GIL(Global Interpreter Lock),在一个进程获取GIL锁后执行100条字节码后自动给释放GIL锁,只能用到一个CPU内核;多线程不能实现多核任务,但多进程可以实现;

* 多线程间局部变量间的传送:使用ThreadLocal实现
  ```
  import threading 
    # 创建全局ThreadLocal对象:
    local_school = threading.local()

    def process_student():
        # 获取当前线程关联的student:
        std = local_school.student
        print('Hello, %s (in %s)' % (std, threading.current_thread().name))

    def process_thread(name):
        # 绑定ThreadLocal的student:
        local_school.student = name
        process_student()

    t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
  ```

## 协程

* 协程(Coroutine):又称微线程、纤程;

* 在Python中通过generator实现协程;
* 

### asyncio
* 在Python3.4之后引入对异步IO的支持,编程模型是一个消息模型;
* 在asyncio模块中获取一个EventLoop的引用,然后把需要执行的协程扔到EvevtLoop中执行,就实现异步;
  ```
  import asyncio
  @asyncio.coroutine
  def hello():
      print("Hello world!")
      # 异步调用asyncio.sleep(1):
      r = yield from asyncio.sleep(1)
      print("Hello again!")

  # 获取EventLoop:
  loop = asyncio.get_event_loop()
  # 执行coroutine
  loop.run_until_complete(hello())
  loop.close()
  ```
* 双协程:
  ```
  import threading
  import asyncio

  @asyncio.coroutine
  def hello():
      print('Hello world! (%s)' % threading.currentThread())
      yield from asyncio.sleep(1)
      print('Hello again! (%s)' % threading.currentThread())

  loop = asyncio.get_event_loop()
  tasks = [hello(), hello()]
  loop.run_until_complete(asyncio.wait(tasks))
  loop.close()
  ```


### async/await
* 在Python3.5中引入了async与await替代@asyncio.coroutine与yield from;


### aiohttp
* aiohttp是基于asyncio实现HTTP框架;
* 安装`aiohttp`;
* 数据库的异步驱动:aiomysql;

## 日志

* GIL(全局解释器锁)：保证同一时刻只有一个线程在工作。