import datetime
import sys

'''global id for mapping a creation a unique note'''
last_id = 0

class Note:

    '''represent a note in the notebook'''

    def __init__(self, memo, tags=''):

        '''initialize a note with memo and optional space-separated tags. Automatically set the note's creation date and a unique id'''

        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
    
    def match_filter(self, filter):

        '''determine if the notes mathcs with the filter'''
        
        return filter in self.memo or filter in self.tags

    
class Notebook:

    '''Represent a collection of notes that can be tagged, modified, and searched.'''

    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.
        call a Note object and append'''
        self.notes.append(Note(memo, tags=''))
    
    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its memo to the given value.'''

        note = self._find_note_id(note_id)
        if note:
            note.memo = memo
            return True
        return False
        
    def search(self, filter):
        '''find all notes that given a correct filter'''

        return[note for note in self.notes if note.match_filter(filter)]
    
    def _find_note_id(self, note_id):
        '''Locate the note with the given id.'''

        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
    
    def modify_memo_id(self, note_id, memo):
        '''Find the note with the given id and change its memo to the given value.'''

        self.find_note_id(note_id).memo = memo
    



class Menu:
    '''Display a menu and respond to choices when run.'''

    def __init__(self):

        self.notebook = Notebook()
        self.choice = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_notes,
            "4": self.modify_note,
            "5": self.quit
        }              
    
    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)

    def run(self):

        while True:
            self.display_menu()
            choice = input("Enter a option: ")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
    
    def add_notes(self):
        
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")
    
    def modify_note(self):
        
        id = input("Enter a id note: ")
        memo = input("Type a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo_id(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)
    

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
