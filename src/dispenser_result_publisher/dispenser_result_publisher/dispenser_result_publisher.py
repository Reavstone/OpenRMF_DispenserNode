import rclpy
from rclpy.node import Node

from rmf_dispenser_msgs.msg import DispenserResult, DispenserRequest

import time

class DispenserResponderNode(Node):

    def __init__(self):
        super().__init__('dispenser_responder')
        self.request_sub = self.create_subscription(
            DispenserRequest,
            '/dispenser_requests',
            self.request_callback,
            10
        )
        self.result_pub = self.create_publisher(
            DispenserResult,
            '/dispenser_results',
            10
        )
        self.get_logger().info('Dispenser Responder Node has been started.')

    def request_callback(self, msg):
        self.get_logger().info(f'Received request: {msg.request_guid} from {msg.target_guid}')
        
        start_time = time.time()

        for i in range(1): # for this example 1 answers per request.
            time.sleep(1) # delay

            response_time = time.time() - start_time

            response = DispenserResult()
            response.time.sec = int(response_time)
            response.time.nanosec = int((response_time - int(response_time)) * 1e9)
            response.request_guid = msg.request_guid
            response.source_guid = msg.target_guid
            response.status = DispenserResult.SUCCESS

            self.result_pub.publish(response)
            self.get_logger().info(f'Published response: {response.request_guid} with status {response.status} after {response_time:.2f} seconds')


def main(args=None):
    rclpy.init(args=args)

    dispenser_responder_node = DispenserResponderNode()

    rclpy.spin(dispenser_responder_node)
    dispenser_responder_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()