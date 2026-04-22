import main
from crime import Crime
from person import Person
from location import Location
from event import Event

def print_banner():
    print("="*50)
    print("   INTERACTIVE MURDER MYSTERY SOLVER")
    print("="*50)

def custom_scenario():
    print("\n--- Phase 1: Setup Locations ---")
    locations = {}
    num_locs = int(input("How many locations? "))
    for i in range(num_locs):
        name = input(f"  Name for Location {i+1}: ")
        size = int(input(f"  Size of {name} (integer): "))
        locations[name] = Location(name, size)
        
    print("\n--- Phase 2: Setup People & Timelines ---")
    people = []
    num_people = int(input("How many people? "))
    for i in range(num_people):
        name = input(f"\n  Name of Person {i+1}: ")
        
        events = {}
        num_events = int(input(f"  How many timeline events for {name}? "))
        for j in range(num_events):
            t = int(input(f"    Time of event {j+1} (integer): "))
            action = input(f"    Action (e.g., enter, leave, die): ")
            loc_name = input(f"    Location name for this action: ")
            
            if loc_name in locations:
                events[t] = Event(action, {"location": locations[loc_name]}, "movement" if action != "die" else "status")
            else:
                print(f"    [!] Unknown location {loc_name}. Skipping event.")
                
        people.append(Person(name, events=events))
        
    print("\n--- Phase 3: Define Crimes to Investigate ---")
    crimes = []
    num_crimes = int(input("How many crimes occurred? "))
    for i in range(num_crimes):
        victim = input(f"\n  Victim of Crime {i+1}: ")
        t = int(input(f"  Time of Crime {i+1} (integer): "))
        loc_name = input(f"  Location of Crime {i+1}: ")
        crime_type = input(f"  Type of Crime {i+1} (e.g., Homicide): ")
        
        if loc_name in locations:
            crimes.append(Crime(victim, t, locations[loc_name], crime_type))
        else:
            print(f"  [!] Unknown location. Skipping crime.")
            
    return people, list(locations.values()), crimes

def run_app():
    print_banner()
    print("1. Load pre-built scenario (Mansion Murder)")
    print("2. Create custom mystery")
    choice = input("\nSelect an option (1 or 2): ").strip()
    
    if choice == "1":
        john, alice, jeff, bob, kitchen, living_room, hallway1 = main.define_everything()
        people = [john, alice, jeff, bob]
        locations = [kitchen, living_room, hallway1]
        crime1 = Crime("Bob Brown", 2, kitchen, "Homicide")
        crime2 = Crime("Alice Smith", 4, living_room, "Homicide")
        crimes = [crime1, crime2]
    else:
        people, locations, crimes = custom_scenario()
        
    if not crimes:
        print("No crimes to investigate. Exiting.")
        return
        
    # Process timelines into log
    max_time = max([c.get_time() for c in crimes] + [0]) + 1
    recordlog = []
    for t in range(max_time + 1):
        recordlog = main.record_processing(people, t, recordlog)
        
    print("\n" + "="*50)
    print("COMMENCING INVESTIGATION")
    print("="*50)
    
    for crime in crimes:
        print(f"\nInvestigating crime: {crime.get_crime_type()} of {crime.get_victim()} at {crime.get_time()} in {crime.get_location().get_name()}")
        suspects = main.sherlock_holmes(recordlog, crime.get_victim(), crime.get_time(), crime.get_location())
        main.judge(suspects, crime.get_victim())

    input("\nCase Closed. Press Enter to exit...")

if __name__ == "__main__":
    try:
        run_app()
    except Exception as e:
        print(f"An error occurred: {e}")