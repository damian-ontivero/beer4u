from .delete_command import DeleteBeerCommand
from .delete_command_handler import DeleteBeerCommandHandler
from .register_command import RegisterBeerCommand
from .register_command_handler import RegisterBeerCommandHandler
from .update_command import UpdateBeerCommand
from .update_command_handler import UpdateBeerCommandHandler

BEER_COMMAND_HANDLERS = {
    RegisterBeerCommand: RegisterBeerCommandHandler,
    UpdateBeerCommand: UpdateBeerCommandHandler,
    DeleteBeerCommand: DeleteBeerCommandHandler,
}
