class Agent:
    def __init__(self):
        """
        Here you can initialize any state here.
        You may store maps, filters, history, etc.
        """
        pass

    def act(self, obs):
        """
        Input:
            obs = {
                "odometry": [x_noisy, y_noisy],
                "heading": theta_noisy,
                "image": image (numpy array)
            }

        Output:
            action (str): One of ["FORWARD", "LEFT", "RIGHT"]
        """
        return "FORWARD"
