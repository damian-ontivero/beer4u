from .delete_command import DeleteStoreCommand
from .delete_command_handler import DeleteStoreCommandHandler
from .register_command import RegisterStoreCommand
from .register_command_handler import RegisterStoreCommandHandler
from .update_command import UpdateStoreCommand
from .update_command_handler import UpdateStoreCommandHandler

STORE_COMMAND_HANDLERS = {
    RegisterStoreCommand: RegisterStoreCommandHandler,
    UpdateStoreCommand: UpdateStoreCommandHandler,
    DeleteStoreCommand: DeleteStoreCommandHandler,
}
