import cv2
from env import GridWorld

def main():
    env = GridWorld()
    obs = env.reset()

    for step in range(300):
        # Simple random policy
        action = "FORWARD"
        obs = env.step(action)

        # Show image
        cv2.imshow("GridWorld Simulation", obs["image"])

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
