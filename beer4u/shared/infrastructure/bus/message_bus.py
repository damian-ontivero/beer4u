from beer4u.shared.domain.bus.command import Command
from beer4u.shared.domain.bus.query import Query

Message = Command | Query


class MessageBus:
    
