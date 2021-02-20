```python
import gym
import retro
env = retro.make('Pong-Atari2600')
#env = gym.make('Pong-v0')
import os
import psutil
pid = os.getpid()
py = psutil.Process(pid)
pre_memoryUse = 0
while 1:
    env.reset()
    memoryUse = py.memory_info()[0] / 2.**20
    print('memory use: {}MB'.format(memoryUse))
    add_memory = memoryUse - pre_memoryUse
    print('add memory: {}MB'.format(add_memory))
    pre_memoryUse = memoryUse
```
