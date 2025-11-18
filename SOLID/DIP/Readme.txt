High-level modules should not depend on low-level modules. Both should depend on abstractions.
| Concept       | Description                                                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Principle** | **Dependency Inversion Principle (DIP)**                                                                                                                      |
| **Problem**   | High-level modules depend directly on low-level modules, causing tight coupling and making the system hard to change or test.                                 |
| **Solution**  | Introduce **abstractions (interfaces)** that both high-level and low-level modules depend on. High-level code should not depend on implementation details.    |
| **Benefit**   | Promotes flexibility, easier testing (mocking), and better maintainability — you can swap implementations (e.g., I²C, UART, SPI) without changing core logic. |
