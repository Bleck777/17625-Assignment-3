import Reddit_pb2
import Reddit_pb2_grpc
from client import RedditClient

def high_level_function(api_client: RedditClient, post_id: str):
    # Step 1: Retrive a post
    post = api_client.get_post_content(post_id)

    # Step 2: Retrieve the most upvoted comments (1) under the post
    n = 1
    comments = api_client.get_most_comment(post_id,n)

    # Step 3: Expand the most upvoted comment
    if len(comments) == 0:
        return None
    else:
        n2 = 1
        comment_id = comments[0]["comment_id"]
        replies = api_client.expand_comment_branch(comment_id, n2)
        if len(replies) == 0:
            return None
        else:
            for reply in replies:
                if reply["parent_id"] == comment_id:
                    return reply
