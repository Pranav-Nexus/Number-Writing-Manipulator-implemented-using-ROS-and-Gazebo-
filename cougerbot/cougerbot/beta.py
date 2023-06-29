import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

class ManipulatorController(Node):
    def __init__(self):
        super().__init__('manipulator_controller')
        self.publisher = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory', 10)
        self.timer = self.create_timer(2.0, self.move_manipulator)
        self.current_position_index = 0

        self.positions = []

        numbers = [
            [],  # 0
            [
                [0.0, 0.7, -1.5, 0.0],
                [0.0, 0.7, -0.5, 0.0],
                [0.6, 0.7, -0.5, 0.0]
            ],  # 1
            [
                [0.6, 0.0, 0.0, 0.0],
                [-0.6, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0],
                [0.0, 0.4, 0.0, 0.0]
            ],  # 2
            [
                [0.6, 0.7, -1.5, 0.0],
                [0.0, 0.7, -1.5, 0.0],
                [0.0, 0.7, -0.5, 0.0],
                [0.0, 0.7, -1.0, 0.0],
                [0.6, 0.7, -1.0, 0.0]
            ],  # 3
            [
                [0.6, 0.7, -1.5, 0.0],
                [0.0, 0.7, -1.5, 0.0],
                [0.0, 0.7, -0.5, 0.0],
                [0.6, 0.7, -0.5, 0.0],
                [0.0, 0.7, -0.5, 0.0],
                [0.0, 0.7, -1.0, 0.0],
                [0.6, 0.7, -1.0, 0.0]
            ],  # 4
            [
                [0.0, 0.3, -0.3, 0.0],
                [0.3, 0.3, -0.3, 0.0],
                [0.3, -0.4, 0.4, 0.0],
                [0.3, 0.4, -0.4, 0.0],
                [0.3, 0.3, -0.3, 0.0],
                [-0.3, 0.3, -0.3, 0.0],
                [-0.3, -0.4, 0.4, 0.0],
                [-0.3, 0.4, -0.4, 0.0]
            ],  # 5
            [
                [0.0, 0.0, 0.0, 0.0],
                [0.3, 0.7, -0.7, 0.0],
                [0.0, 0.0, 0.0, 0.0],
                [-0.3, 0.7, -0.7, 0.0],
                [-0.15, 0.35, -0.35, 0.0],
                [0.15, 0.35, -0.35, 0.0]
            ],  # 6
            [
                [0.0, 0.7, -1.5, 0.0],
                [0.6, 0.7, -1.5, 0.0]
            ],  # 7
            [
                [0.0, 0.7, -1.5, 0.0],
                [0.6, 0.7, -1.5, 0.0],
                [0.0, 0.7, -0.5, 0.0]
            ],  # 8
            [
                [0.0, 0.7, -1.5, 0.0],
                [0.6, 0.7, -1.5, 0.0],
                [0.0, 0.7, -1.0, 0.0],
                [0.6, 0.7, -1.0, 0.0]
            ]  # 9
        ]

        print("Enter a number from 0 to 9:")
        number = input()

        try:
            number = int(number)
            if 0 <= number <= 9:
                self.positions = numbers[number]
            else:
                self.positions = []
                print("Invalid number entered!")
        except ValueError:
            self.positions = []
            print("Invalid number entered!")

    def move_manipulator(self):
        if self.current_position_index >= len(self.positions):
            self.get_logger().info("Manipulator reached the final position.")
            return

        position = self.positions[self.current_position_index]
        self.get_logger().info(f"Moving manipulator to position: {position}")

        trajectory = JointTrajectory()
        trajectory.joint_names = ['hip', 'shoulder', 'elbow', 'wrist']

        point = JointTrajectoryPoint()
        point.positions = position
        point.time_from_start = Duration(sec=2)  # Set seconds

        trajectory.points.append(point)
        self.publisher.publish(trajectory)

        self.current_position_index += 1

def main(args=None):
    rclpy.init(args=args)
    manipulator_controller = ManipulatorController()
    rclpy.spin(manipulator_controller)
    manipulator_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
