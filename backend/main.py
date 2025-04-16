import os
import json
from datetime import datetime

class NotesApp:
    def __init__(self):
        self.notes = []
        self.file_path = "notes.json"
        self.load_notes()

    def load_notes(self):
        """Load notes from JSON file if it exists."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    self.notes = json.load(file)
            except json.JSONDecodeError:
                print("Error reading notes file. Starting with empty notes.")
                self.notes = []
        else:
            print("Notes file not found. Starting with empty notes.")

    def save_notes(self):
        """Save notes to JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.notes, file, indent=4)
        print("Notes saved successfully!")

    def add_note(self, title, content):
        """Add a new note."""
        note_id = len(self.notes) + 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        new_note = {
            "id": note_id,
            "title": title,
            "content": content,
            "created_at": timestamp,
            "updated_at": timestamp
        }
        
        self.notes.append(new_note)
        self.save_notes()
        print(f"Note '{title}' added successfully with ID: {note_id}")
        return note_id

    def view_all_notes(self):
        """Display all notes."""
        if not self.notes:
            print("No notes found.")
            return
        
        print("\n===== ALL NOTES =====")
        for note in self.notes:
            print(f"ID: {note['id']} | Title: {note['title']} | Created: {note['created_at']}")
        print("====================\n")

    def view_note(self, note_id):
        """View a specific note by ID."""
        for note in self.notes:
            if note['id'] == note_id:
                print("\n===== NOTE DETAILS =====")
                print(f"ID: {note['id']}")
                print(f"Title: {note['title']}")
                print(f"Content: {note['content']}")
                print(f"Created: {note['created_at']}")
                print(f"Last Updated: {note['updated_at']}")
                print("=======================\n")
                return
        print(f"Note with ID {note_id} not found.")

    def update_note(self, note_id, title=None, content=None):
        """Update an existing note."""
        for note in self.notes:
            if note['id'] == note_id:
                if title:
                    note['title'] = title
                if content:
                    note['content'] = content
                note['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print(f"Note with ID {note_id} updated successfully!")
                return
        print(f"Note with ID {note_id} not found.")

    def delete_note(self, note_id):
        """Delete a note by ID."""
        for i, note in enumerate(self.notes):
            if note['id'] == note_id:
                removed_note = self.notes.pop(i)
                self.save_notes()
                print(f"Note '{removed_note['title']}' deleted successfully!")
                return
        print(f"Note with ID {note_id} not found.")

    def search_notes(self, query):
        """Search notes by title or content."""
        query = query.lower()
        results = []
        
        for note in self.notes:
            if query in note['title'].lower() or query in note['content'].lower():
                results.append(note)
        
        if results:
            print(f"\n===== SEARCH RESULTS FOR '{query}' =====")
            for note in results:
                print(f"ID: {note['id']} | Title: {note['title']}")
            print("=======================\n")
        else:
            print(f"No notes found matching '{query}'.")


def main():
    app = NotesApp()
    
    while True:
        print("\n===== NOTES APP =====")
        print("1. Add a new note")
        print("2. View all notes")
        print("3. View note details")
        print("4. Update a note")
        print("5. Delete a note")
        print("6. Search notes")
        print("7. Exit")
        print("====================")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            app.add_note(title, content)
        
        elif choice == '2':
            app.view_all_notes()
        
        elif choice == '3':
            try:
                note_id = int(input("Enter note ID: "))
                app.view_note(note_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        
        elif choice == '4':
            try:
                note_id = int(input("Enter note ID to update: "))
                title = input("Enter new title (leave empty to keep current): ")
                content = input("Enter new content (leave empty to keep current): ")
                app.update_note(note_id, title if title else None, content if content else None)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        
        elif choice == '5':
            try:
                note_id = int(input("Enter note ID to delete: "))
                app.delete_note(note_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        
        elif choice == '6':
            query = input("Enter search term: ")
            app.search_notes(query)
        
        elif choice == '7':
            print("Thank you for using Notes App. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
