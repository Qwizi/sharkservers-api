import random

from fastapi_events.handlers.local import local_handler
from fastapi_events.typing import Event

from src.auth.schemas import RegisterUserSchema
from src.enums import MainEventEnum
from src.forum.enums import CategoryTypeEnum, ThreadStatusEnum
from src.logger import logger
from src.settings import get_settings

settings = get_settings()


def log_debug_event(event: Event):
    if settings.DEBUG:
        event_name, payload = event
        logger.debug(f"Event {event_name} with payload {payload}")


@local_handler.register(event_name="*")
async def handle_all_events_and_debug_log(event: Event):
    event_name, payload = event
    log_debug_event(event)


@local_handler.register(event_name=MainEventEnum.INSTALL)
async def handle_install_event(event: Event):
    pass


@local_handler.register(event_name="GENERATE_RANDOM_DATA")
async def generate_random_data(event: Event):
    logger.info("Generating random data")
    event_name, payload = event
    auth_service = payload.get("auth_service")
    categories_service = payload.get("categories_service")
    threads_service = payload.get("threads_service")
    posts_service = payload.get("posts_service")
    servers_service = payload.get("servers_service")

    users_list = []
    for i in range(10):
        new_user = await auth_service.register(
            user_data=RegisterUserSchema(
                username=f"TestUser{i}",
                password="test123456",
                password2="test123456",
                email=f"TestUser{i}@test.pl",
            )
        )
        users_list.append(new_user)
        logger.info(f"Created user {new_user.username}")

    categories_list = [await categories_service.create(
        name="Rekrutacja", description="Rekrutacja do ekipy",
        type=CategoryTypeEnum.APPLICATION
    )]
    for i in range(10):
        new_category = await categories_service.create(
            name=f"TestCategory{i}", description=f"Test description {i}"
        )
        categories_list.append(new_category)
        logger.info(f"Created category {new_category.name}")

    user = users_list[0]
    category = categories_list[0]
    threads_list = [
        await threads_service.create(
            category=category,
            title=f"Podanie na administratora",
            author=user,
            content="Test content {i}",
        )
    ]
    for i in range(100):
        user = random.choice(list(users_list))
        category = random.choice(list(categories_list))
        new_thread = await threads_service.create(
            category=category,
            title=f"Test thread {i}",
            author=user,
            content="Test content {i}",
        )
        threads_list.append(new_thread)
        logger.info(f"Created thread {new_thread.title}")

    for i in range(2):
        user = random.choice(list(users_list))
        category = random.choice(list(categories_list))
        new_thread = await threads_service.create(
            category=category,
            title=f"Test thread {i}",
            author=user,
            content="Test content {i}",
            is_pinned=True,
        )
        threads_list.append(new_thread)
        logger.info(f"Created thread {new_thread.title}")

    for i in range(3):
        user = random.choice(list(users_list))
        category = random.choice(list(categories_list))
        new_thread = await threads_service.create(
            category=category,
            title=f"Test thread {i}",
            author=user,
            content="Test content {i}",
            is_closed=True,
        )
        threads_list.append(new_thread)
        logger.info(f"Created thread {new_thread.title}")


    for i in range(4):
        user = random.choice(list(users_list))
        category = random.choice(list(categories_list))
        new_thread = await threads_service.create(
            category=category,
            title=f"Test thread {i}",
            author=user,
            content="Test content {i}",
            status=ThreadStatusEnum.REJECTED,
        )
        threads_list.append(new_thread)
        logger.info(f"Created thread {new_thread.title}")

    for i in range(5):
        user = random.choice(list(users_list))
        category = random.choice(list(categories_list))
        new_thread = await threads_service.create(
            category=category,
            title=f"Test thread {i}",
            author=user,
            content="Test content {i}",
            status=ThreadStatusEnum.APPROVED,
        )
        threads_list.append(new_thread)
        logger.info(f"Created thread {new_thread.title}")

    for i in range(100):
        user = random.choice(list(users_list))
        thread = random.choice(list(threads_list))
        new_post = await posts_service.create(
            author=user,
            content=f"Test post {i}",
        )
        await thread.posts.add(new_post)
        logger.info(f"Created post {new_post.content}")

    logger.info("Finished generating random data")
