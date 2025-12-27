from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

comment = Comment(
    id=1,
    content="First Comment",
    replies = [
        Comment(id=11, content="First Reply"),
        Comment(id=12, content="Second Reply"),
        Comment(id=13, content="Third Reply", replies= [
            Comment(id=131, content="First Reply"),
            Comment(id=132, content="Second Reply"),
        ]),
    ]
)

print(comment)
