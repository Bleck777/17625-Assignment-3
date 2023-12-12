import grpc
import Reddit_pb2
import Reddit_pb2_grpc
import datetime
import argparse
from concurrent import futures
from typing import List, Dict



class RedditServiceServicer(Reddit_pb2_grpc.RedditServiceServicer):
    posts: Dict[int, Reddit_pb2.Post] = {}
    comments: Dict[int, Reddit_pb2.Comment] = {}
    current_id = 0

    def __init__(self):
        self.monitoring_post = None
        self.monitoring_comments = []
        super().__init__()

    def PublishPost(self, request, context):
        # TODO: This is only an example. Delete this when you are done
        # Here you can add logic to handle post publishing
        print(f"Received a request to publish a post: {request.post.title}")
        # For simplicity, we are just returning a fixed message and post ID
        return Reddit_pb2.PublishPostResponse(postId="123", message="Post Published Successfully")

    def SendComment(self, request, context):
        # TODO: This is only an example. Delete this when you are done
        # Here you can add logic to handle comment sending
        print(f"Received a comment: {request.comment.text} by user {request.comment.author.userId}")
        # For simplicity, we are just returning a fixed message and comment ID
        return Reddit_pb2.SendCommentResponse(commentId="456", message="Comment Sent Successfully")
    
    def CreatePost(self, request, context):
        post = request
        post.score = 0
        post.pub_date = datetime.datetime.now().isoformat()
        post.post_id = str(self.current_id)
        self.posts[self.current_id] = post
        self.current_id += 1
        print(f"Requested to publish a post: {post.title} @ {post.pub_date}, assigned post ID: {post.post_id}")
        return post

    def UpvotePost(self, request, context):
        print(f"Requested to upvote post with ID: {request.post_id}")
        post = self.posts[int(request.post_id)]
        post.score += 1
        return post

    def DownvotePost(self, request, context):
        print(f"Requested to downvote post with ID: {request.post_id}")
        post = self.posts[int(request.post_id)]
        post.score -= 1
        return post

    def GetPostContent(self, request, context):
        print(f"Requested to get post with ID: {request.post_id}")
        post = self.posts[int(request.post_id)]
        return post

    def CreateComment(self, request, context):
        comment = request
        comment.score = 0
        comment.pub_date = datetime.datetime.now().isoformat()
        comment.comment_id = str(self.current_id)
        self.comments[self.current_id] = comment
        self.current_id += 1
        print(f"Requested to publish a comment: {comment.text} @ {comment.pub_date}, assigned comment ID: {comment.comment_id}")
        return comment

    def UpvoteComment(self, request, context):
        print(f"Requested to upvote comment with ID: {request.comment_id}")
        comment = self.comments[int(request.comment_id)]
        comment.score += 1
        return comment

    def DownvoteComment(self, request, context):
        print(f"Requested to downvote comment with ID: {request.comment_id}")
        comment = self.comments[int(request.comment_id)]
        comment.score -= 1
        return comment
    
    def _get_n_comment_under_id(self, id, n):
        all_matched = []
        for cmt in self.comments:
            if cmt.parent_id == id:
                all_matched.append(cmt)
        all_matched.sort(key = lambda cmt: cmt.score, reverse=True)
        return all_matched[:n]

    def GetNMostComment(self, request, context):
        results = self._get_n_comment_under_id(request.post_id, request.N)
        return Reddit_pb2.GetNMostResponse(most_comment=results)

    def ExpandCommentBranch(self, request, context):
        root = self.comments[request.comment_id]
        result_first = self._get_n_comment_under_id(request.comment_id, request.N)
        results = [result_first]
        for res in result_first:
            result_res = self._get_n_comment_under_id(res.comment_id, request.N)
            results.append(result_res)
        result = sum(results,start=[])
        return Reddit_pb2.ExpandCommentResponse(root_comment=root, expanded_comments=result)

    def MonitorUpdate(self, request_iterator, context):
        for request in request_iterator:
            if request.post_id != "":
                self.monitoring_post = int(request.post_id)
            for cmt in request.comment_id:
                self.monitoring_comments.append(int(cmt))
            
            post_score = self.posts[self.monitoring_post]
            cmt_score = []
            for cmt in self.monitoring_comments:
                cws = Reddit_pb2.CommentWithScore(comment_id=cmt, comment_score=self.comments[cmt].score)
                cmt_score.append(cws)
            
            yield Reddit_pb2.MonitorUpdateResponse(post_score=post_score, comment_score=cmt_score)




def serve(host:str, port:int, num_workers:int = 10):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=num_workers))
    Reddit_pb2_grpc.add_RedditServiceServicer_to_server(RedditServiceServicer(), server)
    server.add_insecure_port(f'{host}:{port}')
    print(f"Server starting on port {port}...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="gRPC Server Argument Parser")

    # Host argument
    parser.add_argument('--host', type=str, default='localhost',
                        help='Host where the server will run (default: localhost)')

    # Port argument
    parser.add_argument('--port', type=int, default=50051,
                        help='Port where the server will listen (default: 50051)')

    # Number of workers
    parser.add_argument('--num_workers', type=int, default=10,
                        help='Number of worker threads (default: 10)')

    args = parser.parse_args()

    serve(args.host, args.port, args.num_workers)