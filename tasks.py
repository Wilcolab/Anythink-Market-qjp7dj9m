"""
Task implementations for the workflow engine.
These are predefined tasks that can be used in the workflows.
"""
import asyncio
import json
import random
import string
from typing import Dict, Any


async def print_message_task(params: Dict[str, Any] = None) -> Dict[str, Any]:
    """Task that prints a fixed string - demonstrates basic task execution"""
    message = params.get("message", "Hello from Workflow Engine!") if params else "Hello from Workflow Engine!"
    print(f"📝 Print Task: {message}")
    
    # Simulate some processing time
    await asyncio.sleep(0.5)
    
    return {
        "task": "print_message",
        "result": "completed",
        "message_printed": message,
        "timestamp": asyncio.get_event_loop().time()
    }


async def generate_random_data_task(params: Dict[str, Any] = None) -> Dict[str, Any]:
    """Task that generates and prints a random JSON object - demonstrates data generation"""
    # Generate random data
    random_data = {
        "id": random.randint(1000, 9999),
        "name": ''.join(random.choices(string.ascii_letters, k=8)),
        "score": round(random.uniform(0, 100), 2),
        "active": random.choice([True, False]),
        "tags": [f"tag_{i}" for i in random.sample(range(1, 20), k=random.randint(2, 5))],
        "metadata": {
            "created_at": f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
            "version": f"{random.randint(1, 5)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        }
    }
    
    # Pretty print the JSON
    json_output = json.dumps(random_data, indent=2)
    print(f"🎲 Random Data Generated:\n{json_output}")
    
    # Simulate processing time
    await asyncio.sleep(1.0)
    
    return {
        "task": "generate_random_data",
        "result": "completed",
        "generated_data": random_data,
        "data_size": len(json_output)
    }


async def fibonacci_sum_task(params: Dict[str, Any] = None) -> Dict[str, Any]:
    """Task that calculates sum of first N Fibonacci numbers - demonstrates computation"""
    count = params.get("count", 20) if params else 20
    
    # Calculate Fibonacci sequence
    fibonacci_numbers = []
    a, b = 0, 1
    
    for i in range(count):
        fibonacci_numbers.append(a)
        a, b = b, a + b
        # Add small delay to simulate computation
        if i % 5 == 0:  # Every 5th iteration
            await asyncio.sleep(0.1)
    
    total_sum = sum(fibonacci_numbers)
    
    print(f"🔢 Fibonacci Calculation:")
    print(f"   First {count} numbers: {fibonacci_numbers}")
    print(f"   Sum: {total_sum}")
    
    return {
        "task": "fibonacci_sum",
        "result": "completed",
        "count": count,
        "fibonacci_sequence": fibonacci_numbers,
        "sum": total_sum,
        "largest_number": fibonacci_numbers[-1] if fibonacci_numbers else 0
    }