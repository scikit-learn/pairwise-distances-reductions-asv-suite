import time
from abc import ABC, abstractmethod


class Benchmark(ABC):
    """Abstract base class for all the benchmarks"""

    # This timer accounts for wall time with precision
    # in nanoseconds
    timer = time.perf_counter_ns
    processes = 1
    timeout = 1000

    @abstractmethod
    def params(self):
        pass
