# PROJECT__SIMPLE_CONTACT_BOOK_COOMAND_LINE


class Contacts:
    def details(self):
        phone_number = input("Enter the phone number: ").strip()
        if len(phone_number) != 10 or not phone_number.isdigit():
            print("Enter a valid 10-digit phone number")
            return False
        
        name = input("Enter the name: ").strip()
        if not name:
            print("Name cannot be empty")
            return False
            
        gmail = input("Enter your gmail: ").strip()
        if not gmail or "@" not in gmail:
            print("Enter a valid email address")
            return False

        with open("details.txt", "a") as f:
            f.write(f"name:{name},number:{phone_number},gmail:{gmail}\n")
            print("Contact saved successfully.")
        return True
    
    def addition(self):
        self.details()
    
    def delete(self):
        phone_number = input("Enter the phone number you want to delete: ").strip()
        if len(phone_number) != 10 or not phone_number.isdigit():
            print("Enter a valid 10-digit phone number")
            return
        
        try:
            with open("details.txt", "r") as f:
                lines = f.readlines()
            
            with open("details.txt", "w") as f:
                found = False
                for line in lines:
                    if phone_number not in line:
                        f.write(line)  
                    else:
                        found = True
                
                if found:
                    print("The contact has been deleted")
                else:
                    print("The contact was not found")
                    
        except FileNotFoundError:
            print("No contacts file found. Please add contacts first.")
    
    def view(self):
        try:
            with open("details.txt", "r") as f:
                content = f.read()
                if content.strip():
                    print("All contacts:")
                    print(content)
                else:
                    print("No contacts found.")
        except FileNotFoundError:
            print("No contacts file found. Please add contacts first.")
    
    def search(self):
        name = input("Enter the name you want to search: ").strip().lower()
        if not name:
            print("Name cannot be empty")
            return
            
        found = False
        try:
            with open("details.txt", "r") as f:
                lines = f.readlines()  
            
            for line in lines:
                if name in line.lower():
                    print(line.strip())
                    found = True
            
            if found:
                print("Contact(s) found")
            else:
                print("Contact not found")
                
        except FileNotFoundError:
            print("No contacts file found. Please add contacts first.")
    
    def ask(self):
        while True:
            choice = input("Do you want to (add/del/view/search/exit) contacts? ").strip().lower()
            
            if choice == "add":
                self.addition()
            elif choice == "del":
                self.delete()
            elif choice == "view":
                self.view()
            elif choice == "search":
                self.search()
            elif choice == "exit":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose: add, del, view, search, or exit")


if __name__ == "__main__":
    contact_manager = Contacts()
    contact_manager.ask()