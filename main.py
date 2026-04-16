import event
import person
from record import Record
def main():
    john = person.Person(
        "John Doe",
        30,
        events={
            0: event.Event("enter", {"location": "Kitchen"}, "movement"),
            1: event.Event("leave", {"location": "Kitchen"}, "movement"),
            2: event.Event("enter", {"location": "Living Room"}, "movement")
        }
    )

    alice = person.Person(
        "Alice Smith",
        25,
        events={
            0: event.Event("enter", {"location": "Kitchen"}, "movement"),
            2: event.Event("die", {"location": "Kitchen", "cause": "unknown"}, "status")
        }
    )

    jeff = person.Person(
        "Jeff Stein",
        40,
        events={
            0: event.Event("enter", {"location": "Kitchen"}, "movement"),
            3: event.Event("leave", {"location": "Kitchen"}, "movement")
        }
    )
    
    return john, alice, jeff
   
def record_processing(people, time,recordlog):
    for person in people:
        location = person.get_location(time)
        #print(f"{person.get_name()} is at {location} at time {time}.")
        recordlog.append(Record(person, location, time))
    return recordlog
    
def sherlock_holmes(recordlog, victim_name, time_of_death):
    for record in recordlog:
        if record.get_location() == "Kitchen" and record.get_time() == time_of_death and record.get_person().get_name() != victim_name:
            print(f"{record.get_person().get_name()} is a suspect.")
if __name__ == "__main__":
    john, alice, jeff = main()
    recordlog = []
    recordlog=record_processing([john, alice, jeff], 1, recordlog)
    recordlog=record_processing([john, alice, jeff], 2, recordlog)
    recordlog=record_processing([john, alice, jeff], 3, recordlog)
    sherlock_holmes(recordlog, "Alice Smith", 2)
