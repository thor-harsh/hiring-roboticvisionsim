
# Autonomous Navigation Hiring Challenge

## Overview
This hiring challenge is designed to evaluate a candidate’s ability to build a **complete autonomous agent** using noisy sensor inputs and visual perception.

The candidate is expected to:
- Understand noisy sensors
- Perform basic perception from images
- Design a clean agent architecture
- Navigate to a goal while avoiding obstacles

---

## What You Are Given

You are provided with a **fully working simulator environment**.

### Files Provided (Order may be different)
```
.
├── env.py          # Simulation environment (DO NOT MODIFY)
├── run_env.py      # Runs the environment loop
├── agent.py        # (YOU IMPLEMENT THIS)
├── requirements.txt
└── README.md
```

You **must not modify** `env.py` or `run_env.py`.

---

## Environment Description

The simulator represents a **2D grid world** with:

- 🟥 Red dot: Robot
- 🟩 Green dot: Goal
- ⬜ White blocks: Obstacles
- ⬛ Black background

Obstacles are **randomized every episode**.

---

## Observation Format

At every step, your agent receives an observation dictionary:

```python
obs = {
    "odometry": [x_noisy, y_noisy],   # Noisy position estimate
    "heading": theta_noisy,           # Noisy orientation (radians)
    "image": image_frame              # Camera image (numpy array)
}
```

### Important Notes
- Odometry and heading are **intentionally noisy**
- The image is the **only reliable way** to detect obstacles
- Obstacle positions **change every episode**
- Hardcoding obstacle locations will fail evaluation

---

## Action Space

Your agent must return **one of the following actions**:

```python
"FORWARD"
"LEFT"
"RIGHT"
```

These actions are passed directly to the environment.

---

## Your Task

You must implement an autonomous agent that:

1. Uses noisy odometry and heading
2. Optionally smooths or filters sensor noise
3. Extracts obstacle information from the image
4. Navigates toward the goal
5. Avoids obstacles
6. Works across multiple randomized episodes

---

## What Is NOT Required

- No deep learning
- No training loop
- No reinforcement learning
- No datasets
- No Kalman filters required

Classical control + classical computer vision is sufficient.

---

## Expected Agent Interface

You must implement the following file:

### `agent.py`
```python
class Agent:
    def __init__(self):
        pass

    def act(self, obs):
        '''
        Input:
            obs (dict): observation from environment

        Output:
            action (str): one of ["FORWARD", "LEFT", "RIGHT"]
        '''
        return "FORWARD"
```

You may create **helper classes or files** if needed.

---

## Allowed Libraries

You may use:
- `numpy`
- `opencv-python`
- `math`
- `collections`

No external ML frameworks are needed.

---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the simulator
```bash
python run_env.py
```

A window will open showing the simulation.

---

## How to Inspect Observations (Example)

Inside your agent:
```python
print(obs["odometry"])
print(obs["heading"])

cv2.imshow("camera", obs["image"])
cv2.waitKey(1)
```

---

## Evaluation Criteria

Your submission will be evaluated on:

### 1. Correctness
- Reaches the goal
- Avoids obstacles

### 2. Robustness
- Works across random obstacle placements
- Handles sensor noise

### 3. Engineering Quality
- Clean architecture
- Separation of perception, estimation, control
- Readable code

### 4. Reasoning
- Clear comments explaining decisions

---

## Automatic Evaluation

Your agent will be evaluated over **multiple episodes** with:
- Randomized obstacle layouts
- Different start positions

Metrics include:
- Success rate
- Collision count
- Average distance to goal

Evaluation logic is **not shared**.

---

## Time Expectation

This task is designed to be completed in:

⏱ **6–10 hours**

Over-engineering is discouraged.

---

## Submission Instructions

Submit:
- `agent.py`
- Any helper files you created

Do NOT submit:
- Modified environment files
- Large binaries or datasets

---

Good luck.
