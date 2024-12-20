import asyncio


async def start_strongman(name, power):
    print(f'The strongman {name} began the competition.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'The strongman {name} raised {i}')

    print(f'The strongman {name} finished the competition')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Dima', 15))
    task2 = asyncio.create_task(start_strongman('Andrey', 10))
    task3 = asyncio.create_task(start_strongman('Sergey', 9))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())
