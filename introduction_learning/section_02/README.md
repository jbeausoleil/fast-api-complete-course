# 🧟 Hero vs. Enemies Battle Simulator

A simple turn-based battle simulation game written in Python where a `Hero` battles against different types of enemies like `Zombies` and `Ogres` using weapons. This project demonstrates the use of object-oriented programming, inheritance, and modular structure in Python.

---

## 📁 Project Structure

```
.
├── main.py          # Game entry point and battle logic
├── hero.py          # Hero class definition
├── enemy.py         # Base Enemy class
├── ogre.py          # Ogre enemy subclass
├── zombie.py        # Zombie enemy subclass
├── weapon.py        # Weapon class used by Hero
```

---

## 🚀 How to Run

1. Clone the repository or download the files.

2. Make sure you have Python 3 installed.

3. Run the game:

```bash
python main.py
```

You’ll see a simulated battle in your console output between the hero and a chosen enemy type.

---

## ⚔️ Game Logic

- The `Hero` and `Enemy` both have `health_points` and `attack_damage`.
- The `Hero` can optionally equip a `Weapon`, which may increase attack power.
- The game loops through attack rounds until one party's health reaches zero.
- Enemies (`Zombie`, `Ogre`) inherit from the base `Enemy` class and may have custom attributes or behavior.

---

## ✅ Features

- Object-Oriented Design with `@dataclass` usage
- Modular, extensible file structure
- Easy to add new enemies or weapons
- Simple terminal-based gameplay