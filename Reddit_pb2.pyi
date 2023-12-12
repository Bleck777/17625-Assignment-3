from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("user_ID",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_ID: str
    def __init__(self, user_ID: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ("title", "text", "video_url", "image_url", "author", "score", "status", "pub_date", "post_id", "parent_subreddit_id")
    class PostState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NORMAL: _ClassVar[Post.PostState]
        HIDDEN: _ClassVar[Post.PostState]
        LOCKED: _ClassVar[Post.PostState]
    NORMAL: Post.PostState
    HIDDEN: Post.PostState
    LOCKED: Post.PostState
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUB_DATE_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SUBREDDIT_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    video_url: str
    image_url: str
    author: str
    score: int
    status: Post.PostState
    pub_date: str
    post_id: str
    parent_subreddit_id: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ..., author: _Optional[str] = ..., score: _Optional[int] = ..., status: _Optional[_Union[Post.PostState, str]] = ..., pub_date: _Optional[str] = ..., post_id: _Optional[str] = ..., parent_subreddit_id: _Optional[str] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ("parent_id", "author", "text", "score", "status", "pub_date", "comment_id")
    class CommentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NORMAL: _ClassVar[Comment.CommentState]
        HIDDEN: _ClassVar[Comment.CommentState]
    NORMAL: Comment.CommentState
    HIDDEN: Comment.CommentState
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUB_DATE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    parent_id: str
    author: str
    text: str
    score: int
    status: Comment.CommentState
    pub_date: str
    comment_id: str
    def __init__(self, parent_id: _Optional[str] = ..., author: _Optional[str] = ..., text: _Optional[str] = ..., score: _Optional[int] = ..., status: _Optional[_Union[Comment.CommentState, str]] = ..., pub_date: _Optional[str] = ..., comment_id: _Optional[str] = ...) -> None: ...

class Subreddit(_message.Message):
    __slots__ = ("subreddit_id", "name", "status", "tags")
    class SubredditState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PUBLIC: _ClassVar[Subreddit.SubredditState]
        PRIVATE: _ClassVar[Subreddit.SubredditState]
        HIDDEN: _ClassVar[Subreddit.SubredditState]
    PUBLIC: Subreddit.SubredditState
    PRIVATE: Subreddit.SubredditState
    HIDDEN: Subreddit.SubredditState
    SUBREDDIT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    subreddit_id: str
    name: str
    status: Subreddit.SubredditState
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, subreddit_id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[Subreddit.SubredditState, str]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class PostRequest(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class CommentRequest(_message.Message):
    __slots__ = ("comment_id",)
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    def __init__(self, comment_id: _Optional[str] = ...) -> None: ...

class GetNMostRequest(_message.Message):
    __slots__ = ("post_id", "N")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    N: int
    def __init__(self, post_id: _Optional[str] = ..., N: _Optional[int] = ...) -> None: ...

class GetNMostResponse(_message.Message):
    __slots__ = ("most_comment",)
    MOST_COMMENT_FIELD_NUMBER: _ClassVar[int]
    most_comment: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, most_comment: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class ExpandCommentRequest(_message.Message):
    __slots__ = ("comment_id", "N")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    N: int
    def __init__(self, comment_id: _Optional[str] = ..., N: _Optional[int] = ...) -> None: ...

class ExpandCommentResponse(_message.Message):
    __slots__ = ("root_comment", "expanded_comments")
    ROOT_COMMENT_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    root_comment: Comment
    expanded_comments: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, root_comment: _Optional[_Union[Comment, _Mapping]] = ..., expanded_comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class MonitorUpdateRequest(_message.Message):
    __slots__ = ("post_id", "comment_id")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    comment_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, post_id: _Optional[str] = ..., comment_id: _Optional[_Iterable[str]] = ...) -> None: ...

class CommentWithScore(_message.Message):
    __slots__ = ("comment_id", "comment_score")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_SCORE_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    comment_score: int
    def __init__(self, comment_id: _Optional[str] = ..., comment_score: _Optional[int] = ...) -> None: ...

class MonitorUpdateResponse(_message.Message):
    __slots__ = ("post_score", "comment_score")
    POST_SCORE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_SCORE_FIELD_NUMBER: _ClassVar[int]
    post_score: int
    comment_score: _containers.RepeatedCompositeFieldContainer[CommentWithScore]
    def __init__(self, post_score: _Optional[int] = ..., comment_score: _Optional[_Iterable[_Union[CommentWithScore, _Mapping]]] = ...) -> None: ...
