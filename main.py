import event
import location
import person
from record import Record
from crime import Crime
import hallway


    

    
def define_everything():
    kitchen = location.Location("Kitchen",4)
    living_room = location.Location("Living Room", 6)
    hallway1 = hallway.Hallway("Hallway 1",kitchen, living_room)
    john = person.Person(
        "John Doe",
        30,
        events={
            0: event.Event("enter", {"location": kitchen}, "movement"),
            1: event.Event("leave", {"location": kitchen}, "movement"),
            3: event.Event("enter", {"location": living_room}, "movement")
        }
    )

    alice = person.Person(
        "Alice Smith",
        25,
        events={
            0: event.Event("enter", {"location": kitchen}, "movement"),
            3: event.Event("enter", {"location": living_room}, "movement"),  # moved later
            4: event.Event("die", {"location": living_room, "cause": "unknown"}, "status")
        }
    )

    jeff = person.Person(
        "Jeff Stein",
        40,
        events={
            0: event.Event("enter", {"location": kitchen}, "movement"),
            3: event.Event("leave", {"location": kitchen}, "movement")
        }
    )

    bob = person.Person(
        "Bob Brown",
        50,
        events={
            0: event.Event("enter", {"location": kitchen}, "movement"),
            2: event.Event("die", {"location": kitchen, "cause": "unknown"}, "status")
        }
    )

    return john, alice, jeff, bob, kitchen, living_room, hallway1
   
def record_processing(people, time, recordlog):
    for person in people:
        location = person.get_location(time)
        recordlog.append(Record(person, location, time))
    return recordlog
    
def sherlock_holmes(recordlog, victim_name, time_of_crime, location_of_crime):
    suspects = []
    for record in recordlog:

        if (record.get_time() == time_of_crime and record.get_location() == location_of_crime and is_alive_at(record.get_person(), time_of_crime) != False):
            print(f"{record.get_person().get_name()} is a suspect.")
            suspects.append(record.get_person().get_name())
    return suspects
def judge(suspects, victim_name):
    if len(suspects) == 1:
        print(f"{suspects[0]} is the culprit who killed {victim_name}.")
    elif len(suspects) > 1:
        print(f"Multiple suspects: {', '.join(suspects)}. Further investigation needed.")
def is_alive_at(person, time):
    for t, event in sorted(person.events.items()):
        if t > time:
            break
        if event.get_name() == "die":
            return False
    return True
def check_alibi(person):
    pass

if __name__ == "__main__":
    john, alice, jeff, bob, kitchen, living_room, hallway1 = define_everything()

    crime1 = Crime("Bob Brown", 2, kitchen, "Homicide")
    crime2 = Crime("Alice Smith", 4, living_room, "Homicide")
    crimes=[crime1, crime2]
    recordlog = []
    suspects = []
    recordlog=record_processing([john, alice, jeff, bob], 1, recordlog)
    recordlog=record_processing([john, alice, jeff, bob], 2, recordlog)
    recordlog=record_processing([john, alice, jeff, bob], 3, recordlog)
    recordlog=record_processing([john, alice, jeff, bob], 4, recordlog)
    for crime in crimes:
        print(f"Investigating crime: {crime.get_crime_type()} of {crime.get_victim()} at {crime.get_time()} in {crime.get_location().get_name()}")
        suspects = sherlock_holmes(recordlog, crime.get_victim(), crime.get_time(), crime.get_location())
        judge(suspects, crime.get_victim())

    input("\nPress Enter to exit...")
