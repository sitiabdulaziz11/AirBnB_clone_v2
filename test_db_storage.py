# test_db_storage.py
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.state import State  # Ensure you have the State model implemented
from os import getenv

# Initialize the storage
storage = DBStorage()
storage.reload()

# Create a new State object
new_state = State(name="California")

# Save the new state object to the database
storage.new(new_state)
storage.save()

# Retrieve all states
all_states = storage.all(State)
print(f"All states: {all_states}")

# Check if the new state is saved
state_id = new_state.id
retrieved_state = all_states.get(f"State.{state_id}")
print(f"Retrieved state: {retrieved_state}")

# Update the state object
if retrieved_state:
    retrieved_state.name = "New California"
    storage.save()

# Retrieve again to check the update
updated_states = storage.all(State)
updated_state = updated_states.get(f"State.{state_id}")
print(f"Updated state: {updated_state}")

# Delete the state object
if updated_state:
    storage.delete(updated_state)
    storage.save()

# Verify deletion
final_states = storage.all(State)
print(f"Final states after deletion: {final_states}")
