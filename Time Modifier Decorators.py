import time
def decorator(func):
    def modified():
        func()
        print(f"Took {t_final} seconds to run")
    return modified 
@decorator
def func():
    t1=time.time()
    time.sleep(2)
    x=5
    if x==5:
        print("Hi World Lets go To Heaven")
        print("OOOOH YEAAAAH")
        print("GOGOGO")
        print("POGOGOOGGOGO")
        print("Sinchan")
    else:
        pass
    t2=time.time()
    global t_final
    t_final=t2-t1
    return t_final
func()





    