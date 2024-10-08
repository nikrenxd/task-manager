from typing import Annotated
from fastapi import Depends, Query

from src.users.models import User
from src.users.dependencies import get_current_user

from src.tasks.schemas import STaskUpdate
from src.tasks.models import Priority


class ParamsWithId:
    def __init__(
        self,
        collection_slug: str,
        task_id: int,
        user: Annotated[User, Depends(get_current_user)],
    ):
        self.collection_slug = collection_slug
        self.task_id = task_id
        self.user = user


class FindParams:
    def __init__(
        self,
        user: Annotated[User, Depends(get_current_user)],
        collection_slug: str,
        done: Annotated[bool, Query()] = False,
        priority: Annotated[Priority, Query()] = None,
        important: Annotated[bool, Query()] = None,
    ):
        self.user = user
        self.collection_slug = collection_slug
        self.done = done
        self.priority = priority
        self.important = important


class UpdateParams(ParamsWithId):
    def __init__(
        self,
        collection_slug: str,
        body: STaskUpdate,
        task_id: int,
        user: Annotated[User, Depends(get_current_user)],
    ):
        self.body = body
        super().__init__(collection_slug, task_id, user)
