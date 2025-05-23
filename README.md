
# Conway's Game of Life – Python + Pygame

An interactive visualization of Conway’s Game of Life implemented in Python using **Pygame**. This simulation demonstrates how simple rules can lead to complex behavior in a grid of cells.

---

## 🧬 Description

**Conway’s Game of Life** is a cellular automaton that simulates how cells live, die, or reproduce based on the state of their neighbors. Each cell can be either **alive** or **dead**, and the system evolves in discrete time steps.

### 🔁 Game Rules:

1. A live cell with **fewer than two** live neighbors dies (underpopulation).
2. A live cell with **two or three** live neighbors survives.
3. A live cell with **more than three** live neighbors dies (overpopulation).
4. A dead cell with **exactly three** live neighbors becomes alive (reproduction).

---

## 🗂 Project Structure

```
├── main.py          # Entry point of the application
├── game_logic.py    # Core game rules and board operations
├── gui.py           # Pygame-based visualization
├── config.py        # Configuration and settings
├── io_operations.py # Save/Load pattern functionality
└── pattern.txt      # Saved patterns
```

---

## ⚙️ Requirements

* Python 3.x
* Pygame library

### 💾 Installation

```bash
git clone <repository_url>
cd conways-game-of-life
pip install pygame
```

---

## ▶️ How to Run

```bash
python main.py
```

### 🔧 Optional Arguments

```bash
python main.py --width 80 --height 40 --fps 15
```

---

## 🕹 Controls

| Action              | Key / Mouse |
| ------------------- | ----------- |
| Make cell **alive** | Left Click  |
| Make cell **dead**  | Right Click |
| Play/Pause          | Spacebar    |
| Step one generation | N           |
| Generate random     | R           |
| Clear board         | C           |
| Save pattern        | S           |
| Load saved pattern  | L           |

---

## 🧪 Sample Patterns

1. **Glider** – Moves diagonally:

   ```
   000
   010
   111
   ```

2. **Blinker** – Oscillates between two states:

   ```
   000
   111
   000
   ```

---

## 🔍 Features

* Adjustable grid size via command-line arguments
* Save & load custom patterns (`pattern.txt`)
* Generation counter
* Pause/Resume simulation
* Step-by-step evolution mode
* Clean, modular Python code

---

## 🤝 Contributing

Feel free to fork this repo, suggest features, or raise pull requests to improve the simulation!
