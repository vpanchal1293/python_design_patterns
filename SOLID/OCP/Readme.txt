Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.
| Concept       | Description                                                                                                                                                |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Principle** | **Open/Closed Principle (OCP)**                                                                                                                            |
| **Problem**   | Modifying existing classes every time a new behavior or feature is added causes bugs and breaks existing functionality.                                    |
| **Solution**  | Classes should be **open for extension but closed for modification** — extend behavior using inheritance or composition instead of altering existing code. |
| **Benefit**   | Makes systems easier to extend without risking regressions; supports plug-in or modular architectures.                                                     |
