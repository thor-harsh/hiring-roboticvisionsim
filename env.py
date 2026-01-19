import numpy as np
import cv2

class GridWorld:
    def __init__(self, size=500):
        self.size = size
        self.reset()

    def reset(self):
        self.robot = np.array([50.0, 50.0, 0.0])  # x, y, theta
        self.goal = np.array([450.0, 450.0])
        self.obstacles = [
            (200, 200, 60, 60),
            (300, 100, 50, 120)
        ]
        return self.get_observation()

    def step(self, action):
        v = 5.0
        dt = 1.0

        if action == "LEFT":
            self.robot[2] += 0.2
        elif action == "RIGHT":
            self.robot[2] -= 0.2
        elif action == "FORWARD":
            self.robot[0] += v * np.cos(self.robot[2]) * dt
            self.robot[1] += v * np.sin(self.robot[2]) * dt

        self.robot[:2] = np.clip(self.robot[:2], 0, self.size)
        return self.get_observation()

    def get_observation(self):
        return {
            "odometry": self.get_noisy_odometry(),
            "heading": self.get_noisy_heading(),
            "image": self.render()
        }

    def get_noisy_odometry(self):
        return self.robot[:2] + np.random.normal(0, 2.0, size=2)

    def get_noisy_heading(self):
        return self.robot[2] + np.random.normal(0, 0.05)

    def render(self):
        img = np.zeros((self.size, self.size, 3), dtype=np.uint8)

        # Draw obstacles
        for x, y, w, h in self.obstacles:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), -1)

        # Draw goal
        cv2.circle(img, tuple(self.goal.astype(int)), 15, (0, 255, 0), -1)

        # Draw robot
        x, y, theta = self.robot
        pt1 = (int(x), int(y))
        pt2 = (int(x + 20*np.cos(theta)), int(y + 20*np.sin(theta)))
        cv2.line(img, pt1, pt2, (0, 0, 255), 3)

        return img