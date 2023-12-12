import grpc
import Reddit_pb2
import Reddit_pb2_grpc

from typing import Optional



class RedditClient:

    def __init__(self, host: str, port: int) -> None:
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = Reddit_pb2_grpc.RedditServiceStub(self.channel)
        self.stop_subscribe = False

    def create_post(self, title: str, text:str,post_state: int, subreddit_id: str, image_url:Optional[str] = None, video_url: Optional[str] = None, author:Optional[str]=None):
        post = Reddit_pb2.Post(title=title, text=text, status=post_state, parent_subreddit_id=subreddit_id)
        if image_url is not None and video_url is not None:
            raise ValueError("Only one of image_url and video_url can be set")
        if image_url is not None:
            post.image_url = image_url
        if video_url is not None:
            post.video_url = video_url
        if author is not None:
            post.author = author
        return self.stub.CreatePost(post).__dict__
    
    def upvote_post(self, post_id: str):
        postRequest = Reddit_pb2.PostRequest(post_id=post_id)
        return self.stub.UpvotePost(postRequest).__dict__

    def downvote_post(self, post_id: str):
        postRequest = Reddit_pb2.PostRequest(post_id=post_id)
        return self.stub.DownvotePost(postRequest).__dict__
    
    def get_post_content(self, post_id: str):
        postRequest = Reddit_pb2.PostRequest(post_id=post_id)
        return self.stub.GetPostContent(postRequest).__dict__


    def create_comment(self, parent_id:str, author:str, text:str, comment_state: int):
        comment = Reddit_pb2.Comment(parent_id=parent_id, author=author, text=text, status=comment_state)
        return self.stub.CreateComment(comment).__dict__
    
    def upvote_comment(self, comment_id: str):
        commentRequest = Reddit_pb2.CommentRequest(comment_id=comment_id)
        return self.stub.UpvoteComment(commentRequest).__dict__

    def downvote_comment(self, comment_id: str):
        commentRequest = Reddit_pb2.CommentRequest(comment_id=comment_id)
        return self.stub.DownvoteComment(commentRequest).__dict__
    
    def get_most_comment(self, post_id: str, n: int):
        getnmostRequest = Reddit_pb2.GetNMostRequest(post_id=post_id, N=n)
        return list(map(lambda response: response.__dict__, self.stub.GetNMostComment(getnmostRequest)))
    
    def expand_comment_branch(self, comment_id:str, n: int):
        expandcommentRequest = Reddit_pb2.ExpandCommentRequest(comment_id=comment_id,N=n)
        return list(map(lambda response: response.__dict__, self.stub.ExpandCommentBranch(expandcommentRequest).expanded_comments))
    
    def monitor_update(self, post_id:str, comment_ids):
        request = Reddit_pb2.MonitorUpdateRequest(post_id=post_id, comment_id=comment_ids)
        responses = self.stub.MonitorUpdate(iter([request]))
        return map(lambda res: (res.post_score, [item.__dict__ for item in res.comment_scores]) ,responses)

    

    def close(self):
        self.channel.close()
        self.stop_subscribe = True
        

if __name__ == '__main__':
    run()