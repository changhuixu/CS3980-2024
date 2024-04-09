import logging
from auth.authenticate import authenticate
from beanie import PydanticObjectId
from database.connection import Database
from fastapi import APIRouter, Depends, HTTPException, status
from models.events import Event, EventUpdate

logger = logging.getLogger(__name__)

event_router = APIRouter(tags=["Events"])

event_database = Database(Event)


@event_router.get("/", response_model=list[Event])
async def retrieve_all_events() -> list[Event]:
    events = await event_database.get_all()
    logger.info(f"viewing {len(events)} events")
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    logger.info(f"viewing event #{id} details.")
    event = await event_database.get(id)
    if not event:
        logger.warning(f"\t The event #{id} NOT Found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
    return event


@event_router.post("/new")
async def create_event(body: Event, user: str = Depends(authenticate)) -> dict:
    body.creator = user
    logger.info(f"User [{user}] is creating an event.")
    id = await event_database.save(body)
    logger.info(f"\t A new event #[{id}] created.")
    return {"message": "Event created successfully"}


@event_router.put("/{id}", response_model=Event)
async def update_event(
    id: PydanticObjectId, body: EventUpdate, user: str = Depends(authenticate)
) -> Event:
    logger.info(f"User [{user}] is updating event #{id}.")
    event = await event_database.get(id)
    if not event:
        logger.warning(f"\t The event #{id} NOT Found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Operation not allowed"
        )
    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
    logger.info(f"\t Event #[{id}] is updated.")
    return updated_event


@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId, user: str = Depends(authenticate)) -> dict:
    logger.info(f"User [{user}] is deleting event #{id}.")
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )
    if not event:
        logger.warning(f"\t The event #{id} NOT Found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Operation not allowed"
        )
    event = await event_database.delete(id)
    logger.info(f"\t Event #[{id}] is deleted.")
    return {"message": "Event deleted successfully."}
