import Reddit_pb2
import Reddit_pb2_grpc
import unittest
from client import RedditClient
from high_level_function import high_level_function
from unittest.mock import patch, Mock

class MockTest (unittest.TestCase):
    @patch('client.RedditClient')  # Replace 'your_module' with the actual module name
    def test_high_level_function(self, mock_client):
        # Set a mock object
        mock_client_object = Mock(spec=RedditClient)

        # Hardcoded responses
        post_id = "1"
        post_content = {"post_id": post_id, "title": "Test Post Title", "content": "This is a test", "score": 12}
        most_upvoted_comments = [{"comment_id": "2", "score": 10, "parent_id": "1"}]
        expanded_comment_replies = [{"comment_id": "3", "score": 8, "parent_id": "2"}]

        # Set the return values for mock methods
        mock_client_object.get_post_content.return_value = post_content
        mock_client_object.get_most_comment.return_value = most_upvoted_comments
        mock_client_object.expand_comment_branch.return_value = expanded_comment_replies

        # Set the mock API as the instance defined
        mock_client.return_value = mock_client_object


        # Call the high-level function
        result = high_level_function(mock_client_object, post_id)

        # Assertions based on the business logic
        self.assertEqual(result["comment_id"], "3")


if __name__ == "__main__":
    unittest.main()