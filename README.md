# TestTest_My_python_skill
Note for udemy couse exercise, Python Coding.

If you expert in python developer pass this repo.

TryHackme
Race Condition
#Real World Analogy

Picture the following situation. You call a restaurant to reserve a table for a crucial business lunch. You are familiar with the restaurant and its setup. One particular table, number 17, is your preferred choice, considering it has a nice view and is relatively isolated. You call to make a reservation for Table 17; the host confirms it is free as no “Reserved” tag is placed on it. At the same time, another customer is talking with another host and making a reservation for the same table.

Who really reserved the table? That’s a race condition.

Why did this happen? This unlucky situation happened because more than one host was taking reservations; furthermore, it took the host a few minutes to fetch the “Reserved” tag and put it on the table after updating the daily reservation book. There is at least a one-minute window for another client to reserve a reserved table.

Similarly, when one thread checks a value to perform an action, another thread might change that value before the action takes place.
Example A

Let’s consider this scenario:

    A bank account has $100.
    Two threads try to withdraw money at the same time.
    Thread 1 checks the balance (sees $100) and withdraws $45.
    Before Thread 1 updates the balance, Thread 2 also checks the balance (incorrectly sees $100) and withdraws $35.

We cannot be 100% certain which thread will get to update the remaining balance first; however, let’s assume that it is Thread 1. Thread 1 will set the remaining balance to $55. Afterwards, Thread 2 might set the remaining balance to $65 if not appropriately handled. (Thread 2 calculated that $65 should remain in the account after the withdrawal because the balance was $100 when Thread 2 checked it.) In other words, the user made two withdrawals, but the account balance was deducted only for the second one because Thread 2 said so!
Example B

Let’s consider another scenario:

    A bank account has $75.
    Two threads try to withdraw money at the same time.
    Thread 1 checks the balance (sees $75) and withdraws $50.
    Before Thread 1 updates the balance, Thread 2 checks the balance (incorrectly sees $75) and withdraws $50.

Thread 2 will proceed with the withdrawal, although such a transaction should have been declined.

Examples A and B demonstrate a Time-of-Check to Time-of-Use (TOCTOU) vulnerability.