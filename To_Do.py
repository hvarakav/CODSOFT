class WorkItem:
  """Represents a single work item with a description and progress stage."""

  def __init__(self, description, stage="To Begin"):
      """Initializes the work item with its description and starting stage."""
      self.description = description
      self.stage = stage

  def restart(self):
      """Resets the work item's stage back to 'To Begin'."""
      self.stage = "To Begin"


class WorkTracker:
  """Manages a collection of WorkItems."""

  def __init__(self):
      """Initializes an empty work list."""
      self.work_list = []

  def add_work(self, item):
      """Adds a new WorkItem to the list."""
      self.work_list.append(item)
      print(f"Work '{item.description}' added successfully!")

  def update_work_stage(self, description, new_stage):
      """Updates the stage of a specific WorkItem."""
      for item in self.work_list:
          if item.description == description:
              item.stage = new_stage
              print(f"Work '{description}' stage updated successfully!")
              return True
      return False

  def display_all_work(self):
      """Shows all WorkItems and their current stages."""
      if not self.work_list:
          print("No work currently tracked.")
      else:
          for item in self.work_list:
              print(f"{item.description} - Stage: {item.stage}")

  def remove_work(self, description):
      """Removes a WorkItem by description from the list."""
      for i, item in enumerate(self.work_list):
          if item.description == description:
              del self.work_list[i]
              print(f"Work '{description}' removed successfully!")
              return True
      return False


def main():
  work_tracker = WorkTracker()

  while True:
      print("\n===== Work Tracking Menu =====")
      print("1. Add Work Item")
      print("2. Update Work Stage")
      print("3. Display All Work")
      print("4. Restart Work Item")
      print("5. Remove Work Item")
      print("6. Exit")

      choice = input("Enter your choice (1/2/3/4/5/6): ")

      if choice == "1":
          work_description = input("Enter work description: ")
          new_work = WorkItem(work_description)
          work_tracker.add_work(new_work)

      elif choice == "2":
          work_description = input("Enter work description: ")
          new_stage = input("Enter new stage (To Begin, In Progress, Completed): ")
          if work_tracker.update_work_stage(work_description, new_stage):
              pass

      elif choice == "3":
          work_tracker.display_all_work()

      elif choice == "4":
          work_description = input("Enter work description to restart: ")
          if work_tracker.remove_work(work_description):
              work_tracker.add_work(WorkItem(work_description))  # Simulates restart

      elif choice == "5":
          work_tracker.remove_work(input("Enter work description to remove: "))

      elif choice == "6":
          print("Exiting the Work Tracking application. Goodbye!")
          break

      else:
          print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
  main()