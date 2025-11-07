import asyncio
async def fetch_data() -> str:
    print("Fetching data...")
    await asyncio.sleep(1)  # Simulate an async operation
    return "Data fetched successfully"

async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay}s")



async def main():
    await fetch_data()
    await asyncio.gather(
        task("Task A", 2),
        task("Task B", 3),
        task("Task C", 1)
    )

result = asyncio.run(main())