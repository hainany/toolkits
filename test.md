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

    memory use: 43.625MB, add memory: 0.18359375MB
    memory use: 43.765625MB, add memory: 0.140625MB
    memory use: 43.9375MB, add memory: 0.171875MB
    memory use: 44.0546875MB, add memory: 0.1171875MB
    memory use: 44.2421875MB, add memory: 0.1875MB
    memory use: 44.390625MB, add memory: 0.1484375MB
    memory use: 44.57421875MB, add memory: 0.18359375MB
    memory use: 44.7109375MB, add memory: 0.13671875MB
