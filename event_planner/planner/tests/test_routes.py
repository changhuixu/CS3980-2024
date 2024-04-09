from httpx import AsyncClient
import pytest

from auth.jwt_handler import create_access_token
from models.events import Event, EventUpdate


@pytest.fixture
async def access_token() -> str:
    return create_access_token("python-web-dev@cs.uiowa.edu")


@pytest.fixture
async def mock_event() -> Event:
    # Clean up resources
    await Event.find_all().delete()

    new_event = Event(
        creator="python-web-dev@cs.uiowa.edu",
        title="Project 2 Presentation",
        image="https://placehold.co/600x400?text=Project+1+Presentation",
        description="Each student will present their FastAPI project to demo basic CRUD operations.",
        tags=[
            "python",
            "fastapi",
            "project",
            "presentation",
            "midterm exam",
        ],
        location="168 VAN",
    )

    await Event.insert_one(new_event)

    return new_event


@pytest.mark.anyio
async def test_get_events(default_client: AsyncClient, mock_event: Event) -> None:
    response = await default_client.get("/events/")

    assert response.status_code == 200
    assert response.json()[0]["_id"] == str(mock_event.id)


@pytest.mark.anyio
async def test_get_event(default_client: AsyncClient, mock_event: Event) -> None:
    url = f"/events/{str(mock_event.id)}"
    response = await default_client.get(url)

    assert response.status_code == 200
    assert response.json()["creator"] == mock_event.creator
    assert response.json()["_id"] == str(mock_event.id)


@pytest.mark.anyio
async def test_post_event(default_client: AsyncClient, access_token: str) -> None:
    payload = {
        "title": "Project 1 Presentation",
        "image": "https://placehold.co/600x400?text=Project+1+Presentation",
        "description": "Each student will present their FastAPI project to demo basic CRUD operations.",
        "tags": [
            "python",
            "fastapi",
            "project",
            "presentation",
            "midterm exam",
        ],
        "location": "168 VAN",
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    test_response = {"message": "Event created successfully"}

    response = await default_client.post("/events/new", json=payload, headers=headers)

    assert response.status_code == 200
    assert response.json() == test_response


@pytest.mark.anyio
async def test_get_events_count(default_client: AsyncClient) -> None:
    response = await default_client.get("/events/")

    events = response.json()

    assert response.status_code == 200
    assert len(events) == 2


@pytest.mark.anyio
async def test_update_event(
    default_client: AsyncClient, mock_event: Event, access_token: str
) -> None:
    test_payload = EventUpdate(title="Project #1 Presentation")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    url = f"/events/{str(mock_event.id)}"

    response = await default_client.put(
        url, data=test_payload.model_dump_json(), headers=headers
    )

    assert response.status_code == 200
    assert response.json()["title"] == test_payload.title


@pytest.mark.anyio
async def test_delete_event(
    default_client: AsyncClient, mock_event: Event, access_token: str
) -> None:
    test_response = {"message": "Event deleted successfully."}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    url = f"/events/{mock_event.id}"

    response = await default_client.delete(url, headers=headers)

    assert response.status_code == 200
    assert response.json() == test_response


@pytest.mark.anyio
async def test_get_event_again(default_client: AsyncClient, mock_event: Event) -> None:
    url = f"/events/{str(mock_event.id)}"
    response = await default_client.get(url)

    assert response.status_code == 200
