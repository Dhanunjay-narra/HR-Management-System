"""
Domain Event Bus
Provides loose coupling across business modules through asynchronous event publishing and subscriptions.
"""
import asyncio
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional
from app.core.logging import logger


@dataclass
class DomainEvent:
    event_type: str
    tenant_id: Optional[str]
    actor_id: Optional[str]
    payload: Dict[str, Any]
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    event_id: Optional[str] = None


EventHandler = Callable[[DomainEvent], Any]


class EventBus:
    """Asynchronous In-Memory Event Dispatcher."""

    def __init__(self) -> None:
        self._subscribers: Dict[str, List[EventHandler]] = {}
        self._wildcard_subscribers: List[EventHandler] = []

    def subscribe(self, event_type: str, handler: EventHandler) -> None:
        """Subscribe a handler to a specific event type."""
        if event_type == "*":
            self._wildcard_subscribers.append(handler)
        else:
            if event_type not in self._subscribers:
                self._subscribers[event_type] = []
            self._subscribers[event_type].append(handler)
        logger.info(f"Subscribed handler '{handler.__name__}' to event '{event_type}'")

    async def publish(self, event: DomainEvent) -> None:
        """Publish an event to all matching subscribers."""
        logger.info(f"Publishing domain event: {event.event_type} (Tenant: {event.tenant_id})")
        handlers: List[EventHandler] = []

        if event.event_type in self._subscribers:
            handlers.extend(self._subscribers[event.event_type])
        handlers.extend(self._wildcard_subscribers)

        # Also support prefix wildcards (e.g. "employee.*")
        prefix = event.event_type.split(".")[0] + ".*"
        if prefix in self._subscribers:
            handlers.extend(self._subscribers[prefix])

        for handler in handlers:
            try:
                if asyncio.iscoroutinefunction(handler):
                    asyncio.create_task(handler(event))
                else:
                    handler(event)
            except Exception as e:
                logger.error(f"Error executing event handler {handler.__name__} for {event.event_type}: {e}", exc_info=True)


event_bus = EventBus()
