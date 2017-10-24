from multiprocessing import Process
from time import sleep
def test(t):
    sleep(t)


def run_with_limited_time(func, args, kwargs, time):
    """Runs a function with time limit

    :param func: The function to run
    :param args: The functions args, given as tuple
    :param kwargs: The functions keywords, given as dict
    :param time: The time limit in seconds
    :return: True if the function ended successfully. False if it was terminated.
    """
    p = Process(target=func, args=args, kwargs=kwargs)
    p.start()
    p.join(time)
    if p.is_alive():
        p.terminate()
        return False

    return True

if __name__ == "__main__":
    run_with_limited_time(test,(5,),{}, 6) # return True
    run_with_limited_time(test,(7,),{}, 6) # return False
