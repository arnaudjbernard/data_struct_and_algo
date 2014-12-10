from perf import multi_pipe
from perf import multi_queue
from perf import multi_joinablequeue


def main():
    multi_pipe.main()
    multi_queue.main()
    multi_joinablequeue.main()


if __name__ == "__main__":
    main()